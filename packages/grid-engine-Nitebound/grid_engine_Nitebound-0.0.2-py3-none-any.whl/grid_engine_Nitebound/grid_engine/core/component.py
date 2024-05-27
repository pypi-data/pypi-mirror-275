

class Component:
    def __init__(self, parent):
        self.parent = parent

    def on_event(self, event):
        pass

    def on_key_pressed(self, keystates):
        pass

    def on_key_released(self, key_states):
        pass

    def on_update(self, dt):
        pass

    def on_late_update(self):
        pass

    def on_draw(self, dest, dt):
        pass
