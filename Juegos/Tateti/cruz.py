import pygame as pg

color_p2 = 240, 84, 84

class Cruz:
    def __init__(self, x, y, pantalla):
        self.x = x-50
        self.y = y-50
        pg.draw.line(pantalla, color_p2, (self.x, self.y), (self.x+100, self.y+100))
        pg.draw.line(pantalla, color_p2, (self.x, self.y+100), (self.x+100, self.y))