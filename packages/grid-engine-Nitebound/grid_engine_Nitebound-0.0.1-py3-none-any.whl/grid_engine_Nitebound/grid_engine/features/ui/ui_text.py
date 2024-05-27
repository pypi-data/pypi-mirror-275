from .ui_element import UIElement
import pygame as pg


class UIText(UIElement):
    pg.font.init()
    DEFAULT_FONT = pg.font.SysFont("Courier", 20, True)

    def __init__(self, text):
        super().__init__()
        self._text = text
        self.style.foreground_color = pg.Color(2, 125, 255)
        self.style.background_color = pg.Color(255, 0, 255)
        self.text_surface = self.DEFAULT_FONT.render(self._text, True, self.style.text_color)
        self.ui_surface.resize(self.text_surface.get_width(), self.text_surface.get_height())
        self.ui_surface.surface.blit(self.text_surface, (0, 0))
        #self.ui_surface.surface = self.text_surface
        #self.on_render()

    @property
    def text(self):
        self.text_surface = self.DEFAULT_FONT.render(self._text, True, self.style.text_color)
        self.ui_surface.resize(self.text_surface.get_width(), self.text_surface.get_height())
        self.ui_surface.surface.fill((255, 255, 255, 0))
        self.ui_surface.blit(self.text_surface, (0, 0))
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.text_surface = self.DEFAULT_FONT.render(self._text, True, self.style.text_color)
        self.ui_surface.resize(self.text_surface.get_width(), self.text_surface.get_height())
        self.ui_surface.surface.fill((255, 255, 255, 0))
        self.ui_surface.blit(self.text_surface, (0, 0))

    def on_render(self):
        self.ui_surface.surface.blit(self.text_surface, (0, 0))

    def on_draw(self, dest, offset=(0, 0)):
        #self.ui_surface.surface.blit(self.text_surface, (0, 0))
        dest.blit(self.ui_surface.surface, self.local_bounds)
