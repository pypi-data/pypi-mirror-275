from src.grid_engine_Nitebound.grid_engine.core.component import Component
from pygame import Vector2
from math import exp
import numpy as np


class DistanceConstraint2D(Component):
    def __init__(self, parent, other, rest_length):
        super().__init__(parent)
        self.parent = parent
        self.other = other
        self.rest_length = rest_length

    def on_update(self, dt):
        super().on_update(dt)
        # Calculate the vector between the two bodies
        delta = self.other.transform.position - self.parent.transform.position
        # Calculate the current distance between the two bodies
        current_distance = delta.length()
        # Calculate the difference from the rest length
        difference = (current_distance - self.rest_length) / current_distance

        # Calculate the correction factor (optional: include mass in calculations)
        correction_factor = 0.5  # Split the correction 50/50 between the two bodies
        correction = delta * difference * correction_factor

        if not self.parent.is_kinematic:
            self.parent.transform.position -= correction

        if not self.other.is_kinematic:
            self.other.transform.position += correction


class RigidBody2D(Component):
    def __init__(self, parent, mass, drag=.1, angular_drag=.99, use_gravity=True, is_kinematic=False, is_trigger=False, velocity=Vector2(0, 0), angular_velocity=0, bounds=(0, 0, 1024, 768)):
        super().__init__(parent)
        self.mass = mass
        self.drag = drag
        self.angular_drag = angular_drag
        self.use_gravity = use_gravity
        self.is_kinematic = is_kinematic
        self.is_trigger = is_trigger
        self.velocity = Vector2(velocity)
        self.angular_velocity = angular_velocity
        self.bounds = bounds
        self.gravity = Vector2(0, 9.81)  # Earth's gravity in m/s^2
        self.restitution = .6
        self.center_of_mass = Vector2(self.parent.get_component("Transform").position)

    def calculate_inertia_tensor(self):
        # Simplified inertia for irregular objects; for demonstration, assume a rectangular approximation
        width = max(v[0] for v in self.parent.poly_collider.vertices) - min(
            v[0] for v in self.parent.poly_collider.vertices)
        height = max(v[1] for v in self.parent.poly_collider.vertices) - min(
            v[1] for v in self.parent.poly_collider.vertices)
        return (1 / 12) * self.mass * (width ** 2 + height ** 2)

    def apply_collision_response(self, collision_point, normal, penetration_depth):
        # Resolve penetration
        move_vector = normal * penetration_depth
        self.parent.transform.position += move_vector

        # Calculate lever arm
        r = collision_point - self.parent.poly_collider.center
        lever_arm_length = np.linalg.norm(r)
        if lever_arm_length == 0:
            return  # Avoid division by zero

        # Calculate torque: torque = r x F
        force_magnitude = np.dot(self.velocity, normal) * self.restitution  # Reflective force
        torque = np.cross(r, normal * force_magnitude)
        inertia_tensor = self.calculate_inertia_tensor()

        # Apply angular velocity change
        angular_impulse = torque / inertia_tensor
        self.angular_velocity += angular_impulse

    def set_parent(self, parent):
        self.parent = parent

    def apply_force(self, force):
        if not self.is_kinematic:
            acceleration = force / self.mass
            self.velocity += acceleration

    def apply_torque(self, torque):
        if not self.is_kinematic:
            angular_acceleration = torque / self.mass  # Simplified, consider moment of inertia for rotation
            self.angular_velocity += angular_acceleration

    def on_update(self, dt):
        super().on_update(dt)
        if self.use_gravity and not self.is_kinematic:
            self.apply_force(self.gravity * self.mass)
        self.parent.transform.position += self.velocity * dt
        self.parent.transform.rotation += self.angular_velocity * dt
        self.velocity *= exp(-self.drag * dt)
        self.angular_velocity *= exp(-self.angular_drag * dt)
        self.handle_collisions(dt)

    def handle_collisions(self, dt):
        # Get bounds of the polygon
        min_x = min(v[0] for v in self.parent.poly_collider.vertices)
        max_x = max(v[0] for v in self.parent.poly_collider.vertices)
        min_y = min(v[1] for v in self.parent.poly_collider.vertices)
        max_y = max(v[1] for v in self.parent.poly_collider.vertices)

        # Window dimensions
        # window_width, window_height = 1024, 768  # Example, replace with actual window size

        # Check and handle horizontal boundaries
        if min_x < 0:
            self.parent.transform.position.x += abs(min_x)
            self.velocity.x *= -self.restitution

        if max_x > self.bounds[2]:
            self.parent.transform.position.x -= (max_x - self.bounds[2])
            self.velocity.x *= -self.restitution

        # Check and handle vertical boundaries
        if min_y < 0:
            self.parent.transform.position.y += abs(min_y)
            self.velocity.y *= -self.restitution
        if max_y > self.bounds[3]:
            self.parent.transform.position.y -= (max_y - self.bounds[3])
            self.velocity.y *= -self.restitution

    def apply_boundary_torque(self, collider, normal):
        # Calculate point of impact - for simplicity, use centroid to boundary projection
        point_of_impact = collider.center + normal * (collider.radius if hasattr(collider, 'radius') else 0)
        lever_arm = point_of_impact - collider.center
        torque = np.cross(lever_arm, normal * self.mass * self.gravity.y)  # Cross product of lever arm and force vector
        self.angular_velocity += torque / self.mass  # Adjusting angular velocity based on torque

    def apply_gravity(self):
        if self.use_gravity and not self.is_kinematic:
            # Gravity applies at the center of mass
            force = self.gravity * self.mass
            # Calculate torque if center of mass is offset from the object's pivot
            com_offset = self.parent.poly_collider.calculate_centroid() - self.parent.transform.position
            torque = np.cross(com_offset, [force.x, force.y, 0])[2]  # Cross product in 3D, z-component is the torque

            self.apply_force(force)
            self.apply_torque(torque)

    def on_draw(self, dest, dt):
        super().on_draw(dest, dt)

