import pygame
from pygame.time import Clock
pygame.font.init()
from pygame.locals import *


class Obj_1:
    def __init__(self, x, y, win, width, height, color, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.value = value
        self.win = win
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.value = 1
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.text = self.font.render(format(self.value), True, (255,255,255))
        self.text_x = (self.x + self.width // 2 - 4)
        self.text_y = (self.y + self.height // 2 - 6)
        self.visible = True


    def draw(self):
        self.rect = pygame.draw.rect(self.win, self.color, pygame.Rect(self.x,self.y,self.width,self.height))
        W.win.blit(self.text, (self.text_x, self.text_y))


class Player:
    def __init__(self):
        self.x = self.y = 0
        self.width = self.height = 25
        self.color = (255,0,0)
        self.vel = 25
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.value = 2
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.text = self.font.render(format(self.value), True, (255,255,255))
        self.text_x = (self.x + self.width // 2 - 4)
        self.text_y = (self.y + self.height // 2 - 6)
        self.game_over = False


    def draw(self):
        self.rect = pygame.draw.rect(W.win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        W.win.blit(P.text, (self.text_x, self.text_y))


    def collisions(self):
        collision = self.rect.colliderect(O.rect)
        if collision:
            O.visible = False
            self.value +=  O.value
            self.text = self.font.render(format(self.value), True, (255,255,255))
            W.win.blit(P.text, (self.text_x, self.text_y))
            O.value = 0

        collision = self.rect.colliderect(O_2.rect)
        if collision:
            O_2.visible = False
            self.value += O_2.value
            self.text = self.font.render(format(self.value), True, (255,255,255))
            W.win.blit(P.text, (self.text_x, self.text_y))
            O_2.value = 0

        collision = self.rect.colliderect(O_3.rect)
        if collision:
            O_3.visible = False
            self.value += O_3.value
            self.text = self.font.render(format(self.value), True, (255,255,255))
            W.win.blit(P.text, (self.text_x, self.text_y))
            O_3.value = 0

        collision = self.rect.colliderect(O_4.rect)
        if collision:
            O_4.visible = False
            self.value -= O_4.value
            self.text = self.font.render(format(self.value), True, (255,255,255))
            W.win.blit(P.text, (self.text_x, self.text_y))
            O_4.value = 0



        



class Window:
    def __init__(self):
        self.width = self.height = 500
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (0, 0, 0)
        self.line_color = (255, 255, 255)
        self.line_x = 25
        self.line_y = 25
        self.clock = pygame.time.Clock()
        self.timer = 30
        self.dt = 0
        self.timer_over = False


    def draw_line(self):
        self.line_x = 25
        self.line_y = 25
        for a in range(1,  self.win.get_width()//25):
            pygame.draw.line(W.win, self.line_color, (self.line_x, 0), (self.line_x, self.height))
            self.line_x += 25

        for v in range(1, self.win.get_height()//25):
            pygame.draw.line(W.win, self.line_color, (0, self.line_y), (self.width, self.line_y))
            self.line_y += 25

    def Game_over(self):
        if P.value == 5:
             P.game_over = True


    def run(self):
        Run = True
        while Run:
            W.Game_over()
            pygame.time.delay(15)
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pos)



                if event.type == pygame.QUIT:
                    Run = False

                if P.game_over:
                    Run = False
                    if not(self.timer_over):
                        print("Game Over! You won!")
                        pass



            self.timer -= self.dt
            if self.timer <= 0:
                self.timer_over = True
                Run = False


            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and P.x > 2:
                P.x -= P.vel
                self.left = True
                self.right = False
                self.up = False
                self.down = False
                P.text_x -= 25

            if keys[pygame.K_RIGHT] and P.x < (W.width - P.width - 2):
                P.x += P.vel
                self.left = False
                self.right = True
                self.up = False
                self.down = False
                P.text_x += 25

            
            if keys[pygame.K_UP] and P.y > 2:
                P.y -= P.vel
                self.left = False
                self.right = False
                self.up = True
                self.down = False
                P.text_y -= 25

            if keys[pygame.K_DOWN] and P.y < (W.height - P.height - 2):
                P.y += P.vel
                self.left = False
                self.right = False
                self.up = False
                self.down = False
                P.text_y += 25

            W.win.fill(W.color)
            P.draw()
            W.draw_line()
            P.collisions()
            if O.visible:
                O.draw()
            if O_2.visible:
                O_2.draw()
            if O_3.visible:
                O_3.draw()
            if O_4.visible:
                O_4.draw()
            pygame.display.update()
            self.dt = self.clock.tick(1000) / 1000
            print(self.timer)


P = Player()
W = Window()
O = Obj_1(325, 50, W.win, 25, 25, (0,255,0), 1)
O_2 = Obj_1(375, 250, W.win, 25, 25, (0,255,0), 1)
O_3 = Obj_1(425, 450, W.win, 25, 25, (0,255,0), 1)
O_4 = Obj_1(225, 150, W.win, 25, 25, (0,0,255), 1)
W.run()