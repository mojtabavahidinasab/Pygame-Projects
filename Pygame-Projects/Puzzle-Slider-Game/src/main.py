import pygame, random

pygame.init()

from cell import Cell
from movement import handle_movement
from values import give_values
from main_menu import main_menu

BORDERS = 100

class App:
    def __init__(self):
        self.width, self.height = 500, 500
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (16, 16, 16)
        self.cell_list = None
        self.Running = False
        self.game_over = False
        self.win_label = Cell((self.width - 200)//2, 400, 200, 75, "Solved!")

    def load_cells(self, WIDTH, HEIGHT, LIST, NUM):

        start_x, start_y = BORDERS, 100

        PADDING = (((self.width - 2 * BORDERS) - (NUM * WIDTH)) // (NUM - 1)) + WIDTH

        for arr in LIST:
            random.shuffle(arr)

        random.shuffle(LIST)

        for i in range(NUM):
            for j in range(NUM):
                self.cell_list[i][j] = Cell((start_x + (j * PADDING)), (start_y + (i * (HEIGHT + 20))), WIDTH, HEIGHT, LIST[i][j])

    def get_values(self, NUM):

        values = []

        for i in range(NUM):
            for j in range(NUM):
                values.append(self.cell_list[i][j].value)

        return values

    def main_function(self):

        self.Running, NUM = main_menu(self.win, self.width, self.height, self.color)
        
        WIDTH, HEIGHT, LIST, FINAL = give_values(NUM)

        self.cell_list = [[0] * NUM for _ in range(NUM)]

        self.load_cells(WIDTH, HEIGHT, LIST, NUM)

        while self.Running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    for index, row in enumerate(self.cell_list):
                        for idx, cell in enumerate(row):
                            if cell.rect.collidepoint(pos):

                                if not self.game_over:
                                    handle_movement(self.cell_list, cell, index, idx, NUM)

                                if FINAL == self.get_values(NUM):
                                    self.game_over = True

            self.draw()

    def draw(self):

        self.win.fill(self.color)

        for row in self.cell_list:
            for cell in row:
                cell.draw(self.win)

        if self.game_over:
            self.win_label.draw(self.win)

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    App().main_function()