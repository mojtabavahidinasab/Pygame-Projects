import pygame

class ColorButton:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width, self.height = 20, 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):

        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))