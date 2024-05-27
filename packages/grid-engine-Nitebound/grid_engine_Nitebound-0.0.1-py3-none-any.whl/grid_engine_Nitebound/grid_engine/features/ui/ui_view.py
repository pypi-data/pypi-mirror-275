from pygame.locals import *
from pygame import Surface, Vector2
from .ui_element import UIElement


class UIView(UIElement):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.content_view_surface = Surface(self.local_bounds.size, SRCALPHA)
        self.content_surface = Surface(self.local_bounds.size, SRCALPHA)
        self.content_surface.fill((255, 255, 255, 255))
        self.content_offset = [0, 0]
        self.children = []

    def resize(self, w, h):
        self.local_bounds.w = w
        self.local_bounds.h = h
        self.content_view_surface = Surface((w, h), SRCALPHA)
        self.content_surface = Surface((w, h), SRCALPHA)
        self.content_surface.fill((255, 255, 255, 255))

    def on_event(self, event):
        pass

    def on_update(self):
        super().on_update()
        if self.content_offset[1] > 0:
            self.content_offset[1] = 0

    def on_draw(self, dest, offset=(0, 0)):
        self.content_view_surface.fill((255, 255, 255))
        for element in self.children:
            element.on_draw(self.content_surface, offset)

        self.content_view_surface.blit(self.content_surface, (0, self.content_offset[1]))
        dest.blit(self.content_view_surface, Vector2(offset))
        #pg_draw.rect(dest, (0, 0, 0), pad_rect(self.rect, (-5, -5)), 1)

    def on_late_update(self):
        pass
