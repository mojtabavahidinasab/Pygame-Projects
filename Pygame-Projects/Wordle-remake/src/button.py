import pygame

class Button:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.width, self.height = 40, 60
        self.font = pygame.font.SysFont("Pygame-Projects/Wordle-remake/assets/font.ttf", 30)
        self.text = text
        self.color = (60, 60, 60)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clicked = False

    def draw(self, win):

        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        text_ = self.font.render(format(self.text), True, (255, 255, 255))

        rect = text_.get_rect(center = (self.x + self.width//2, self.y + self.height//2))

        win.blit(text_, rect)

        pos = pygame.mouse.get_pos()

        if not self.clicked:
            if self.rect.collidepoint(pos):
                self.color = (40, 40, 40)
            else:
                self.color = (60, 60, 60)