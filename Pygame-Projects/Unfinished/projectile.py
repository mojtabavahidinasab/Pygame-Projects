import pygame, math, random

pygame.init()


class Projectile:
    def __init__(self, x, y, vel, angle):
        self.x = x
        self.y = y
        self.color = (100, 100, 100)
        self.radius = 10
        self.vel = vel
        self.angle = angle
        self.vel_x = (math.cos(self.angle) * self.vel)
        self.vel_y = (math.sin(self.angle) * self.vel)
        self.time = 0
        self.dist_x = 0
        self.dist_y = 0
        self.InMotion = False
        self.final_x = self.x
        self.final_y = self.y

        
    def draw(self):
        pygame.draw.circle(M.win, self.color, (self.final_x, self.final_y), self.radius)

    def move(self):
        if P.InMotion:
            self.time += 0.5
            self.dist_x = (self.vel_x * self.time)
            self.dist_y = (self.vel_y * self.time) + ((-4.9 * (self.time ** 2)) / 2)
            self.final_x = self.x + self.dist_x
            self.final_y = self.y - self.dist_y


            if self.final_y >= self.y + 1:
                P.InMotion = False
                self.time = 0

        else:
            self.final_x = self.x 
            self.final_y = self.y


class Main:
    def __init__(self):
        self.width = 1200
        self.height = 500
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (240, 240, 240)
        self.LoopVar = True
        self.clock = pygame.time.Clock()
        self.pos_init = (0, 0)
        self.pos_final = (0, 0)

    def run(self):
        while self.LoopVar:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.LoopVar = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                P.InMotion = True

            self.win.fill(self.color)
            P.draw()
            P.move()
            pygame.display.update()
            self.clock.tick(30)

M = Main()
P = Projectile(12, 388, 50, (math.pi) / 3)
M.run()
