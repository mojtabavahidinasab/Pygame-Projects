import pygame
from random import choice
pygame.font.init()


pygame.init()

class Ball:
    def __init__(self):
        self.x = 292
        self.y = 292
        self.width = self.height = 15
        self.color = (0, 0, 0)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vel_x = 5
        self.vel_y = 10
        self.left = choice([True, False])
        self.up = choice([True, False])
        self.down = False
        self.collision_1 = self.rect.colliderect(P_1.rect)
        self.collision_2 = self.rect.colliderect(P_2.rect)

    def draw(self):
        self.rect = pygame.draw.rect(w.win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def move(self):
        if self.left:
            self.x -= self.vel_x
        else:
            self.x += self.vel_x


        if self.up:
            self.down = False
            self.y -= self.vel_y
        else:
            self.down = True
            self.y += self.vel_y


    def collide_walls(self):
        if self.y >= (w.height - self.height):
            self.down = False
            self.up = True

        if self.y <= 0:
            self.up = False
            self.down = True


    def collide_paddle(self):
        
        if (self.y >= P_1.y and self.y <= P_1.y + P_1.height) and (self.x == P_1.x + P_1.width + 2): 
            self.left = False
            w.score += 1

        if (self.y >= P_2.y and self.y <= P_2.y + P_2.height) and (self.x + self.width >= P_2.x):
            self.left = True
            w.score += 1

                


    def reset(self):
        if self.x < -5 or self.x > w.width:
            self.x = 292
            self.y = 292
            w.lives -= 1
            self.left = choice([True, False])



class Paddle:
    def __init__(self, x, y):
        self.width = 15
        self.height = (self.width*(8))
        self.color = (0, 0, 0)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vel = 20


    def draw(self):
        self.rect = pygame.draw.rect(w.win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        self.text = w.font.render("lives: " + format(w.lives), True, self.color, w.color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (520, 50)
        w.win.blit(self.text, self.text_rect)

        self.text_2 = w.font.render("Score: " + format(w.score), True, self.color, w.color)
        self.text_rect_2 = self.text_2.get_rect()
        self.text_rect_2.center = (70, 50)
        w.win.blit(self.text_2, self.text_rect_2)





class window:
    def __init__(self):
        self.width = 600
        self.height = 600
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (255, 255, 255)
        self.lives = 5
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.score = 0

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_DOWN] and (P_1.y < w.height - P_1.height):
                P_1.y += P_1.vel
                P_2.y += P_2.vel

            if keys[pygame.K_UP] and (P_1.y > 0):
                P_1.y -= P_1.vel
                P_2.y -= P_2.vel

            self.win.fill(self.color)
            P_1.draw()
            P_2.draw()
            B.draw()
            B.move()
            B.collide_walls()
            B.collide_paddle()
            B.reset()
            pygame.display.update()
            self.clock.tick(30)


            if w.lives == 0:
                run = False
                print(self.score)



P_1 = Paddle(25, 240)
P_2 = Paddle(560, 240)
B = Ball()
w = window()
w.run()