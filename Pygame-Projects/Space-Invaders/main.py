import pygame, random
from random import choice
import time

pygame.font.init()

class Player:
    def __init__(self):
        self.width = self.height = 64
        self.img = pygame.transform.scale((pygame.image.load('Pygame-Projects/Space-Invaders/Assets/player_img.png')), (self.width, self.height))
        self.x = ((640 - self.width)//2)
        self.y = 500
        self.vel = 32
        self.player_rect = pygame.Rect(self.x - 1/2, self.y - 1/2, self.width + 1, self.height + 1)
        self.red_health_width = (self.width + 1)
        self.green_health_width = (self.width + 1)
        self.health_rect_red = pygame.Rect(self.x - 1/2, self.y + 79, self.red_health_width, 10)
        self.health_rect_green = pygame.Rect(self.x - 1/2, self.y + 79, self.green_health_width, 10)
        self.is_alive = True
        self.score = 0
        self.lives = 3
        

    def draw(self):
        if self.is_alive:
            M.win.blit(self.img, (self.x, self.y))

            self.health_rect_red = pygame.draw.rect(M.win, (255, 0, 0), pygame.Rect(self.x - 1/2, self.y + 79, self.red_health_width, 10))
            self.health_rect_green = pygame.draw.rect(M.win, (0, 255, 0), pygame.Rect(self.x - 1/2, self.y + 79, self.green_health_width, 10))

        if self.green_health_width == 0:
            self.lives -= 1
            self.green_health_width = (self.width + 1)

        if self.lives == 0:
            self.is_alive = False
            M.max_bullets = 0
            print("Your score was: " + format(self.score))
            M.Run = False
            time.sleep(0.5)


        self.text = M.font.render("Score: " + format(self.score), True, (255, 255, 255), (100, 100, 100))
        self.text_rect = self.text.get_rect()
        self.text_rect.center =(450, 50)
        M.win.blit(self.text, self.text_rect)

        self.text_2 = M.font.render("Lives: " + format(self.lives), True, (255, 255, 255), (100, 100, 100))
        self.text_rect_2 = self.text_2.get_rect()
        self.text_rect_2.center =(150, 50)
        M.win.blit(self.text_2, self.text_rect_2) 

                
class Enemy:
    def __init__(self, x, y):
        self.width = self.height = 48
        self.img = pygame.transform.scale((pygame.image.load('Pygame-Projects/Space-Invaders/Assets/enemy.png')), (self.width, self.height))
        self.x = x
        self.y = y
        self.vel_list = [2, 4, 6, 8, 10, 12]
        self.vel =  choice(self.vel_list)
        self.rect = pygame.Rect(self.x - 1/2, self.y - 1/2, self.width + 1, self.height + 1)
        self.reset_x = [45, 60, 75, 90, 105, 150, 165, 180, 195, 210, 240, 270, 300, 350, 400, 450, 500, 550, 600, 610]
        self.reset_y = [-100, -75, -50, -25, 0]

    def draw(self):
        self.rect = pygame.draw.rect(M.win, (100, 100, 100), pygame.Rect(self.x - 1/2, self.y - 1/2, self.width + 1, self.height + 1))
        M.win.blit(self.img, (self.x, self.y))

        if self.rect.colliderect(pygame.Rect(M.bullet_x, M.bullet_y, 5, 15)):
                self.x = choice(self.reset_x)
                self.y  = choice(self.reset_y)
                self.vel = choice(self.vel_list)
                P.score += 1


        if (self.y >= M.height - self.height):
            P.green_health_width -= 13
            self.x = choice(self.reset_x)
            self.y  = choice(self.reset_y)
            self.vel = choice(self.vel_list)

        if self.rect.colliderect(P.player_rect):
            P.green_health_width -= 13
            self.x = choice(self.reset_x)
            self.y  = choice(self.reset_y)
            self.vel = choice(self.vel_list)
            P.score += 1

        self.y += self.vel

        


class Main:
    def __init__(self):
        self.width = self.height = 640
        self.win = pygame.display.set_mode((self.width, self.height))
        self.caption = pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.Run = True
        self.player_bullets =  []
        self.max_bullets = 6
        self.bullet = None
        self.bullet_vel = 12
        self.bullet_x = 0
        self.bullet_y = 0
        self.font = pygame.font.Font('freesansbold.ttf', 24)
 


    def handle_player_bullets(self):
        for self.bullet in self.player_bullets:
            pygame.draw.rect(self.win, (10, 255, 10), pygame.Rect(self.bullet_x, self.bullet_y, 5, 15))

            self.bullet_y -= self.bullet_vel


            if self.bullet_y < 0:
                self.player_bullets.remove(self.bullet)
                self.max_bullets = 6
            else:
                self.max_bullets = 0

        

    def run(self):
        while self.Run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Run = False


                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(self.player_bullets) < self.max_bullets:
                        self.bullet_x = (P.x + 65/2 - 5/2)
                        self.bullet_y = (P.y + P.height//2 - 2)
                        self.bullet = pygame.Rect(self.bullet_x, self.bullet_y, 5, 15)
                        self.player_bullets.append(self.bullet)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                self.Run = False

            if keys[pygame.K_LEFT] and (P.x >= 2):
                P.x -= P.vel

            if keys[pygame.K_RIGHT] and (P.x <= self.width - P.width - 2):
                P.x += P.vel


            self.win.fill((100, 100, 100))
            M.handle_player_bullets()
            E_1.draw()
            E_2.draw()
            P.draw()
            pygame.display.update()
            self.clock.tick(30)

P = Player()
E_1 = Enemy((random.randint(0, 600)), random.randint(-100, -5)) 
E_2 = Enemy((random.randint(0, 600)), random.randint(-100, -5)) 
M =  Main()
M.run()            
