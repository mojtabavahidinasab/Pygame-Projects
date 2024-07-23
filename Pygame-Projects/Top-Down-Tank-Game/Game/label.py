import pygame

class Label:
    def __init__(self, text, value, color, pos):
        self.text = text
        self.value = value
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.color_text = (255, 255, 255)
        self.color = color
        self.pos = pos

    def update(self, value, pos):
        self.value = value
        self.pos = pos

    def render(self, win):
        text_surface = self.font.render(f"{self.text}{self.value}", True, self.color_text)
        text_rect = text_surface.get_rect(topleft=self.pos)
        pygame.draw.rect(win, self.color, text_rect)
        win.blit(text_surface, self.pos)