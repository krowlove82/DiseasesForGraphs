from typing import Tuple, List

import pygame
from tkinter import *
import Vertices
import Edges
import random

root = Tk()
canvas = Canvas(root, bg="black", height=1100, width=2000)
image = PhotoImage(file="us.gif")
# image = image.zoom(25)
# image = image.subsample(15)
# root.attributes("-fullscreen", True)
label = Label(root, image=image)
label.place(x=0, y=0)
canvas.pack()



def main() -> None:

    objects = [
        # Vertices(pos=(200, 400))
    ]

    pygame.init()

    # Game loop
    running = True
    fps = 60
    dt = 1 / fps
    clock = pygame.time.Clock()

    while running:
        root.update()
        # Redraw
        for o in objects:
            o.draw(canvas)

        # Show what we have drawn
        clock.tick(fps)


        # Event Loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
            elif e.type == pygame.KEYDOWN:
                print("damn")
                if e.key == pygame.K_SPACE:
                    print("fuck")
                    root.attributes("-fullscreen", False)




    # Shut down pygame
    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
