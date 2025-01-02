# Im making this game to practice one and only one thing. Writing as clean code as possible.
# I've made games far complicated in logic and code than this one. 
# Aim will be lines <= 200, excluding comments, and using the minimum amount of variables required.

# Looks I've succeeded in my goals, though I did take some help from "external sources".

from pygame import *
import pygame.mixer
from os.path import join
import random

pygame.init()
mixer.init()

mixer.music.load("./assets/sound.mp3")
mixer.music.set_volume(0.9)

pygame.display.set_caption("Rock-Paper-Scissors!")

def get_image(name):
    return pygame.transform.scale(pygame.image.load(join("./assets", name)), (192, 192))

class Button:
    def __init__(self, x, y, image, name):
        self.x, self.y = x, y
        self.width, self.height = 256, 256
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = image
        self.color, self.hover_color = (165, 194, 212), (102, 205, 170)
        self.name = name

    def draw_and_hover(self):
        pygame.draw.rect(A.win, self.color, pygame.Rect(self.x, self.y, self.width, self.height), border_radius=12)
        A.win.blit(self.image, (self.x + 32, self.y + 32))

        pos = pygame.mouse.get_pos()
        self.color = self.hover_color if self.rect.collidepoint(pos) else (165, 194, 212)

class App:
    def __init__(self):
        self.width, self.height = 800, 600
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (240, 240, 240)
        self.clock = pygame.time.Clock()
        self.Run = True
        self.pos, self.comp_choice, self.name_in_play, self.mouse_down = (0, 0), None, None, False
        self.Draw, self.Player_win, self.Comp_win = False, False, False
        self.font = pygame.font.Font("./assets/brightgear.otf", 48)

    def draw_text(self, text, pos):
        rendered_text = self.font.render(text, True, (0, 0, 0), self.color)
        self.win.blit(rendered_text, pos)

    def make_comp_move(self):
        move_probabilities = {'Rock': 0.4, 'Paper': 0.3, 'Scissors': 0.3}
        self.comp_choice = random.choices(list(move_probabilities.keys()), weights=move_probabilities.values())[0]

    def check_winner(self):
        choices = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}

        if self.mouse_down:
            if self.name_in_play == self.comp_choice:
                self.Draw, self.Player_win, self.Comp_win = True, False, False
            elif choices[self.name_in_play] == self.comp_choice:
                self.Player_win, self.Draw, self.Comp_win = True, False, False
            else:
                self.Comp_win, self.Draw, self.Player_win = True, False, False


    def draw_window(self):
        self.win.fill(self.color)
        for button in buttons:
            button.draw_and_hover()
        self.draw_text("Comp Played: " + format(self.comp_choice), (10, 300))
        self.draw_text("You Played: " + format(self.name_in_play), (10, 372))

        result_text = ''
        if self.Draw:
            result_text = "It's a Draw!"
        elif self.Player_win:
            result_text = "You Win!"
        elif self.Comp_win:
            result_text = "Comp Wins!"
        self.draw_text(result_text, (300, 480))

        pygame.display.update()
        self.clock.tick(60)

    def main(self):
        while self.Run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    self.mouse_down = True
                    mixer.music.play()

                    for i, button in enumerate(buttons):
                        if button.rect.collidepoint(self.pos):
                            self.make_comp_move()
                            self.name_in_play = button.name

            self.check_winner()
            self.draw_window()

A = App()
buttons = [Button(8, 10, get_image("stone.png"), "Rock"),
           Button(272, 10, get_image("paper.png"), "Paper"),
           Button(536, 10, get_image("scissors.png"), "Scissors")]

A.main()
