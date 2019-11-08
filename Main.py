from typing import Tuple, List

import pygame
from tkinter import *
import Vertices
import Edges
import random


def main() -> None:

    objects = [
        # Vertices(pos=(200, 400))
    ]

    pygame.init()

    pygame.init()
    screen = pygame.display.set_mode([1200, 625], pygame.FULLSCREEN)
    bg_color = [255, 255, 255]
    screen.fill(bg_color)
    black = [0, 0, 0]
    pygame.display.set_caption('Disease Graph')
    image = pygame.image.load('us.gif')

    # Game loop
    running = True
    fps = 60
    dt = 1 / fps
    clock = pygame.time.Clock()
    font = pygame.font.Font("freesansbold.ttf", 16)
    while running:
        screen.fill(bg_color)
        screen.blit(image, (0, 0))

        # New York
        screen.blit(font.render("New York", True, black), [775, 170])
        pygame.draw.circle(screen, black, (765, 175), 10)
        # DC
        screen.blit(font.render("DC", True, black), [735, 230])
        pygame.draw.circle(screen, black, (735, 220), 10)
        # Altanta
        screen.blit(font.render("Atlanta", True, black), [630, 315])
        pygame.draw.circle(screen, black, (630, 340), 10)
        # Chicago
        screen.blit(font.render("Chicago", True, black), [560, 165])
        pygame.draw.circle(screen, black, (560, 190), 10)
        # Austin
        screen.blit(font.render("Austin", True, black), [420, 395])
        pygame.draw.circle(screen, black, (420, 420), 10)
        # LA
        screen.blit(font.render("LA", True, black), [70, 295])
        pygame.draw.circle(screen, black, (70, 320), 10)
        # Minneapolis
        screen.blit(font.render("Minneapolis", True, black), [480, 105])
        pygame.draw.circle(screen, black, (480, 130), 10)
        # Miami
        screen.blit(font.render("Miami", True, black), [720, 465])
        pygame.draw.circle(screen, black, (720, 490), 10)
        # Seattle
        screen.blit(font.render("Seattle", True, black), [80, 40])
        pygame.draw.circle(screen, black, (80, 30), 10)
        # Denver
        screen.blit(font.render("Denver", True, black), [300, 240])
        pygame.draw.circle(screen, black, (300, 230), 10)

        # Redraw
        for o in objects:
            pass

        pygame.display.flip()
        # Event Loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    pass




    # Shut down pygame
    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
