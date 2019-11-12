from typing import Tuple, List

import pygame
import Edges
import random


class Button:
    def __init__(self, width, height, center, text, background, font, id):
        self.surface = pygame.Surface((width, height))
        self.rect = self.surface.get_rect()
        self.surface.fill(background)
        self.rect.center = center
        self.textSurf = font.render(text, 1, [0, 0, 0])
        self.textRect = self.textSurf.get_rect(center = (width / 2, height / 2))
        self.surface.blit(self.textSurf, self.textRect)
        self.rect = pygame.Rect(center, (width, height))
        self.id = id

    def draw(self, screen):
        screen.blit(self.surface, self.rect)
        pygame.draw.rect(screen, [0, 0, 0], self.rect, 1)


def main() -> None:

    edges = [
        # Edges("animal", random.randint(1, 15)),
        # Edges("water", random.randint(1, 15)),
        # Edges("air", random.randint(1, 15))
    ]

    pygame.init()

    pygame.init()
    screen = pygame.display.set_mode([1200, 625], pygame.FULLSCREEN)
    bg_color = [255, 255, 255]
    screen.fill(bg_color)
    black = [0, 0, 0]
    pygame.display.set_caption('Disease Graph')
    image = pygame.image.load('us.gif')
    font = pygame.font.Font("freesansbold.ttf", 16)

    buttons = [
        Button(80, 40, (900, 200), "Cholera", [0, 0, 150], font, "Cholera"),
        Button(100, 40, (900, 300), "Spanish Flu", [150, 0, 0], font, "Flu"),
        Button(80, 40, (900, 400), "Plague", [0, 150, 0], font, "Plague")
    ]


    # Game loop
    running = True
    fps = 60
    dt = 1 / fps
    clock = pygame.time.Clock()

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

        for b in buttons:
            b.draw(screen)

        # Redraw
        for o in edges:
            pass

        pygame.display.flip()
        # Event Loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                for b in buttons:
                    if b.rect.collidepoint(pygame.mouse.get_pos()):
                        if b.id == "Cholera":
                            print("Cholera clicked")
                        elif b.id == "Flu":
                            print("Flu clicked")
                        elif b.id == "Plague":
                            print("Plague clicked")





    # Shut down pygame
    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
