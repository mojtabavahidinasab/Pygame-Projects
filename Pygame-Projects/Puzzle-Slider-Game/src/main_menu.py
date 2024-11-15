import pygame
from cell import Cell

def load_cells():

    texts = ["3x3", "4x4", "5x5", "6x6"]

    cells = []

    for idx, text in enumerate(texts):
        cells.append(Cell(200, (20 + (120 * idx)), 100, 100, text))

    return cells

def main_menu(win, width, height, color):

    RUNNING = True
    GAME_RUNNING = False
    NUM = 0

    cell_list = load_cells()

    while RUNNING:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                NUM = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for cell in cell_list:
                    if cell.rect.collidepoint(pos):
                        RUNNING = False
                        GAME_RUNNING = True
                        text = cell.value.split("x")
                        NUM = int(text[0])

        win.fill(color)

        for cell in cell_list:
            cell.draw(win)

        pygame.display.update()
        pygame.time.Clock().tick(60)
    
    return GAME_RUNNING, NUM


    