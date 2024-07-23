import pygame
import random
from random import choice

pygame.init()

class Tiles:
    def __init__(self, x, y, color):
      self.width = 49
      self.height = 19
      self.x = x
      self.y = y
      self.color = color
      self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
      self.visibility = True



    def draw(self):
        if self.visibility:
            self.rect = pygame.draw.rect(S.window, self.color, pygame.Rect(self.x, self.y, self.width, self.height))


    def collide_Ball(self):
        if pygame.Rect.colliderect(self.rect, B.rect):
            self.visibility = False
            B.down = True
            B.vel_x = random.choice(B.vel_x_list)

class Ball:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = 247
        self.vel_x_list = [3, 5, 8, 10, 12, 13, 14, 15]
        self.y  = 389
        self.vel_y = 16
        self.vel_x = random.choice(self.vel_x_list)
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.x, self.y)
        self.left = choice([True, False])
        self.down = False

    def draw(self):
        self.rect = pygame.draw.rect(S.window, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def move(self):
        if not self.down:
            B.y -= B.vel_y
        else:
            B.y += B.vel_y
        
        
        if B.left:
            B.x -= B.vel_x
        else:
            B.x += B.vel_x


    def collide_Pad(self):
        if pygame.Rect.colliderect(P.rect, self.rect):
            self.down = False
            self.vel_x = random.choice(self.vel_x_list)

    def collide_walls(self):

        if self.y <= 0:
            self.down = True

        if self.x <= 0:
            self.left = False

        if self.x >= S.width - self.width:
            self.left = True

    def reset(self):
        if self.y >= S.height - self.height:
            self.x = 247
            self.y = 389
            self.left = choice([True, False])
            self.vel_x = random.choice(self.vel_x_list)
            self.down = False


class Pad:
    def __init__(self):
        self.width = 70
        self.height = 10
        self.x = ((S.width - self.width)//2)
        self.y = 400
        self.vel = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (255, 255, 255)


    def draw(self):
        self.rect = pygame.draw.rect(S.window, self.color, pygame.Rect(self.x, self.y, self.width, self.height))



class screen:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.window = pygame.display.set_mode((self.width, self.height))
        self.color = (0,0,0)
        self.clock = pygame.time.Clock()

    def run(self):
        Run = True
        while Run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False



            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and P.x > 0:
                P.x -= P.vel

            if keys[pygame.K_RIGHT] and P.x <= S.width - P.width:
                P.x += P.vel



            self.window.fill(self.color)
            P.draw()
            B.draw()
            B.move()
            B.collide_walls()
            B.reset()
            B.collide_Pad()

            T_1.draw()
            T_2.draw()
            T_3.draw()
            T_4.draw()
            T_5.draw()
            T_6.draw()
            T_7.draw()
            T_8.draw()
            T_9.draw()
            T_10.draw()

            T_1.collide_Ball()
            T_2.collide_Ball()
            T_3.collide_Ball()
            T_4.collide_Ball()
            T_5.collide_Ball()
            T_6.collide_Ball()
            T_7.collide_Ball()
            T_8.collide_Ball()
            T_9.collide_Ball()
            T_10.collide_Ball()


            pygame.display.update()
            self.clock.tick(30)



B = Ball()
S = screen()
P = Pad()
B = Ball()

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

T_1 = Tiles(0, 20, RED)
T_2 = Tiles(50, 20, BLUE)
T_3 = Tiles(100, 20, YELLOW)
T_4 = Tiles(150, 20, BLUE)
T_5 = Tiles(200, 20, YELLOW)
T_6 = Tiles(250, 20, RED)
T_7 = Tiles(300, 20, YELLOW)
T_8 = Tiles(350, 20, RED)
T_9 = Tiles(400, 20, BLUE)
T_10 = Tiles(450, 20, YELLOW)




S.run()