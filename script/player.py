import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        self.camera = pg.Vector2(0, 0)
        self.dragging = False
        self.drag_start_mouse = pg.Vector2(0, 0)
        self.drag_start_camera = pg.Vector2(0, 0)
        self.pos = pg.Vector2(0, 0)

        self.left_clicked, self.right_clicked = False, False

        self.name = ""
        self.coins = 0

        self.in_settings = False

    def update_cursor(self, cursor: int = None) -> None:
        if self.dragging:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        elif cursor == None: 
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        else:
            pg.mouse.set_cursor(cursor)

    def update_pos(self): 
        self.pos = pg.Vector2(pg.mouse.get_pos())

    def update_clicks(self):
        self.left_clicked = pg.mouse.get_pressed(num_buttons = 3)[0]
        self.right_clicked = pg.mouse.get_pressed(num_buttons = 3)[2]

    def draw_stats(self): ... 

PLAYER = Player()