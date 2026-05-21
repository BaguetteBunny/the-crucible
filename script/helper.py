import pygame as pg

sign = lambda x: 1 if x > 0 else -1 if x < 0 else 0

def sign_vec2(v: pg.Vector2): return pg.Vector2(sign(v.x), sign(v.y))
