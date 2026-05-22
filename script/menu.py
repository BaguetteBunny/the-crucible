import pygame as pg
import constants as C

from data.configs import MenuLabel

class Menu():
    def __init__(self, pos: pg.Vector2) -> None:
        self.image: pg.SurfaceType = None
        self.pos = pos

    def draw(self, screen: pg.Surface = C.SCREEN):
        screen.blit(self.image, self.pos)

class Sidebar(Menu):
    def __init__(self, pos: pg.Vector2) -> None:
        super().__init__(pos)
        self.image = C.MENUS[MenuLabel.SIDEBAR]

class Settings(Menu):
    def __init__(self, pos: pg.Vector2) -> None:
        super().__init__(pos)
        self.image = C.MENUS[MenuLabel.SETTINGS]

SIDEBAR = Sidebar(pg.Vector2(0, 0))

SETTINGS = Settings(C.MIDPOINT - pg.Vector2(352, 320).elementwise() * C.SCREEN_SCALE)