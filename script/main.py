import pygame as pg
import sys

pg.init()
pg.display.set_caption("Grid Game")

import constants as C

from player import PLAYER
from grid import GRID
from menu import SETTINGS, SIDEBAR
from text import Text
from data.configs import Colors, FontSize

def quit():
    pg.quit()
    sys.exit()

def event_handler(event: pg.event.EventType):
    # Quit
    if event.type == pg.QUIT:
        quit()
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            PLAYER.pause = not PLAYER.pause

    # Drag Across Screen
    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and not PLAYER.pause:
        PLAYER.dragging = True
        PLAYER.drag_start_mouse  = PLAYER.pos
        PLAYER.drag_start_camera = pg.Vector2(PLAYER.camera)
        PLAYER.update_cursor()

    if event.type == pg.MOUSEBUTTONUP and event.button == 1:
        PLAYER.dragging = False
        PLAYER.update_cursor()

    if event.type == pg.MOUSEMOTION and PLAYER.dragging:
        PLAYER.camera = PLAYER.drag_start_camera + (PLAYER.pos - PLAYER.drag_start_mouse)
        PLAYER.camera.x = max(-C.MIDPOINT.x, min(C.MIDPOINT.x, PLAYER.camera.x))
        PLAYER.camera.y = max(-C.MIDPOINT.y, min(C.MIDPOINT.y, PLAYER.camera.y))

def draw_grid(surface: pg.Surface = C.SCREEN) -> None:
    for row in range(GRID.rows):
        for col in range(GRID.cols):
            loc = pg.Vector2(col, row) * GRID.cell_size + PLAYER.camera + GRID.origin

            border_rect = pg.Rect(loc, (GRID.cell_size, GRID.cell_size))
            pg.draw.rect(surface, Colors.GRAY, border_rect, GRID.border_size)

            inner_rect = border_rect.inflate(-GRID.border_size * 2, -GRID.border_size * 2)
            pg.draw.rect(surface, Colors.BLACK, inner_rect)

def main() -> None:
    while True:
        for event in pg.event.get(): event_handler(event)
 
        pg.display.flip()
        C.CLOCK.tick(C.FPS)
        
        # Draw
        C.SCREEN.fill(Colors.BG_MAIN)
        draw_grid()

        if PLAYER.pause:
            t = Text(text= "PAUSED", color = Colors.WHITE, is_italic= True, font= C.FONTS[FontSize.XL6])
            t.draw(C.SCREEN, (0,0))

            SETTINGS.draw()




        # Update
        PLAYER.update_pos()
 
if __name__ == "__main__":
    main()