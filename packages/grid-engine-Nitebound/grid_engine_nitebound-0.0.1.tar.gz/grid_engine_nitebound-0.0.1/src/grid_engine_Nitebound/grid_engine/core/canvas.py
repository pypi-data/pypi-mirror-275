import pygame as pg
from pygame import Vector2, Rect, draw as pg_draw


class Canvas:
    def __init__(self, size, title="Canvas", flags=0):
        self.surface = pg.display.set_mode((size[0], size[1]), flags)
        self.width = size[0]
        self.height = size[1]
        self.title = title
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.frame_rate = 120
        self.running = True
        self.dt = 1 / self.frame_rate
        self.current_fps = 0
        self.quick_exit = False
        self.show_fps = False

    def clear(self, color=(0, 0, 0)):
        self.surface.fill(color)

    def get_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.quick_exit:
                        self.running = False

        return events

    def get_keys_pressed(self):
        keys_pressed = pg.key.get_pressed()
        return keys_pressed

    def get_mouse_position(self):
        return Vector2(pg.mouse.get_pos())

    def get_mouse_buttons(self):
        return pg.mouse.get_pressed()

    def on_event(self, event):
        if event.type == pg.QUIT:
            self.running = False

    def on_update(self):
        pass

    def on_late_update(self):
        pg.display.update()
        self.dt = self.clock.tick(self.frame_rate)/1000
        self.current_fps = self.clock.get_fps()

        if self.show_fps:
            pg.display.set_caption(f'{self.title} (FPS: {int(self.current_fps)})')