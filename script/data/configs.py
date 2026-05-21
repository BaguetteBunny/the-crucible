import enum

class RainbowConfig:
    def __init__(self, enabled: bool = False, hue_step: int = 10, fixed_lightness: int = 80) -> None:
        self.enabled = enabled
        self.hue_step = hue_step
        self.fixed_lightness = fixed_lightness

class Shapes(enum.Enum):
    CIRCLE = 0
    SQUARE = 1
    TRIANGLE = 2

class Colors(tuple, enum.Enum):
    BLACK = (0, 0, 0)
    GRAY = (80, 80, 80)
    BG_MAIN = (30, 30, 30)
    WHITE = (255,255,255)

class Tool(enum.Enum):
    DRILL = 1
    SIFTER = 2

class FontSize(enum.Enum):
    XS4 = 0
    XS3 = 1
    XS2 = 2
    XS = 3
    S = 4
    M = 5
    L = 6
    XL = 7
    XL2 = 8
    XL3 = 9
    XL4 = 10
    XL5 = 11
    XL6 = 12
    XL7 = 13
    XL8 = 14

class MenuLabel(enum.Enum):
    SIDEBAR = 0
    SETTINGS = 1