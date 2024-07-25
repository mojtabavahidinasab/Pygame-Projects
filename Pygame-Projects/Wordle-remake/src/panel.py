import pygame

class Panel:

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.width, self.height = 50, 50
        self.text = text
        self.font = pygame.font.Font("Pygame-Projects/Wordle-remake/assets/font.ttf", 30)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color_main = (30, 30, 30)

    def draw(self, win):

        pygame.draw.rect(win, self.color_main, pygame.Rect(self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(self.x - 2, self.y - 2, self.width + 4, self.height + 4), 2, 2, 2, 2)

        self.text_ = self.font.render(format(self.text), True, (255, 255, 255))

        rect = self.text_.get_rect(center = (self.x + self.width//2, self.y + self.height//2 - 3))

        win.blit(self.text_, rect)