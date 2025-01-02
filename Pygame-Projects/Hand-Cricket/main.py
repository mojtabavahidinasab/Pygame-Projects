#-------Imports--------#
from pygame import *
import random
import pygame.mixer
import time
pygame.init()
mixer.init()
#----------------------#

print("In this version, only the player can bat first.")
time.sleep(0.2)
print("When the score resets to 0, understand that the Player is out, and now the computer will bat.")
time.sleep(0.2)
print("The code is one of the worst that I've written, I dont even remember the amount of variables I've created.")

mixer.music.load("./sound.mp3")
mixer.music.set_volume(0.9)

pygame.display.set_caption("Hand Cricket!")

class Button:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.width = self.height = 80
        self.Button_color = (255, 90, 90)
        self.Hover_color = (90, 90, 255)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, self.Button_color, pygame.Rect(self.x, self.y, self.width, self.height), border_radius=5)

        self.text = Game.font.render(format(self.value), True, (255, 255, 255), self.Button_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + 20, self.y + 20)
        win.blit(self.text, self.text_rect)

        if self.rect.collidepoint(Game.pos):
            self.Button_color = self.Hover_color
        else:
            self.Button_color = (255, 90, 90)
    
class Main:
    def __init__(self):
        self.width = self.height = 600
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color_main = (240, 240, 240)
        self.font = pygame.font.Font('./moran.ttf', 30)
        self.pos = (0, 0)
        self.bat_score = 0
        self.clock = pygame.time.Clock()
        self.Run = True
        self.comp_choice = 0
        self.mouse_down = False
        self.Player_Batting = True
        self.comp_check = False
        self.Comp_Batting = False
        self.target = 0

    def score_text(self):
        # Score
        self.bat_score_text = self.font.render("Score: " + format(self.bat_score), True, (0, 0, 0), self.color_main)
        self.bat_score_text_rect = self.bat_score_text.get_rect()
        self.bat_score_text_rect.center = (80, 200)
        self.win.blit(self.bat_score_text, self.bat_score_text_rect)

        # Comp's Choice
        self.comp_text = self.font.render("Computer Played: " + format(self.comp_choice), True, (0, 0, 0), self.color_main)
        self.comp_text_rect = self.comp_text.get_rect()
        self.comp_text_rect.center = (200, 140)
        self.win.blit(self.comp_text, self.comp_text_rect)

        # Target
        self.target_text = self.font.render("Target: " + format(self.target), True, (0, 0, 0), self.color_main)
        self.target_text_rect = self.target_text.get_rect(center = (90, 260))
        if not self.Player_Batting:
            self.win.blit(self.target_text, self.target_text_rect)

    def OUT_AND_WIN_TEXT(self, msg):
        # Out Text
        # Player Wins and Comp Wins
        self.win_text = self.font.render(msg, True, (0, 0, 0), self.color_main)
        self.win_text_rect = self.win_text.get_rect(center = (300, 500))


        self.win.blit(self.win_text, self.win_text_rect)

    def check_winner(self):
        if not self.Player_Batting and self.Comp_Batting and (self.bat_score >= self.target):
            self.OUT_AND_WIN_TEXT("Comp Wins!")
 
        if not self.Comp_Batting and not self.Player_Batting and (self.bat_score < self.target):
            self.OUT_AND_WIN_TEXT("Player Wins!")

    def Redraw_window(self):
        self.clock.tick(60)
        self.win.fill(self.color_main)

        B_1.draw(self.win)
        B_2.draw(self.win)
        B_3.draw(self.win)
        B_4.draw(self.win)
        B_5.draw(self.win)
        B_6.draw(self.win)

        self.score_text()
        self.check_winner()
        pygame.display.update()

    def main(self):
        while self.Run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.Run = False
                
                if e.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()

                    if B_1.rect.collidepoint(self.pos):
                        mixer.music.play()
                        self.comp_choice = random.randint(1, 6)
                        if self.Player_Batting:
                            self.bat_score += B_1.value
                        else:
                            self.bat_score += self.comp_choice
                        self.mouse_down = True
                        if self.comp_choice == B_1.value and self.Player_Batting:
                            self.comp_check = True
                            self.target = self.bat_score - self.comp_choice + 1
                            self.bat_score = 0
                            self.Player_Batting = False
                            self.Comp_Batting = True
                        elif self.comp_choice == B_1.value:
                            self.Comp_Batting = False

                    if B_2.rect.collidepoint(self.pos):
                        self.comp_choice = random.randint(1, 6)
                        mixer.music.play()
                        if self.Player_Batting:
                            self.bat_score += B_2.value
                        else:
                            self.bat_score += self.comp_choice
                        self.mouse_down = True
                        if self.comp_choice == B_2.value and self.Player_Batting:
                            self.comp_check = True
                            self.target = self.bat_score - self.comp_choice + 1
                            self.bat_score = 0
                            self.Player_Batting = False
                            self.Comp_Batting = True
                        elif self.comp_choice == B_2.value:
                            self.Comp_Batting = False

                    if B_3.rect.collidepoint(self.pos):
                        mixer.music.play()
                        self.comp_choice = random.randint(1, 6)
                        if self.Player_Batting:
                            self.bat_score += B_3.value
                        else:
                            self.bat_score += self.comp_choice
                        self.mouse_down = True
                        if self.comp_choice == B_3.value and self.Player_Batting:
                            self.comp_check = True
                            self.target = self.bat_score - self.comp_choice + 1   
                            self.bat_score = 0
                            self.Player_Batting = False
                            self.Comp_Batting = True
                        elif self.comp_choice == B_3.value:
                            self.Comp_Batting = False

                    if B_4.rect.collidepoint(self.pos):
                        mixer.music.play()
                        self.comp_choice = random.randint(1, 6)
                        if self.Player_Batting:
                            self.bat_score += B_4.value
                        else:
                            self.bat_score += self.comp_choice
                        self.mouse_down = True
                        if self.comp_choice == B_4.value and self.Player_Batting:
                            self.comp_check = True
                            self.target = self.bat_score - self.comp_choice + 1
                            self.bat_score = 0
                            self.Player_Batting = False
                            self.Comp_Batting = True
                        elif self.comp_choice == B_4.value:
                            self.Comp_Batting = False


                    if B_5.rect.collidepoint(self.pos):                                        
                        mixer.music.play()
                        self.comp_choice = random.randint(1, 6)
                        if self.Player_Batting:
                            self.bat_score += B_5.value
                        else:
                            self.bat_score += self.comp_choice
                        self.mouse_down = True
                        if self.comp_choice == B_5.value and self.Player_Batting:
                            self.comp_check = True
                            self.target = self.bat_score - self.comp_choice + 1
                            self.bat_score = 0
                            self.Player_Batting = False
                            self.Comp_Batting = True
                        elif self.comp_choice == B_5.value:
                            self.Comp_Batting = False

                    if B_6.rect.collidepoint(self.pos):
                        mixer.music.play()
                        self.comp_choice = random.randint(1, 6)
                        if self.Player_Batting:
                            self.bat_score += B_6.value
                        else:
                            self.bat_score += self.comp_choice
                        self.mouse_down = True
                        if self.comp_choice == B_6.value and self.Player_Batting:
                            self.comp_check = True
                            self.target = self.bat_score - self.comp_choice + 1
                            self.bat_score = 0
                            self.Player_Batting = False
                            self.Comp_Batting = True
                        elif self.comp_choice == B_6.value:
                            self.Comp_Batting = False

            self.Redraw_window()

B_1 = Button(20, 20, 1)
B_2 = Button(116, 20, 2)
B_3 = Button(212, 20, 3)
B_4 = Button(308, 20, 4)
B_5 = Button(404, 20, 5)
B_6 = Button(500, 20, 6)

Game = Main()
time.sleep(1)
Game.main()
