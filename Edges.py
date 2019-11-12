import pygame

class Edges:

    def __init__(self):
        self.edges={}

    def generate_edges(self,surface,cities):
        # Generates edges
        #edges={}
        for node in cities:
            for neighbor in cities[node]:
                self.edges.update({node, neighbor})
                pygame.draw.line(surface, (0, 0, 0), node, neighbor, 5)

    def generate_weights(self):
        pass