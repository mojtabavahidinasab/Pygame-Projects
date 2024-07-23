import pygame

class Pixel:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.previous_color = (255, 255, 255)

    def draw(self, surface):

        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))