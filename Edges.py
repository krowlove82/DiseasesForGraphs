import pygame
import random


class Edges:

    def __init__(self):
        self.first = []
        self.second = []
        self.weight = 0
        self.type = 0
        self.selected = False

    def add_edge(self, node, neighbor):
        self.first.append(node)
        self.second.append(neighbor)

    def generate_weights(self):
        self.weight = random.randint(1, 10)

    def generate_edge_type(self):
        self.type = random.choice(["air", "water", "animals"])

    def draw(self, screen, color=None):
        if self.type == "air":
            if color is None:
                color = [0, 0, 0]
            pygame.draw.line(screen, color, self.first[0], self.second[0], 5)
        elif self.type == "water":
            if color is None:
                color = [0, 0, 255]
            pygame.draw.line(screen, color, self.first[0], self.second[0], 5)
        elif self.type == "animals":
            if color is None:
                color = [255, 0, 0]
            pygame.draw.line(screen, color, self.first[0], self.second[0], 5)
        else:
            pygame.draw.line(screen, (0, 255, 0), self.first[0], self.second[0], 5)
