import ctypes
import pygame as pg
from data.configs import FontSize, MenuLabel, IconLabel

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Size Constants
SCREEN_SIZE = pg.Vector2(screensize[0], screensize[1])
SCREEN_SCALE = pg.Vector2(SCREEN_SIZE.x / 1920, SCREEN_SIZE.y / 1080)
MIDPOINT = SCREEN_SIZE.elementwise() / 2

# Main Constants
FPS = 60
SCREEN = pg.display.set_mode((SCREEN_SIZE))
CLOCK = pg.time.Clock()
VERSION = "Alpha v0"

DRAG_THRESHOLD = 5

# Pathing Constants
ASSETS_PATH = "./assets/"
FONTS_PATH = ASSETS_PATH + "./fonts/"
MENU_PATH = ASSETS_PATH + "./menu/"
TOOLS_PATH = ASSETS_PATH + "./tools/"
ICONS_PATH = ASSETS_PATH + "./icons/"

# Asset Constants
FONTS = {
    FontSize.XS4: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 2),
    FontSize.XS3: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 5),
    FontSize.XS2: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 10),
    FontSize.XS: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 15),
    FontSize.S: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 20),
    FontSize.M: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 30),
    FontSize.L: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 40),
    FontSize.XL: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 50),
    FontSize.XL2: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 60),
    FontSize.XL3: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 70),
    FontSize.XL4: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 80),
    FontSize.XL5: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 90),
    FontSize.XL6: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 100),
    FontSize.XL7: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 110),
    FontSize.XL8: pg.font.Font(FONTS_PATH + "monogram-extended.ttf", 120),
}

MENUS = {
    MenuLabel.SIDEBAR: pg.transform.scale_by(pg.image.load(MENU_PATH + "sidebar.png").convert_alpha(), SCREEN_SCALE.x),
    MenuLabel.SETTINGS: pg.transform.scale_by(pg.image.load(MENU_PATH + "settings.png").convert_alpha(), SCREEN_SCALE.x),
}

ICONS = {
    IconLabel.COIN: pg.transform.scale_by(pg.image.load(ICONS_PATH + "coin.png").convert_alpha(), SCREEN_SCALE.x),
    IconLabel.HEART: pg.transform.scale_by(pg.image.load(ICONS_PATH + "heart.png").convert_alpha(), SCREEN_SCALE.x),
    IconLabel.MUTED_SPEAKER: pg.transform.scale_by(pg.image.load(ICONS_PATH + "speaker-crossed.png").convert_alpha(), SCREEN_SCALE.x),
    IconLabel.SPEAKER: pg.transform.scale_by(pg.image.load(ICONS_PATH + "speaker.png").convert_alpha(), SCREEN_SCALE.x),
    IconLabel.TRIPLE_DOTS: pg.transform.scale_by(pg.image.load(ICONS_PATH + "3-dots.png").convert_alpha(), SCREEN_SCALE.x),
    IconLabel.STAR: pg.transform.scale_by(pg.image.load(ICONS_PATH + "star.png").convert_alpha(), SCREEN_SCALE.x),
}
