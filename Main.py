from typing import Tuple, List

import pygame
from tkinter import *
import Vertices
import Edges
import random

# root = Tk()
# canvas = Canvas(root, bg="black", height=1100, width=2000)
# image = PhotoImage(file="us.gif")
# # image = image.zoom(25)
# # image = image.subsample(15)
# # root.attributes("-fullscreen", True)
# label = Label(root, image=image)
# label.place(x=0, y=0)
# canvas.pack()



def main() -> None:

    objects = [
        # Vertices(pos=(200, 400))
    ]

    pygame.init()

    pygame.init()
    screen = pygame.display.set_mode(size=[1200, 625])
    bg_color = [255, 255, 255]
    screen.fill(bg_color)
    pygame.display.set_caption('Disease Graph')
    image = pygame.image.load('us.gif')

    # Game loop
    running = True
    fps = 60
    dt = 1 / fps
    clock = pygame.time.Clock()
    while running:
        # root.update()
        screen.fill(bg_color)
        screen.blit(image, (0, 0))
        # Redraw
        for o in objects:
            pass
            # o.draw(canvas)

        pygame.display.flip()
        # Event Loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    pass
                    # root.attributes("-fullscreen", False)




    # Shut down pygame
    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
