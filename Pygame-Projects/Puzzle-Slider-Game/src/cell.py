import pygame

class Cell:
    def __init__(self, x, y, width, height, value):
        self.x = x
        self.y = y
        self.width, self.height = width, height
        self.value = value
        self.color = (64, 64, 64, 1) if self.value is not None else (255, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.SysFont("Tahoma", self.height//2)

    def draw(self, win):

        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, self.color, pygame.Rect(self.x - 5, self.y - 5, self.width + 10, self.height + 10), 5, 5, 5, 5)

        if self.value is not None:
            text = self.font.render(format(self.value), True, (192, 192, 192))
            rect = text.get_rect(center = (self.x + self.width//2, self.y + self.height//2))

            win.blit(text, rect)
