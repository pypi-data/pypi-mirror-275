from src.grid_engine_Nitebound.grid_engine import GameObject
from src.grid_engine_Nitebound.grid_engine.features.components import Mesh2D, RigidBody2D
from src.grid_engine_Nitebound.grid_engine.features.components.colliders.poly_collider import PolyCollider
import numpy as np
from numpy import cos, sin, radians,sqrt
from pygame import Vector2, draw as pg_draw

class Actor(GameObject):
    def __init__(self, name="Actor"):
        super().__init__(name)
        self.speed = 9
        self.turn_speed = 100
        self.rigidbody = RigidBody2D(self, .45)
        self.rigidbody.use_gravity = False
        self.rigidbody.drag = 5
        self.rigidbody.angular_drag = 21
        self.components.append(self.rigidbody)

        self.mesh = Mesh2D(self)
        self.poly_collider = PolyCollider(self, self.mesh.vertices)
        self.components.append(self.mesh)
        self.components.append(self.poly_collider)

    def on_key_pressed(self, keystates):
        super().on_key_pressed(keystates)
        for component in self.components:
            component.on_key_pressed(keystates)

    def on_update(self, dt):
        super().on_update(dt)
        self.mesh.update_vertices(dt)  # Update Mesh2D vertices
        self.poly_collider.vertices = np.array([Vector2(v[0], v[1]) for v in self.mesh.world_vertices])

    def on_draw(self, dest, dt):
        super().on_draw(dest, dt)
        p2x = self.transform.position.x + 12 * cos(radians(self.transform.rotation))
        p2y = self.transform.position.y + 12 * sin(radians(self.transform.rotation))

        px = self.transform.position.x + 5 * cos(radians(self.transform.rotation))
        py = self.transform.position.y + 5 * sin(radians(self.transform.rotation))

        pg_draw.circle(dest, (255, 255, 255), self.transform.position, 3, 1)
        pg_draw.line(dest, (255, 255, 255), (px, py), (p2x, p2y))
