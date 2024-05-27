from .ui_element import UIElement
from .ui_text import UIText
import pygame as pg
from pygame.locals import *


class UIButton(UIElement):
    def __init__(self, text, rect=(0, 0, 10, 10), parent=None):
        super().__init__("Button", parent)
        self.label = UIText(text)
        self._text = text
        self.size = self.label.text_surface.get_size()
        self.local_bounds.w = self.size[0]
        self.local_bounds.h = self.size[1]
        self._hovered = False
        self._left_clicked = False
        self._right_clicked = False

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.label.text = self._text

    def reset_properties(self):
        self._left_clicked = False
        self._right_clicked = False
        self._hovered = False

    def on_update(self):
        mouse_pos = pg.Vector2(pg.mouse.get_pos())

    def on_late_update(self):
        pass

    def on_event(self, event):
        mouse_pos = pg.mouse.get_pos()
        # Need to get the global position of the button to check if the mouse
        # is over it correctly
        if event.type == MOUSEBUTTONDOWN:
            if event.button == BUTTON_LEFT:
                if self.local_bounds.collidepoint(mouse_pos):
                    print("Closer?!")

    def on_draw(self, dest, offset=(0, 0)):
        self.label.on_draw(dest, self.local_bounds.topleft + offset)
        pg.draw.rect(dest, (255, 2, 100), self.local_bounds, 1)
        pg.draw.circle(dest, (255, 0, 0), self.local_bounds.topleft, 4)
