import pygame as pg
from pygame import Vector2
from src.grid_engine_Nitebound.grid_engine.core import Component
from src.grid_engine_Nitebound.grid_engine.core.toolkit import centroid, generate_uniform_poly
import numpy as np
from numpy import cos, sin, radians


class MinMax:
    def __init__(self):
        self.min = 0
        self.max = 0


def ensure_numpy_array(vertices):
    if not isinstance(vertices, np.ndarray):
        return np.array(vertices)
    return vertices


def rotate_vertex_about_point(vertex, angle, point):
    theta = radians(angle)
    rotated_vertex = np.dot(np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]]), (vertex - point)) + point
    return rotated_vertex


def rotate_vertices_about_point(vertices, theta, point):
    vertices = ensure_numpy_array(vertices)
    point = ensure_numpy_array(point)
    theta = np.radians(theta)
    c, s = np.cos(theta), np.sin(theta)
    rotation_matrix = np.array([[c, -s], [s, c]])
    translated_vertices = vertices - point
    rotated_vertices = np.dot(translated_vertices, rotation_matrix)
    return rotated_vertices + point


def translate_vertices(vertices, offset):
    vertices = ensure_numpy_array(vertices)
    offset = ensure_numpy_array(offset)
    return vertices + offset


def rotate_vertices(vertices, theta):
    vertices = ensure_numpy_array(vertices)
    theta = np.radians(theta)  # Convert angle to radians
    c, s = np.cos(theta), np.sin(theta)
    r = np.array([[c, -s], [s, c]])  # Rotation matrix
    return np.dot(vertices, r)  # Apply rotation


def scale_vertices(vertices, scale):
    vertices = ensure_numpy_array(vertices)
    scale_matrix = np.array([[scale, 0], [0, scale]]) if isinstance(scale, (int, float)) else np.array([[scale[0], 0], [0, scale[1]]])
    return np.dot(vertices, scale_matrix)


def find_max_min_projections(poly, axis):
    projections = [np.dot(vertex, axis) for vertex in poly.original_vertices]
    p_min = min(projections)
    p_max = max(projections)
    return MinMax(p_min, p_max)


def polygons_collide(poly1, poly2):
    normals1 = calculate_normals(poly1.vertices)
    normals2 = calculate_normals(poly2.vertices)
    minimum_overlap = None  # None means no overlap found yet
    smallest_axis = None  # The axis along which the minimum overlap occurs

    # Check all normals (axes) from both polygons
    for normal in normals1 + normals2:
        min1, max1 = find_projection_extremes(poly1.vertices, normal)
        min2, max2 = find_projection_extremes(poly2.vertices, normal)

        # Check for a gap in the projections; if found, no collision on this axis
        if max1 < min2 or max2 < min1:
            return False, None  # No collision detected, and no MTV needed

        # Calculate overlap on this axis
        overlap = min(max1, max2) - max(min1, min2)
        if minimum_overlap is None or overlap < minimum_overlap:
            minimum_overlap = overlap
            smallest_axis = normal

    # If we get here, all axes have some overlap, and we have the smallest one
    # Determine the direction to push poly1 to resolve the collision
    if poly1.parent.transform.position.dot(smallest_axis) < poly2.parent.transform.position.dot(smallest_axis):
        smallest_axis = -smallest_axis  # Ensure the MTV pushes poly1 away from poly2

    mtv = smallest_axis * minimum_overlap
    return True, mtv


def find_projection_extremes(vertices, axis):
    # Project all vertices onto the axis and find min/max
    min_proj = max_proj = vertices[0].dot(axis)
    for vertex in vertices[1:]:
        proj = vertex.dot(axis)
        if proj < min_proj:
            min_proj = proj
        if proj > max_proj:
            max_proj = proj
    return min_proj, max_proj


def update_polygon_vertices(vertices, position, rotation):
    center = centroid(vertices)
    rotated_vertices = [rotate_vertex_about_point(v, rotation, center) for v in vertices]
    translated_vertices = [v + position - center for v in rotated_vertices]
    return translated_vertices


def calculate_normals(vertices):
    normals = []
    for i in range(len(vertices)):
        next_index = (i + 1) % len(vertices)
        edge = vertices[next_index] - vertices[i]
        normal = np.array([-edge[1], edge[0]])
        normal_length = np.linalg.norm(normal)
        if normal_length != 0:
            normal = normal / normal_length
        normals.append(normal)
    return normals


