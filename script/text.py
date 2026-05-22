import pygame as pg
import colorsys

import constants as C
from player import PLAYER
from data.configs import RainbowConfig, FontSize, Colors

class Text:
    def __init__(self,
                 text: str = 'Empty Text Layer',
                 font: pg.font.Font = C.FONTS[FontSize.M],
                 color: Colors | RainbowConfig = Colors.WHITE,
                 pos: pg.Vector2 = pg.Vector2(0.0, 0.0),
                 opacity: int = 255,
                 is_centered: bool = False,
                 is_bold: bool = False,
                 is_italic: bool = False,
                 is_underline: bool = False,
                 is_number_formatting: bool = False) -> None:

        self.text = text
        self.font = font
        self.color = color
        self.pos = pos
        self.opacity = opacity
        self.centered = is_centered

        self.font.set_bold(is_bold)
        self.font.set_italic(is_italic)
        self.font.set_underline(is_underline)

        if is_number_formatting: self.text = self.format_long_number()

        self.rendered_images = [self.render_text(line) for line in self.text.split('\n')]

    def draw(self, screen: pg.Surface = C.SCREEN, new_pos = None) -> None:
        x, y = new_pos or self.pos
        for img in self.rendered_images:
            chars = img if isinstance(img, list) else [img]
            row_x = x
            for char in chars:
                dest = char.get_rect(center=(row_x, y)) if self.centered else (row_x, y)
                screen.blit(char, dest)
                row_x += char.get_width()
            y += chars[0].get_height()

    def render_text(self, text: str) -> pg.Surface | list[pg.Surface]:
        if isinstance(self.color, RainbowConfig) and self.color.enabled:
            images = []
            for char, color in zip(text, self.rainbow_generator()):
                surf = self.font.render(char, True, color)
                surf.set_alpha(self.opacity)
                images.append(surf)
            return images
        else:
            surf = self.font.render(text, True, self.color)
            surf.set_alpha(self.opacity)
            return surf

    def format_long_number(self) -> str:
        n = int(float(self.text))
        for threshold, suffix in [(1_000_000_000_000, 'T'), (1_000_000_000, 'B'), (1_000_000, 'M'), (1_000, 'k')]:
            if n >= threshold:
                val = n / threshold
                return f"{val:.1f}{suffix}".replace(".0", "")
        return str(n)

    def rainbow_generator(self, start_hue: int = 0):
        hue = start_hue
        while True:
            rgb = colorsys.hsv_to_rgb(hue / 360.0, 1, self.color.fixed_lightness / 100.0)
            yield [int(c * 255) for c in rgb]
            hue = (hue + self.color.hue_step) % 360

PLAYER_NAME = Text(PLAYER.name, 
                   C.FONTS[FontSize.L], 
                   pos = pg.Vector2(224 * C.SCREEN_SCALE.x, 80 * C.SCREEN_SCALE.y), 
                   is_centered = True,
                   is_underline = True)