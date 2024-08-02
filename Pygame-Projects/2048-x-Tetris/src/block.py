import pygame
import random

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = self.height = 75
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.value = random.choices([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024], k=1)
        self.color_map = None
        self.font = pygame.font.SysFont('monospace', 30)
        self.falling = True
        self.variable_color = max(250 - self.value[0] * 1.5, 0)
        self.color = (240, self.variable_color, 240)

    def draw(self, win):

        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(self.x - 1, self.y - 1, self.width + 2, self.height + 2), 2, 2, 2, 2)
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))


        text = self.font.render(format(self.value[0]), True, (100, 100, 100))
        rect = text.get_rect(center = (self.x + self.width//2, self.y + self.height//2))
        win.blit(text, rect)

        if self.falling:
            self.y += 75//15

    def update_color(self):
        self.variable_color = max(200 - self.value[0] * 10, 0)
        self.color = (250, self.variable_color, 200)
