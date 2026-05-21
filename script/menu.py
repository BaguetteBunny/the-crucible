import pygame as pg
import constants as C

from data.configs import MenuLabel

class Menu():
    def __init__(self) -> None:
        self.image = None

    def draw(self, screen: pg.Surface, pos: pg.Vector2):
        screen.blit(pos)


class Sidebar(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.image = C.MENUS[MenuLabel.SIDEBAR]

    def draw(self, screen: pg.Surface):
        super().draw(screen, pg.Vector2(0, 0))
        

SIDEBAR = Sidebar()