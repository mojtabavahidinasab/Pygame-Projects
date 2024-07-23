import pygame

class Utility_button:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.width = 200
        self.height = 40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = text

    def draw(self, win):
        font = pygame.font.Font("assets/font.ttf", 35)
        
        pygame.draw.rect(win, (60, 60, 60), pygame.Rect(self.x, self.y, self.width, self.height))

        text_ = font.render(format(self.text), True, (255, 255, 255))

        rect = text_.get_rect(center = (self.x + self.width//2, self.y + self.height//2))

        win.blit(text_, rect)

        
