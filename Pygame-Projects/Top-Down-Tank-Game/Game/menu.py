import pygame

class Menu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 300
        self.height = 500
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (200, 200, 200)

    def draw(self, win):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height), 10, 10, 10, 10)

