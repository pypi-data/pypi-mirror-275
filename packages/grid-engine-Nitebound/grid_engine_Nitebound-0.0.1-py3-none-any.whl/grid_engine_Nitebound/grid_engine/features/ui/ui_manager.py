from pygame import Rect, Vector2, math
import pygame as pg
from src.grid_engine_Nitebound.grid_engine.core import Canvas
from src.grid_engine_Nitebound.grid_engine.features.ui.ui_panel import UIPanel
from src.grid_engine_Nitebound.grid_engine.features.ui.ui_text import UIText
from src.grid_engine_Nitebound.grid_engine.features.ui.ui_element import UIElement
from src.grid_engine_Nitebound.grid_engine.features.ui.ui_style import UIStyle


class UIManager:
    def __init__(self, canvas):
        self.elements = []  # Changed from dict to list
        self.focused_element = None
        self.canvas = canvas
        self.current_cursor = pg.cursors.arrow

    def add_element(self, element):
        self.elements.append(element)

    def bring_to_front(self, element):
        if element in self.elements:
            self.elements.remove(element)
            self.elements.append(element)

    def on_event(self, event):
        mouse_pos = pg.mouse.get_pos()

        for element in reversed(self.elements):
            element.on_event(event)

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == pg.BUTTON_LEFT:
                for element in reversed(self.elements):  # Check in reverse order
                    element.is_dragging = False
                    element.reset_properties()
                    break  # Stop at the first element clicked

        if event.type == pg.MOUSEBUTTONDOWN:
            for element in reversed(self.elements):
                if element.local_bounds.collidepoint(mouse_pos):
                    self.bring_to_front(element)
                    break

    def on_update(self):
        mouse_pos = pg.mouse.get_pos()
        for element in reversed(self.elements):  # Update top-most element last
            element.on_update()
            print(element.name, element.global_bounds)


    def on_late_update(self):
        for element in reversed(self.elements):
            element.on_late_update()

    def on_draw(self, dest, offset=(0, 0)):
        for element in self.elements:  # Draw from bottom to top
            element.on_draw(dest, offset)
