import pygame as pg
import constants as C
from player import PLAYER
from data.configs import IconLabel


class Button:
    def __init__(self,
                 image: pg.Surface,
                 pos: pg.Vector2 = (0.0, 0.0),
                 click_side: tuple[bool, bool] = (True, False),
                 cd: int = 150,
                 animated: tuple[int, int] = (0, 0)) -> None:

        self.base_image = image
        self.image = image
        self.pos = pos
        self.rect = self.image.get_rect(topleft=pos)

        self.opacity = 255
        self.cooldown = cd
        self.left_click_enabled = click_side[0] or not click_side[1]
        self.right_click_enabled = click_side[1]
        self.last_left_click_time = 0
        self.last_right_click_time = 0

        self.animated = None
        if animated[0] > 0 and animated[1] > 0:
            self.animated = animated
            self.animated_frames = animated[0]
            self.animated_cd = animated[1]
            self.current_frame_time = pg.time.get_ticks()
            self.frame = 0

            size = image.get_height()
            self.animation_list = [
                pg.transform.smoothscale_by(image.subsurface(i * size, 0, size, size), C.SCALE_X * 2)
                for i in range(self.animated_frames)
            ]
            self.base_image = self.animation_list[0]

    def draw(self,
             screen: pg.Surface = C.SCREEN,
             rescale: float | None = None,
             opacity: int = 255,
             rotation: float | None = None) -> None:

        if self.animated:
            now = pg.time.get_ticks()
            if now - self.current_frame_time >= self.animated_cd:
                self.frame = (self.frame + 1) % self.animated_frames
                self.current_frame_time = now
            self.image = self.animation_list[self.frame]
        else:
            self.image = self.base_image

        if rescale is not None:
            self.image = pg.transform.smoothscale_by(self.image, rescale)

        if rotation is not None:
            self.image = pg.transform.rotate(self.image, rotation)

        self.rect = self.image.get_rect(center=self.pos)

        if self.is_ready():
            self.opacity = opacity
        self.image.set_alpha(self.opacity)

        screen.blit(self.image, self.rect)

    def clicked(self, click_opacity: int = 200) -> bool:
        if (self.left_click_enabled
                and PLAYER.left_clicked
                and self.rect.collidepoint(PLAYER.pos)
                and self._click_ready(self.last_left_click_time)):
            self.last_left_click_time = pg.time.get_ticks()
            self.opacity = click_opacity
            return True

        if (self.right_click_enabled
                and PLAYER.right_clicked
                and self.rect.collidepoint(PLAYER.pos)
                and self._click_ready(self.last_right_click_time)):
            self.last_right_click_time = pg.time.get_ticks()
            self.opacity = click_opacity
            return True

        return False

    def is_ready(self) -> bool:
        now = pg.time.get_ticks()
        return (now - self.last_left_click_time >= self.cooldown and
                now - self.last_right_click_time >= self.cooldown)

    def _click_ready(self, last_click_time: int) -> bool:
        return pg.time.get_ticks() - last_click_time >= self.cooldown
    
SETTINGS_BUTTON = Button(C.ICONS[IconLabel.TRIPLE_DOTS], (1860 * C.SCREEN_SCALE.x, 30 * C.SCREEN_SCALE.y))