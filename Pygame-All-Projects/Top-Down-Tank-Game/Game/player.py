import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = self.height = 64
        self.color = (255, 100, 100)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.center_x = self.x + self.width/2
        self.center_y = self.y + self.height/2
        self.visible = True
        self.img = pygame.transform.scale(pygame.image.load("Top-Down-Tank-Game/assets/images/Tanks.png"), (64, 64))
        self.dirn = 0

#----------Cannon----------#
        self.cannon_img = pygame.transform.scale(pygame.image.load("Top-Down-Tank-Game/assets/images/cannon.png"), (50, 50))

        self.cannon_left_x = self.center_x - 50
        self.cannon_left_y = self.center_y - 25
        self.cannon_right_x = self.center_x
        self.cannon_right_y = self.center_y - 25
        self.cannon_up_y = self.center_y - 50
        self.cannon_up_x = self.center_y - 25
        self.cannon_down_y = self.center_y
        self.cannon_down_x = self.center_y - 25

        self.cannon_dirn = 0
#----------Cannon----------#

#----------HealthBar----------#
        self.bar_x = self.x
        self.bar_y = self.y - 50
        self.bar_width_red = self.width
        self.bar_width_green = self.width
        self.bar_height = 15
        self.color_1 = (240, 0, 0)
        self.color_2 = (0, 240, 0)
#----------HealthBar----------#

        self.speed = 15

    def draw(self, win):
        if self.visible:

            if self.dirn == 0:
                win.blit(pygame.transform.rotate(self.img, 90), (self.x, self.y))

            if self.dirn == 1:
                win.blit(pygame.transform.rotate(self.img, -90), (self.x, self.y))

            if self.dirn == 2:
                win.blit(pygame.transform.rotate(self.img, 0), (self.x, self.y))

            if self.dirn == 3:
                win.blit(pygame.transform.rotate(self.img, 180), (self.x, self.y))
                
            if self.cannon_dirn == 0:#left
                win.blit(pygame.transform.rotate(self.cannon_img, 90), (self.cannon_left_x, self.cannon_left_y))

            if self.cannon_dirn == 1:#right
                win.blit(pygame.transform.rotate(self.cannon_img, -90), (self.cannon_right_x, self.cannon_right_y))

            if self.cannon_dirn == 2:#up
                win.blit(pygame.transform.rotate(self.cannon_img, 0), (self.cannon_up_x, self.cannon_up_y))

            if self.cannon_dirn == 3:#down
                win.blit(pygame.transform.rotate(self.cannon_img, 180), (self.cannon_down_x, self.cannon_down_y))


            pygame.draw.rect(win, self.color_1, pygame.Rect(self.bar_x, self.bar_y, self.bar_width_red, self.bar_height))
            pygame.draw.rect(win, self.color_2, pygame.Rect(self.bar_x, self.bar_y, self.bar_width_green, self.bar_height))

        if self.bar_width_green == 0:
            self.visible = False