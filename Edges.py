import pygame
import random

class Edges:

    def __init__(self):
        self.first=[]
        self.second=[]
        self.weight=0
        self.type=0

    def add_edge(self,node,neighbor):
         self.first.append(node)
         self.second.append(neighbor)
         self.generate_edge_type()


    def generate_weights(self):
        self.weight=random.randint(1,10)

    def generate_edge_type(self):
       self.type=random.choice(["air","water","animals"])

    def draw(self,screen):

        if (self.type == "air"):
            pygame.draw.line(screen, (0,0,0), self.first[0], self.second[0], 5)
        elif (self.type == "water"):
            pygame.draw.line(screen, (0, 0, 255), self.first[0], self.second[0], 5)
        else:
            pygame.draw.line(screen, (255, 0, 0), self.first[0], self.second[0], 5)
        pass