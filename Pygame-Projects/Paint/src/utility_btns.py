import pygame

class UtilityBtn:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.width, self.height = 40, 40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (255, 255, 255)
        self.font = pygame.font.SysFont('monospace', 10)

    def draw(self, win):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        text = self.font.render(format(self.text), True, (0, 0, 0))
        rect = text.get_rect(center = (self.x + self.width/2, self.y + self.height/2))
        win.blit(text, rect)