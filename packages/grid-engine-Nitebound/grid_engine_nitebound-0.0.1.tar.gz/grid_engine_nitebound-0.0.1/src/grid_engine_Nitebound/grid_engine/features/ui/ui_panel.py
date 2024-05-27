from pygame import Surface, Rect, draw as pg_draw, key as pg_key, mouse as pg_mouse, Vector2, cursors as pg_cursors
from pygame import font as pg_font, sysfont as pg_sysfont
from pygame.locals import *
from .ui_element import UIElement
from .ui_view import UIView
from src.grid_engine_Nitebound.grid_engine.core.toolkit import pad_rect


class UIPanel(UIElement):
    cursor_horizontal = pg_cursors.Cursor(SYSTEM_CURSOR_SIZEWE)
    cursor_vertical = pg_cursors.Cursor(SYSTEM_CURSOR_SIZENS)
    cursor_diag1 = pg_cursors.Cursor(SYSTEM_CURSOR_SIZENWSE)
    cursor_diag2 = pg_cursors.Cursor(SYSTEM_CURSOR_SIZENESW)

    def __init__(self, name, manager, parent=None, position=(50, 50), width=300, height=300):
        super().__init__(name, parent, (position[0], position[1], width, height))
        # self.style.background_color = (255, 255, 0)
        # self.style.foreground_color = (255, 255, 0)
        # self.style.text_color = (255, 0, 0)
        # self.style.fill_color = (0, 255, 0)
        # self.surface = Surface((self.rect.w, self.rect.h), SRCALPHA)
        self.min_size = (81, 42)
        self.max_size = None
        self.border_width = 1
        self.border_radius = 10
        self.padding = 3
        self.handle_rect = Rect(position[0], position[1], self.local_bounds.w, 18)
        self.title_font = pg_font.SysFont("Courier", int(self.handle_rect.h * .8), True)
        self._text_surface = self.title_font.render(name, True, self.style.text_color)
        #self.on_render()

        self.is_dragging = False
        self._is_resizing_top = False
        self._is_resizing_right = False
        self._is_resizing_bottom = False
        self._is_resizing_left = False
        self._dragging_offset = (0, 0)
        self.draggable = True
        self.resizable = True
        self.content_rect = self.ui_surface.surface.get_rect()
        self.current_cursor = pg_cursors.arrow
        self._ui_manager = manager
        self.scroll_velocity = 40
        self.ui_view = UIView(self.name + " View")
        # Make the drag handles turn the cursor into a resize cursor.
        self.children = []

    def add_element(self, element):
        element.parent = self
        self.children.append(element)

    def update_cursor(self, mouse_pos):
        hovered_edges = []
        if self.rect.collidepoint(mouse_pos):
            # Top Edge Resize Check
            if mouse_pos[1] < self.rect.top + self.border_width + self.padding:
                hovered_edges.append("Top")

            # Right Edge Resize Check
            if mouse_pos[0] > self.rect.right - self.border_width - self.padding * 2:
                hovered_edges.append("Right")

            # Bottom Edge Resize Check
            if mouse_pos[1] > self.rect.bottom - self.border_width - self.padding * 2:
                hovered_edges.append("Bottom")

            # Left Edge Resize Check
            if mouse_pos[0] < self.rect.left + self.border_width + self.padding:
                hovered_edges.append("Left")

        if self.resizable:
            if "Top" in hovered_edges:
                self._ui_manager.current_cursor = self.cursor_vertical

            if "Bottom" in hovered_edges:
                self._ui_manager.current_cursor = self.cursor_vertical

            if "Left" in hovered_edges:
                self._ui_manager.current_cursor = self.cursor_horizontal

            if "Right" in hovered_edges:
                self._ui_manager.current_cursor = self.cursor_horizontal

            if "Top" in hovered_edges and "Left" in hovered_edges:
                self._ui_manager.current_cursor = self.cursor_diag1

            if "Top" in hovered_edges and "Right" in hovered_edges:
                self._ui_manager.current_cursor = self.cursor_diag2

            if "Bottom" in hovered_edges and "Left" in hovered_edges:
                self._ui_manager.current_cursor = self.cursor_diag2

            if "Bottom" in hovered_edges and "Right" in hovered_edges:
                self._ui_manager.current_cursor = self.cursor_diag1

        return hovered_edges

    def update_content_surface(self):
        self.ui_view.resize(self.handle_rect.w - self.border_width*2 - self.padding*2, self.local_bounds.h - self.handle_rect.h - self.border_width*2 - self.padding*2)
        self.ui_view.local_bounds.x = self.padding + self.border_width
        self.ui_view.local_bounds.y = self.handle_rect.h + self.padding + self.border_width

        #self.ui_view.content_surface = Surface(self.content_rect.size, SRCALPHA)

    def get_state_properties(self):
        return self._is_resizing_left or self._is_resizing_top or self._is_resizing_right or self._is_resizing_bottom

    def reset_properties(self):
        self.is_dragging = False
        self._is_resizing_top = False
        self._is_resizing_right = False
        self._is_resizing_bottom = False
        self._is_resizing_left = False
        self._dragging_offset = (0, 0)

    def resize(self, width, height):
        if width < self.min_size[0]: width = self.min_size[0]
        if height < self.min_size[1]: width = self.min_size[1]
        self.ui_surface.resize(width, height)
        self.local_bounds.width = width
        self.local_bounds.height = height
        self.handle_rect.w = self.local_bounds.w
        self.on_render()

    def update_layout(self):
        pass

    def on_render(self):
        self.ui_surface.surface.fill((0, 0, 0, 0))

        # Window Background Rect
        pg_draw.rect(self.ui_surface.surface, self.style.fill_color, (0, 0, self.local_bounds.w, self.local_bounds.h),
                     border_radius=self.border_radius)
        self._text_surface = self.title_font.render(self.name, True, self.style.text_color)


        # Content Rect
        pg_draw.rect(self.ui_surface.surface, self.style.background_color, (
            self.border_width + self.padding, self.border_width + self.handle_rect.h + self.padding,
            self.local_bounds.w - self.border_width * 2 - self.padding * 2,
            self.local_bounds.h - self.border_width * 2 - self.handle_rect.h - self.padding * 2), 1,
                     border_radius=self.border_radius)

        # Content Border
        pg_draw.rect(self.ui_surface.surface, self.style.frame_color, (
            self.border_width + self.padding, self.border_width + self.handle_rect.h + self.padding,
            self.local_bounds.w - self.border_width * 2 - self.padding * 2,
            self.local_bounds.h - self.border_width * 2 - self.handle_rect.h - self.padding * 2), 1,
                     border_radius=self.border_radius)

        pg_draw.rect(self.ui_surface.surface, (255, 255, 255), (1, 1, self.local_bounds.w-2, self.local_bounds.h-2),
                     self.border_width,
                     border_radius=self.border_radius)

        # Border Rect
        pg_draw.rect(self.ui_surface.surface, self.style.border_color, (0, 0, self.local_bounds.w, self.local_bounds.h),
                     self.border_width,
                     border_radius=self.border_radius)

        self.update_content_surface()

        for child in self.children:
            child.on_draw(self.ui_view.content_surface, (0, 0))

        self.ui_view.on_draw(self.ui_surface.surface, (self.padding + self.border_width, self.handle_rect.h + self.padding + self.border_width))
        self.ui_surface.blit(self._text_surface, (16, 4))

    def on_event(self, event):
        super().on_event(event)
        for child in self.children:
            child.on_event(event)

        if event.type == MOUSEBUTTONDOWN:
            if event.button == BUTTON_LEFT:
                if self.local_bounds.collidepoint(event.pos):
                    if self.draggable:
                        crect = Rect(self.handle_rect.x, self.handle_rect.y, self.handle_rect.w,
                                     self.handle_rect.h + self.border_width + self.padding)

                        if crect.collidepoint(event.pos):
                            self.is_dragging = True
                            self._dragging_offset = (Vector2(event.pos) - self.local_bounds.topleft)

                    if self.resizable:
                        # Top Edge Resize Check
                        if event.pos[1] < self.local_bounds.top + self.border_width + self.padding:
                            self._is_resizing_top = True

                        # Right Edge Resize Check
                        if event.pos[0] > self.local_bounds.right - self.border_width - self.padding * 2:
                            self._is_resizing_right = True

                        # Bottom Edge Resize Check
                        if event.pos[1] > self.local_bounds.bottom - self.border_width - self.padding * 2:
                            self._is_resizing_bottom = True

                        # Left Edge Resize Check
                        if event.pos[0] < self.local_bounds.left + self.border_width + self.padding:
                            self._is_resizing_left = True

        if event.type == MOUSEBUTTONUP:
            if event.button == BUTTON_LEFT:
                self.reset_properties()

        if event.type == MOUSEWHEEL:
            self.ui_view.local_bounds.x = self.local_bounds.x
            self.ui_view.local_bounds.y = self.local_bounds.y

            # if pad_rect(self.rect, 10).collidepoint((event.x, event.y)):#.collidepoint(pg_mouse.get_pos()):
            if self.local_bounds.collidepoint(pg_mouse.get_pos()):
                if not self.handle_rect.collidepoint(pg_mouse.get_pos()):
                    self.ui_view.content_offset[1] += event.y * self.scroll_velocity

        self.ui_view.on_event(event)

    def on_update(self):
        super().on_update()
        mouse_pos = pg_mouse.get_pos()
        self.ui_view.on_update()

        for child in self.children:
            child.on_update()

        if self._is_resizing_top:
            h = self.local_bounds.bottom - mouse_pos[1]
            if h != self.local_bounds.h:
                if h > self.min_size[1]:
                    self.resize(self.local_bounds.w, h)
                    self.local_bounds.top = mouse_pos[1]

        if self._is_resizing_right:
            w = mouse_pos[0] - self.local_bounds.left + self.border_width + self.padding
            if w != self.local_bounds.w:
                self.resize(w, self.local_bounds.h)

        if self._is_resizing_bottom:
            h = mouse_pos[1] - self.local_bounds.top + self.border_width + self.padding
            if h != self.local_bounds.h:
                if h > self.min_size[1]:
                    self.resize(self.local_bounds.w, h)

        if self._is_resizing_left:
            w = self.local_bounds.right - mouse_pos[0]
            if w != self.local_bounds.w:
                if w > self.min_size[0]:
                    self.resize(w, self.local_bounds.h)
                    self.local_bounds.left = mouse_pos[0]

        if self.is_dragging and self._is_resizing_top is False and self._is_resizing_right is False:
            if self._is_resizing_bottom is False:
                if self._is_resizing_left is False:
                    self.local_bounds.x = mouse_pos[0] - self._dragging_offset[0]
                    self.local_bounds.y = mouse_pos[1] - self._dragging_offset[1]

        self.handle_rect.x = self.local_bounds.x
        self.handle_rect.y = self.local_bounds.y

    def on_late_update(self):
        super().on_late_update()

        for child in self.children:
            child.on_late_update()

    def on_draw(self, dest, offset=(0, 0)):
        self.on_render()

        if self.ui_surface:
            self.ui_surface.on_draw(dest, Vector2(self.local_bounds.topleft) + offset)
        pg_draw.circle(dest, (255, 0, 0), self.local_bounds.topleft, 4)


