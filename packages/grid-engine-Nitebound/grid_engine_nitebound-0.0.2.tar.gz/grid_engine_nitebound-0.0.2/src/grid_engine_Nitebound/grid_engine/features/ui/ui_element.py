from pygame import Vector2, Rect, draw as pg_draw, event as pg_event
from src.grid_engine_Nitebound.grid_engine.features.ui.ui_surface import UISurface
from src.grid_engine_Nitebound.grid_engine.features.ui.ui_style import UIStyle


class UIElement:
    def __init__(self, name="UIElement", parent=None, rect=(0, 0, 0, 0), ui_surface=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.local_bounds = Rect(rect)
        self._global_bounds = Rect(rect)
        # self.rect = Rect(rect)
        self.ui_surface = UISurface(self.local_bounds.w, self.local_bounds.h, self) if ui_surface is None else ui_surface
        self.style = UIStyle()


    @property
    def global_bounds(self):
        if  self.parent:
            gbx = self.parent.global_bounds[0] + self.local_bounds[0]
            gby = self.parent.global_bounds[1] + self.local_bounds[1]
            gbw = self.local_bounds[2]
            gbh = self.local_bounds[3]

            self._global_bounds = Rect(gbx, gby, gbw, gbh)
        else:
            self._global_bounds = self.local_bounds

        return self._global_bounds

    def on_event(self, event):
        if self.ui_surface:
            self.ui_surface.on_event(event)

    def on_update(self):
        if self.ui_surface:
            self.ui_surface.on_update()

    def on_late_update(self):
        if self.ui_surface:
            self.ui_surface.on_late_update()

    def on_draw(self, dest, offset=(0, 0)):
        pg_draw.rect(dest, (255, 0, 0), (0, 0, 100, 100), 2)