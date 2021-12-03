import pygame as pg

color_p1 = 17, 153, 158

class Circulo:
    def __init__(self, x, y, pantalla):
        self.x = x
        self.y = y
        pg.draw.circle(pantalla, color_p1, (self.x, self.y), 60, 2)