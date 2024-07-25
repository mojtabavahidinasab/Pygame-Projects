import pygame
import random

pygame.init()

from button import Button
from panel import Panel
from utility_btn import Utility_button

btn_width ,btn_height = 40, 60
panel_w = panel_h = 50

WORD_LIST = ["ALIVE", "DEATH", "MOUSE", "MONEY", "WOULD", "COULD", "PHONE", "WATCH", "WIRES", "GAMES", "GRASS"]

WORD = random.choice(WORD_LIST)

class Main:
    def __init__(self):
        self.width, self.height = 600, 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.keyboard_list = []
        self.letters_clicked = 0
        self.panel_list = []
        self.back_btn = Utility_button(66, 650, "Back")
        self.enter_btn = Utility_button(332, 650, "Enter")
        self.current_word = ""
        self.game_over = False

    def panels(self):

        x_space = (350//6)
        
        for y in range(6):
            for x in range(5):
                panel = Panel((x_space + (x * (panel_w + x_space))), (50 + (y * (panel_h + 15))), "")
                self.panel_list.append(panel)

    def keyboard(self):

        for x in range(13):
            for y in range(2):
                btn = Button(5 + (x * (btn_width + (80//13))), (510 + (y * (btn_height + (10//2)))), None)

                self.keyboard_list.append(btn)

        str = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"

        list = str.split(',')

        for i in range(len(self.keyboard_list)):
            btn = self.keyboard_list[i]
            btn.text = list[i]

    def enter_clicked(self):

        self.current_word = ""

        if self.letters_clicked % 5 != 0:
            pass

        else:
            hashmap = {}

            for i in range(self.letters_clicked - 5, self.letters_clicked):
                letter = self.panel_list[i].text
                self.current_word += letter
                if self.letters_clicked <= 4:
                    hashmap[WORD[i]] = self.panel_list[i]
                else:
                    hashmap[WORD[i - self.letters_clicked]] = self.panel_list[i]

            for let in hashmap:
                if let == hashmap[let].text:
                    hashmap[let].color_main = (10, 240, 10)
                    for btn in self.keyboard_list:
                        if btn.text == let:
                            btn.color = (10, 240, 10)

                elif (let != hashmap[let].text):
                    if (hashmap[let].text in hashmap.keys()):
                        hashmap[let].color_main = (240, 240, 10)
                        for btn in self.keyboard_list:
                            if btn.text == hashmap[let].text:
                                if not btn.color == (10, 240, 10):
                                    btn.color = (240, 240, 10)

            if self.current_word == WORD:
                self.game_over = True

        if self.letters_clicked == 30:
            print(WORD)
            
    def run(self):
        self.keyboard()
        self.panels()

        Run = True
        while Run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if not self.game_over:
                        if self.back_btn.rect.collidepoint(pos):
                            self.letters_clicked -= 1
                            self.panel_list[self.letters_clicked].text = ""
                            
                            if self.letters_clicked < 0:
                                self.letters_clicked = 0

                        if self.enter_btn.rect.collidepoint(pos):
                            self.enter_clicked()

                        for btn in self.keyboard_list:
                            if btn.rect.collidepoint(pos):

                                btn.clicked = True

                                if self.letters_clicked < len(self.panel_list):
                                    self.panel_list[self.letters_clicked].text = btn.text

                                    self.letters_clicked += 1

            self.win.fill((30, 30, 30))

            for button in self.keyboard_list:
                button.draw(self.win)

            for panel in self.panel_list:
                panel.draw(self.win)

            self.back_btn.draw(self.win)
            self.enter_btn.draw(self.win)

            pygame.display.update()
            self.clock.tick(60)


M = Main()
M.run()