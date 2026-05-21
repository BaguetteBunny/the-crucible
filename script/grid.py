import constants as C
import numpy as np
import pygame as pg

class Grid():
    def __init__(self) -> None:
        self.cols = 4
        self.rows = 4

        self.cell_size: float = 128 * C.SCREEN_SCALE.x
        self.border_size: int = int(2 * C.SCREEN_SCALE.x)

        self.total_size = pg.Vector2(pg.Vector2(self.cols, self.rows) * self.cell_size)
        self.origin = pg.Vector2(C.MIDPOINT - (pg.Vector2(self.cols, self.rows) / 2) * self.cell_size)

        self.matrix = np.zeros((self.rows, self.cols), dtype=np.int8)
        
GRID = Grid()