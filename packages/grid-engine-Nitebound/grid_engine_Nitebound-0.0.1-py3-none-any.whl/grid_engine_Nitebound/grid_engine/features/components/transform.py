from src.grid_engine_Nitebound.grid_engine.core.component import Component
from pygame import Vector2, draw as pg_draw
from math import cos, sin, radians


class Transform(Component):
    def __init__(self, parent, position=(0, 0), rotation=0, scale=1):
        super().__init__(parent)
        self.position = Vector2(position)
        self.rotation = rotation
        self.scale = scale

    def translate(self, offset):
        self.position += offset

    def rotate(self, angle):
        self.rotation += angle

    def scale(self, factor):
        self.scale *= factor

    def on_event(self, event):
        super().on_event(event)

    def on_update(self, dt):
        self.rotation = self.rotation % 360
        super().on_update(dt)

    def on_late_update(self):
        super().on_late_update()

    def on_draw(self, dest, dt):
        super().on_draw(dest, dt)