# class PolyCollider(Component):
#     def __init__(self, parent, vertices):
#         super().__init__(parent)
#         self.vertices = np.array(vertices)
#         self.center = self.calculate_centroid()
#
#     def calculate_centroid(self):
#         if len(self.vertices) > 0:
#             return np.mean(self.vertices, axis=0)
#         return np.array([0, 0])
#
#     def move_out_of_collision(self, other):
#         collision, mtv = self.check_collision(other)
#         if collision:
#             # Calculate point of impact (simplified to midpoint between centroids for illustration)
#             impact_point = (self.center + other.center) / 2
#
#             # Apply translation
#             self.parent.transform.position -= mtv * 0.5
#             other.parent.transform.position += mtv * 0.5
#
#             # Calculate lever arms
#             lever_arm_self = impact_point - self.center
#             lever_arm_other = impact_point - other.center
#
#             # Calculate torque and apply angular velocities
#             torque_self = np.cross(lever_arm_self, -mtv)  # Negative because MTV pushes out
#             torque_other = np.cross(lever_arm_other, mtv)
#
#             # Here you might need to consider the object's moment of inertia to translate torque to angular velocity
#             # For simplicity, assuming a direct application:
#             self.parent.rigidbody.angular_velocity += torque_self / self.parent.rigidbody.mass
#             other.parent.rigidbody.angular_velocity -= torque_other / other.parent.rigidbody.mass
#
#     def check_collision(self, other):
#         axes = self.get_axes() + other.get_axes()
#         minimum_overlap = float('inf')
#         smallest_axis = None
#
#         for axis in axes:
#             projection1 = self.project_on_axis(axis)
#             projection2 = other.project_on_axis(axis)
#             overlap = min(projection2[1], projection1[1]) - max(projection2[0], projection1[0])
#
#             if overlap < 0:
#                 return False, None
#
#             if overlap < minimum_overlap:
#                 minimum_overlap = overlap
#                 smallest_axis = axis * (1 if np.dot(smallest_axis, other.center - self.center) < 0 else -1)
#
#         mtv = smallest_axis * minimum_overlap
#         return True, mtv
#
#     def get_axes(self):
#         axes = []
#         num_vertices = len(self.vertices)
#         for i in range(num_vertices):
#             edge = self.vertices[(i + 1) % num_vertices] - self.vertices[i]
#             normal = np.array([-edge[1], edge[0]])
#             normal /= np.linalg.norm(normal)
#             axes.append(normal)
#         return axes
#
#     def project_on_axis(self, axis):
#         projections = np.dot(self.vertices, axis)
#         return np.min(projections), np.max(projections)


class PolyCollider(Component):
    def __init__(self, parent, vertices):
        super().__init__(parent)
        self.vertices = np.array(vertices)  # Ensure vertices are a numpy array
        self.center = self.calculate_centroid()

    def calculate_centroid(self):
        if len(self.vertices) > 0:
            return np.mean(self.vertices, axis=0)
        return np.array([0, 0])

    def handle_collision(self, other, mtv):
        if not self.parent.rigidbody:
            self.parent.transform.position += mtv
        else:
            self.parent.rigidbody.apply_collision_response(mtv)

    def move_out_of_collision(self, other):
        collision, mtv = self.check_collision(other)
        if collision:
            # Calculate the point of impact for simplicity we use centroid average
            point_of_impact = (self.center + other.center) / 2

            # Apply MTV to resolve collision
            direction_to_other = other.center - self.center
            direction_norm = np.linalg.norm(direction_to_other)

            if direction_norm == 0:
                return  # Avoid division by zero if centers are exactly the same

            mtv_direction = np.dot(mtv, direction_to_other)
            if mtv_direction < 0:
                mtv = -mtv  # Ensure MTV pushes this object away from the other object

            # Assume both objects are dynamic for simplicity, adjust as needed for your game's logic
            self.parent.transform.position -= mtv * 0.5
            other.parent.transform.position += mtv * 0.5

            # Calculate torque due to collision
            lever_arm_self = point_of_impact - self.center
            lever_arm_other = point_of_impact - other.center
            torque_self = np.cross(lever_arm_self, -mtv)  # Negative because MTV pushes out
            torque_other = np.cross(lever_arm_other, mtv)

            # self.parent.rigidbody.apply_torque(torque_self)
            # other.parent.rigidbody.apply_torque(torque_other)

            # op = self.parent.rigidbody.velocity
            # self.parent.rigidbody.velocity = other.parent.rigidbody.velocity
            # other.parent.rigidbody.velocity = op

    def check_collision(self, other):
        axes = self.get_axes() + other.get_axes()
        minimum_overlap = float('inf')
        smallest_axis = None
        for axis in axes:
            projection1 = self.project_on_axis(axis)
            projection2 = other.project_on_axis(axis)
            overlap = min(projection2[1], projection1[1]) - max(projection2[0], projection1[0])
            if overlap < 0:
                return False, None
            if overlap < minimum_overlap:
                minimum_overlap = overlap
                smallest_axis = axis
        if np.dot(smallest_axis, other.center - self.center) < 0:
            smallest_axis = -smallest_axis
        mtv = smallest_axis * minimum_overlap
        return True, mtv

    def get_axes(self):
        axes = []
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            edge = self.vertices[(i + 1) % num_vertices] - self.vertices[i]
            normal = np.array([-edge[1], edge[0]])
            normal /= np.linalg.norm(normal)
            axes.append(normal)
        return axes

    def project_on_axis(self, axis):
        projections = np.dot(self.vertices, axis)
        return np.min(projections), np.max(projections)

    def on_update(self, dt):
        super().on_update(dt)
        # Update the centroid in case of transformations
        self.center = self.calculate_centroid()

        # Implement any additional periodic update logic here
