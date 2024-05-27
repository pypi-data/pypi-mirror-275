from pygame import Vector2, Rect, Surface, SRCALPHA, draw as pg_draw


class UISurface:
    def __init__(self, width, height, parent=None):
        self._rect = Rect(0, 0, width, height)
        self.surface = Surface(self._rect.size, SRCALPHA)
        self.element = parent

    def resize(self, width, height):
        self._rect.w = width
        self._rect.h = height
        self.surface = Surface(self._rect.size, SRCALPHA)

    def fill(self, color=(100, 100, 100), rect=None):
        if rect:
            self.surface.fill(color, rect)
        else:
            self.surface.fill(color)

    def blit(self, surface, offset=(0, 0)):
        self.surface.blit(surface, offset)

    def on_render(self):
        pass

    def on_init(self):
        pass

    def on_event(self, event):
        pass

    def on_update(self):
        pass

    def on_late_update(self):
        pass

    def on_draw(self, dest, offset=(0, 0)):
        dest.blit(self.surface, self._rect.topleft + offset)

