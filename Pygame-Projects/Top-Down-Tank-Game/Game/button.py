import pygame

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def draw(self, win):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        self.text_render = self.font.render(format(self.text), True, (255, 255, 255), self.color)
        self.text_render_rect = self.text_render.get_rect()
        self.text_render_rect.center = self.rect.center

        win.blit(self.text_render, self.text_render_rect)
    
    def clicked(self, pos):
        if self.rect.collidepoint(pos):
            return True