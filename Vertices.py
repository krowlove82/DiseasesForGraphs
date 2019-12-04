
import pygame
from pygame.math import Vector2


class Vertices():

    def __init__(self, radius=1, color=None, pos=Vector2(0, 0), id=""):
        if color is None:
            color = [0, 0, 0]
        self.radius = radius
        self.color = color
        self.pos = pos
        self.id = id
        self.rect = pygame.Rect(self.pos.x - 10, self.pos.y - 10, radius * 2, radius * 2)

    def draw(self, surface):
        pos = inting(self.pos.x, self.pos.y)
        pygame.draw.circle(surface, self.color, pos, round(self.radius))

    def change_color(self, color):
        self.color = color


def inting(x, y):
    return round(x), round(y)