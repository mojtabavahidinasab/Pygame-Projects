'''
Assets from techwithtim.
Running this code with these images will get you this warning: (libpng warning: iCCP: known incorrect sRGB profile).
Only single words compatible with this code.
The words are names of characters of a popular indian show, TMKOC.
'''

from pygame import *
import pygame
import random
import pygame.mixer
import time

pygame.init()
mixer.init()

mixer.music.load("Pygame-Projects/Hangman/click.wav")
mixer.music.set_volume(0.9)

words = ['JETHALAL', 'DAYA', 'CHAMPAKLAL', 'TAPU', 'MEHTA', 'ANJALI', 'BHIDE', 'SONU', 'MADHVI', 'POPATLAL', 'ABDUL', 'ROSHAN', 'GOGI', 'PINKU', 'KOMAL', 'HATHI', 'GOLI', 'IYER', 'BABITA', 'NATU', 'BAGHA', 'BAWRI']

images = [pygame.image.load("Pygame-Projects/Hangman/images/hangman0.png"), pygame.image.load("Pygame-Projects/Hangman/images/hangman1.png"),pygame.image.load("Pygame-Projects/Hangman/images/hangman2.png"), pygame.image.load("Pygame-Projects/Hangman/images/hangman3.png"), pygame.image.load("Pygame-Projects/Hangman/images/hangman4.png"), pygame.image.load("Pygame-Projects/Hangman/images/hangman5.png"), pygame.image.load("Pygame-Projects/Hangman/images/hangman6.png")]

class Button:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter.upper()
        self.radius = 20
        self.visible = True

    def draw(self):
        if self.visible:
            pygame.draw.circle(M.win, (0, 0, 0), (self.x, self.y), self.radius, width=3)
            self.text = M.font.render(format(self.letter), True, (0, 0, 0), M.color)
            self.text_rect = self.text.get_rect(center = (self.x - 1, self.y - 1))
            M.win.blit(self.text, self.text_rect)

    def clicked(self):
        if M.mousedown:
            if M.pos[0] >= (self.x - self.radius) and M.pos[0] <= (self.x + self.radius):
                if M.pos[1] >= (self.y - self.radius) and M.pos[1] <= (self.y + self.radius):
                    self.visible = False
                    if self.letter in M.word:
                        indices = [i for i, let in enumerate(M.word) if let == self.letter]
                        for index in indices:
                            M.str[index] = self.letter
                            M.update_str()
                    else:
                        M.lives -= 1

class Main:
    def __init__(self):
        self.width, self.height = 800, 540
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (250, 250, 250)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 20)
        self.text_font = pygame.font.SysFont("arial", 60)
        self.pos = (0, 0)
        self.mousedown = False
        self.lives = 7
        self.word = random.choice(words)
        self.str = ["_" for i in range(len(self.word))]
        self.display_str = " ".join(self.str)

    def draw_text(self):
        self.word_txt = self.text_font.render(format(self.display_str), True, (0, 0, 0), self.color)
        self.win.blit(self.word_txt, (20, 100))
        self.lives_text = self.text_font.render("Lives: " + format(self.lives), True, (0, 0, 0), self.color)
        self.win.blit(self.lives_text, (20, 20))

    def draw_after_death(self):
        self.txt = self.text_font.render("You Died!", True, (0, 0, 0), self.color)
        self.txt_rect = self.txt.get_rect(center = (400, 380))
        self.win.blit(self.txt, self.txt_rect)

        self.word_txt = self.text_font.render("The word was: " + format(self.word), True, (0, 0, 0), self.color)
        self.word_rect = self.word_txt.get_rect(center = (400, 460))
        self.win.blit(self.word_txt, self.word_rect)

    def draw_after_win(self):
        self.text = self.text_font.render("You Won!", True, (0, 0, 0), self.color)
        self.text_rect = self.text.get_rect(center = (400, 300))
        self.win.blit(self.text, self.text_rect)

    def blit(self, img):
        self.win.blit(pygame.transform.scale(img, (192, 192)), (550, 100))   

    def check_win(self):
        if "".join(self.str) == self.word:
            self.draw_after_win()
            for button in Buttons:
                button.visible = False
            mixer.music.stop()

    def draw_images(self):
        if self.lives == 6:
            self.blit(images[0])
        elif self.lives == 5:
            self.blit(images[1])
        elif self.lives == 4:
            self.blit(images[2])
        elif self.lives == 3:
            self.blit(images[3])
        elif self.lives == 2:
            self.blit(images[4])
        elif self.lives == 1:
            self.blit(images[5])
        elif self.lives == 0:
            self.blit(images[6])

    def stop_game(self):
        if self.lives == 0:
            for button in Buttons:
                button.visible = False
            self.draw_after_death()
            mixer.music.stop()

    def update_str(self):
        self.display_str = " ".join(self.str)

    def run(self):
        Run = True
        while Run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mousedown = True
                    self.pos = pygame.mouse.get_pos()
                    for button in Buttons:
                        button.clicked()
                        mixer.music.play()
                    

            self.win.fill(self.color)
            for button in Buttons:
                button.draw()
            self.draw_text()
            self.stop_game()
            self.draw_images()
            self.check_win()
            pygame.display.update()
            self.clock.tick(60)

M = Main()
Buttons = [Button(20, 450, "a"), Button(80, 450, "b"), Button(140, 450, "c"), Button(200, 450, "d"), Button(260, 450, "e"), Button(320, 450, "f"), Button(380, 450, "g"), Button(440, 450, "h"), Button(500, 450, "i"), Button(560, 450, "j"), Button(620, 450, "k"), Button(680, 450, "l"), Button(740, 450, "m"), Button(40, 500, "n"), Button(100, 500, "o"), Button(160, 500, "p"), Button(220, 500, "q"), Button(280, 500, "r"), Button(340, 500, "s"), Button(400, 500, "t"), Button(460, 500, "u"), Button(520, 500, "v"), Button(580, 500, "w"), Button(640, 500, "x"), Button(700, 500, "y"), Button(760, 500, "z")]
M.run()