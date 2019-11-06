import pygame
import random


def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


class Vertices:

    def __init__(self, radius=1, color=None, pos=(0, 0)):
        if color is None:
            color = get_random_color()
        self.radius = radius
        self.color = color
        self.pos = pos

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos.int(), round(self.radius))