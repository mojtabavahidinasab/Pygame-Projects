import pygame

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.width = 5
        self.height = 5
        self.color = (240, 240, 240)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.transform.scale(pygame.image.load("assets/images/bullet.png"), (5, 5))

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def move(self, speed):
        if self.direction == 0:
            self.x -= speed
        if self.direction == 1:
            self.x += speed
        if self.direction == 2:
            self.y -= speed
        if self.direction == 3:
            self.y += speed