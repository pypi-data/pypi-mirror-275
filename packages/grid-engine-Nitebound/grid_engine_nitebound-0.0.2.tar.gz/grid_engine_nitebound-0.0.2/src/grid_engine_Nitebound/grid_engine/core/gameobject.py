from src.grid_engine_Nitebound.grid_engine.features.components.transform import Transform
import pygame.draw as pg_draw


class GameObject:
    def __init__(self, name="GameObject", parent=None):
        self.name = name
        self.transform = Transform(self)
        self.components = [self.transform]
        self.parent = parent
        self.surface = None
        self.children = []

    def add_component(self, component):
        component.parent = self
        self.components.append(component)

    def get_component(self, component_type):
        for i, component in enumerate(self.components):
            type_str = str(type(component))
            type_str_parts = str(type(component)).split(".")
            c_type = type_str_parts[-1].replace('\'>', '')
            if component_type.lower() == str(c_type).lower():
                return self.components[i]
        return None

    def on_event(self, event):
        for component in self.components:
            component.on_event(event)

    def on_key_pressed(self, keystates):
        pass

    def on_key_released(self, key_states):
        pass

    def on_mouse_button_pressed(self, mouse_buttons):
        pass

    def on_mouse_button_released(self, mouse_buttons):
        pass

    def on_update(self, dt):
        for component in self.components:
            component.on_update(dt)

    def on_late_update(self):
        for component in self.components:
            component.on_late_update()

    def on_draw(self, dest, dt):
        for component in self.components:
            component.on_draw(dest, dt)
