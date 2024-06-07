import pygame, random

from player import Player
from bullet import Bullet
from enemy import Enemy
from button import Button
from label import Label
from menu import Menu

pygame.init()

pygame.mixer.init()

def check_collision(o1, o2):
    return(
        o1.x < o2.x + o2.width and 
        o1.x + o1.width > o2.x and 
        o1.y < o2.y + o2.height and 
        o1.y + o1.height > o2.y 
    )

class Main:
    def __init__(self):
        self.width, self.height = 1200, 700
        self.full_width = 1600
        self.color = (100, 100, 120)
        self.clock = pygame.time.Clock()
        self.Running = True
        self.win = pygame.display.set_mode((self.full_width, self.height))
        self.player = Player(400, 400)
        self.bullets = 10
        self.bullet_list = []
        self.counter = 0
        self.enemy_list = []
        self.last_enemy_generated = pygame.time.get_ticks()
        self.pos = None
        self.reload_btn = Button(1315, 200, 150, 50, (240, 100, 100), "Reload")
        self.revive_btn = Button(1315, 500, 150, 50, (240, 100, 100), "Revive")
        self.is_revive_clicked = False
        self.revive_visible = False
        self.score = 0
        self.bullet_count = Label("Bullets: ", self.bullets - self.counter, self.color, (1330, 300))
        self.score_label = Label("Score: ", self.score, self.color, (1330, 400))
        self.menu = Menu(1250, 100)
        self.tank_shooting = pygame.mixer.Sound("assets/sounds/tank-shooting.wav")
        self.tank_hit = pygame.mixer.Sound("assets/sounds/tank-hit.mp3")

    def enemy_bullet_collision(self):
        for enemy in self.enemy_list[:]:
            for bullet in self.bullet_list[:]:
                if check_collision(bullet, enemy):
                    self.enemy_list.remove(enemy)
                    self.bullet_list.remove(bullet)
                    self.score += 1
                    self.tank_hit.play()
                    self.tank_hit.set_volume(0.1)
                    break

    def enemy_player_collision(self):
        for enemy in self.enemy_list[:]:
            if check_collision(enemy, self.player):
                self.enemy_list.remove(enemy)
                self.player.bar_width_green -= 8
                self.score += 1
                self.tank_hit.play()
                self.tank_hit.set_volume(0.1)

    def revive(self):
        if not self.player.visible:
            self.revive_visible = True

        if self.is_revive_clicked:
            self.player.visible = True
            self.player.bar_width_green = self.player.width
            self.counter = 0
            self.is_revive_clicked = False
            self.revive_visible = False
            self.score = 0


    def main(self): 
        
        while self.Running:
            self.current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()

                    if self.reload_btn.clicked(self.pos):
                        self.counter = 0

                    if self.revive_btn.clicked(self.pos):
                        self.is_revive_clicked = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.counter < self.bullets:
                            bullet = Bullet(self.player.center_x, self.player.center_y, self.player.cannon_dirn)
                            self.bullet_list.append(bullet)
                            self.counter += 1
                            self.tank_shooting.play()
                            self.tank_shooting.set_volume(0.1)

                    if event.key == pygame.K_r:
                        self.counter = 0

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.player.x >= 15:
                self.player.dirn = 0

                self.player.x -= self.player.speed
                self.player.center_x -= self.player.speed

                self.player.bar_x -= self.player.speed

                self.player.cannon_left_x -= self.player.speed
                self.player.cannon_right_x -= self.player.speed
                self.player.cannon_up_x -= self.player.speed
                self.player.cannon_down_x -= self.player.speed
 
            if keys[pygame.K_RIGHT] and self.player.x <= self.width - self.player.width - 12:
                self.player.dirn = 1

                self.player.x += self.player.speed
                self.player.center_x += self.player.speed

                self.player.bar_x += self.player.speed

                self.player.cannon_left_x += self.player.speed
                self.player.cannon_right_x += self.player.speed
                self.player.cannon_up_x += self.player.speed
                self.player.cannon_down_x += self.player.speed

            if keys[pygame.K_UP] and self.player.y >= 15:
                self.player.dirn = 2

                self.player.y -= self.player.speed
                self.player.center_y -= self.player.speed

                self.player.bar_y -= self.player.speed

                self.player.cannon_up_y -= self.player.speed
                self.player.cannon_down_y -= self.player.speed
                self.player.cannon_left_y -= self.player.speed
                self.player.cannon_right_y -= self.player.speed

            if keys[pygame.K_DOWN] and self.player.y <= self.height - self.player.height - 12:
                self.player.dirn = 3

                self.player.y += self.player.speed
                self.player.center_y += self.player.speed

                self.player.bar_y += self.player.speed

                self.player.cannon_up_y += self.player.speed
                self.player.cannon_down_y += self.player.speed
                self.player.cannon_left_y += self.player.speed
                self.player.cannon_right_y += self.player.speed

            if keys[pygame.K_a]:
                self.player.cannon_dirn = 0

            if keys[pygame.K_s]:
                self.player.cannon_dirn = 3

            if keys[pygame.K_w]:
                self.player.cannon_dirn = 2

            if keys[pygame.K_d]:
                self.player.cannon_dirn = 1

            if self.current_time is not None and self.last_enemy_generated is not None:
                if self.current_time - self.last_enemy_generated >= 4000:
                    enemy = Enemy(random.choice([0, 50, 100, 200, 400, 800]), random.choice([0, 50, 100, 200, 400, 600]))
                    self.enemy_list.append(enemy)
                    self.last_enemy_generated = self.current_time


            self.win.fill(self.color)

            for bullet in self.bullet_list:
                bullet.move(self.player.speed)
                bullet.draw(self.win)

            self.player.draw(self.win)

            self.enemy_bullet_collision()
            self.enemy_player_collision()

            for enemy in self.enemy_list:
                enemy.draw(self.win)
                enemy.move(self.width, self.height)

            self.menu.draw(self.win)

            pygame.draw.line(self.win, (0, 0, 0), (1190, 0), (1190, 700), 5)

            self.reload_btn.draw(self.win)

            self.revive()

            if self.revive_visible:
                self.revive_btn.draw(self.win)

            if self.player.visible:
                self.bullet_count.update((self.bullets - self.counter), (1330, 300))
                self.bullet_count.render(self.win)

            self.score_label.update(self.score, (1330, 400))
            self.score_label.render(self.win)

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    M = Main()
    M.main()


# I don't understand the logic for enemy generation, but who cares?