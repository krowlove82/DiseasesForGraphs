import pygame

class Button:
    def __init__(self, width, height, center, text, background, font, id):
        self.surface = pygame.Surface((width, height))
        self.rect = self.surface.get_rect()
        self.surface.fill(background)
        self.rect.center = center
        self.textSurf = font.render(text, 1, [0, 0, 0])
        self.textRect = self.textSurf.get_rect(center=(width / 2, height / 2))
        self.surface.blit(self.textSurf, self.textRect)
        self.rect = pygame.Rect(center, (width, height))
        self.id = id
        self.font = font
        self.text = text
        self.width = width
        self.height = height
        self.center = center

    def draw(self, screen):
        screen.blit(self.surface, self.rect)
        pygame.draw.rect(screen, [0, 0, 0], self.rect, 1)

    def change_background(self, background):
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = self.surface.get_rect()
        self.surface.fill(background)
        self.rect.center = self.center
        self.textSurf = self.font.render(self.text, 1, [0, 0, 0])
        self.textRect = self.textSurf.get_rect(center=(self.width / 2, self.height / 2))
        self.surface.blit(self.textSurf, self.textRect)
        self.rect = pygame.Rect(self.center, (self.width, self.height))
