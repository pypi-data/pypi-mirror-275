from src.grid_engine_Nitebound.grid_engine.core.component import Component
from src.grid_engine_Nitebound.grid_engine.core.toolkit import translate, rotate, scale
from pygame import Vector2, draw as pg_draw
import numpy as np
from numpy import degrees, cos, sin, radians


class Mesh2D(Component):
    def __init__(self, parent, vertices=None, radius=50, num_sides=6):
        super().__init__(parent)
        self.center = np.array([0, 0], dtype=float)  # Center of the mesh
        self.radius = radius
        self.num_sides = num_sides
        if vertices is None:
            self.vertices = self.generate_polygon(radius, num_sides)
        else:
            self.vertices = np.array(vertices, dtype=float)
        self.world_vertices = []

    def generate_polygon(self, radius, num_sides):
        """ Generates a uniform polygon vertices centered at the origin. """
        return np.array([
            [cos(2 * np.pi * i / num_sides) * radius, sin(2 * np.pi * i / num_sides) * radius]
            for i in range(num_sides)
        ])

    def update_vertices(self, dt):
        """ Updates the vertices based on the GameObject's transform. """
        angle = radians(self.parent.transform.rotation)
        rotation_matrix = np.array([
            [cos(angle), -sin(angle)],
            [sin(angle), cos(angle)]
        ])

        # Rotate and translate vertices
        rotated_vertices = np.dot(self.vertices, rotation_matrix.T)
        self.world_vertices = rotated_vertices + self.parent.transform.position

    def on_draw(self, dest, dt):
        self.update_vertices(dt)
        # Convert vertices for drawing
        polygon_vertices = [(int(v[0]), int(v[1])) for v in self.world_vertices]
        pg_draw.polygon(dest, (255, 0, 0), polygon_vertices, 1)

    def set_vertices(self, vertices):
        self.vertices = vertices