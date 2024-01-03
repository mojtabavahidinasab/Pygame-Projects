import pygame
from math import *

pygame.init()

class Object:
    def __init__(self):
        self.width = self.height = 50
        self.color = (240, 240, 240)
        self.angle = radians(45)
        self.omega = 0.1
        self.center_of_rotation_x = 200
        self.center_of_rotation_y = 250
        self.radius = 225
        self.x = (self.center_of_rotation_x + self.radius * self.omega * cos(self.angle))
        self.y = (self.center_of_rotation_y + self.radius * self.omega * sin(self.angle))
        self.const = 1

    def draw(self):
        pygame.draw.rect(Game.win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        #Rotation code
        self.angle = self.angle + self.omega
        self.x -= self.const*(self.radius * self.omega * cos(self.angle + pi / 2))
        self.y -= self.radius * self.omega * sin(self.angle + pi / 2)


class Main:
    def __init__(self):
        self.width = self.height = 800
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (10, 10, 10)
        self.Var = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.Var:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Var = False

            self.win.fill(self.color)
            Player.draw()
            pygame.display.update()
            self.clock.tick(30)

Player = Object()
Game = Main()
Game.run()