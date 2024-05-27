from .camera import Camera
from src.grid_engine_Nitebound.grid_engine.features.components.colliders.poly_collider import PolyCollider


class Scene:
    def __init__(self, name):
        self.name = name
        self.game_objects = []
        self.camera = Camera()

    def check_collisions(self):
        # Check for collisions between all pairs of game objects
        for i in range(len(self.game_objects)):
            for j in range(i + 1, len(self.game_objects)):
                obj1 = self.game_objects[i]
                obj2 = self.game_objects[j]
                self.check_collision_between(obj1, obj2)

    def check_collision_between(self, obj1, obj2):
        collider1 = obj1.get_component("PolyCollider")
        collider2 = obj2.get_component("PolyCollider")

        if collider1 and collider2:
            if collider1.check_collision(collider2):
                collider1.move_out_of_collision(collider2)
                collider2.move_out_of_collision(collider1)

    def on_event(self, event):
        for game_object in self.game_objects:
            game_object.on_event(event)

    def on_key_pressed(self, keystates):
        for game_object in self.game_objects:
            game_object.on_key_pressed(keystates)

    def on_mouse_button_pressed(self, mouse_buttons):
        for game_objects in self.game_objects:
            game_objects.on_mouse_button_pressed(mouse_buttons)

    def on_update(self, dt):
        # First, update all objects which includes their meshes and colliders
        for obj in self.game_objects:
            obj.on_update(dt)

        # Then, check for collisions
        self.check_collisions()

    def on_late_update(self):
        for game_object in self.game_objects:
            game_object.on_late_update()

    def on_draw(self, dest, dt):
        for game_object in self.game_objects:
            game_object.on_draw(dest, dt)

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)
