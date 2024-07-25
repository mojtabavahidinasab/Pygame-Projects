import pygame, random

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = self.height = 40
        self.dirn = random.choice([1, 2, 3, 4])
        self.color = (200, 150, 150)
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.transform.scale(pygame.image.load("Pygame-Projects/Top-Down-Tank-Game/assets/images/enemy.png"), (40, 40))

    def draw(self, win):
        
        if self.dirn == 1:
            win.blit(pygame.transform.rotate(self.img, -90), (self.x, self.y))
        
        if self.dirn == 2:
            win.blit(pygame.transform.rotate(self.img, 90), (self.x, self.y))
        
        if self.dirn == 3:
            win.blit(pygame.transform.rotate(self.img, 180), (self.x, self.y))
        
        if self.dirn == 4:
            win.blit(pygame.transform.rotate(self.img, 0), (self.x, self.y))

    def move(self, width, height):
        if self.dirn == 1:
            self.x -= self.speed

        if self.dirn == 2:
            self.x += self.speed

        if self.dirn == 3:
            self.y -= self.speed

        if self.dirn == 4:
            self.y += self.speed

        if self.x <= 3:
            self.dirn = 2
        if self.x >= width - self.width - 11:
            self.dirn = 1
        if self.y <= 3:
            self.dirn = 4
        if self.y >= height - self.height - 11:
            self.dirn = 3
