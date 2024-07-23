import pygame

pygame.init()
pygame.font.init()


class Box:
    def __init__(self, x, y):
        self.width = 130
        self.height = 130
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color_1 = (0,0,0)
        self.color = (255, 255, 255)
        self.rect_2 = pygame.Rect((self.x + 3), (self.y + 3), (self.width - 6), (self.height - 6))
        self.font = pygame.font.Font('freesansbold.ttf', 40)
        self.text_for_X = self.font.render("X", True, self.color_1)
        self.text_for_O = self.font.render("O", True, self.color_1)
        self.text_x = (self.x + self.width // 2 - 4)
        self.text_y = (self.y + self.height // 2 - 6)
        self.X_true = False
        self.O_true = False
        self.filled = False
        self.color_x_o = (255, 50, 80)
        self.color_draw = (40, 255, 60)

    def draw(self):
        self.rect = pygame.draw.rect(G.win, self.color_1, pygame.Rect(self.x, self.y, self.width, self.height))
        self.rect_2 = pygame.draw.rect(G.win, self.color, pygame.Rect((self.x + 3), (self.y + 3), (self.width - 6), (self.height - 6)))
        if G.X_Wins or G.O_Wins:
            self.rect_2 = pygame.draw.rect(G.win, self.color_x_o, pygame.Rect((self.x + 3), (self.y + 3), (self.width - 6), (self.height - 6)))

        if G.Is_Draw:
            self.rect_2 = pygame.draw.rect(G.win, self.color_draw, pygame.Rect((self.x + 3), (self.y + 3), (self.width - 6), (self.height -  6)))

        if self.X_true:
            G.win.blit(self.text_for_X, (self.text_x, self.text_y))

        if self.O_true:
            G.win.blit(self.text_for_O, (self.text_x, self.text_y))

    def check_Mouse_collision(self):
        if self.rect.collidepoint(G.pos):
            if G.mouse_down:
                G.mouse_click += 1
            if (G.mouse_click % 2 != 0):
                self.X_true = True
            else:
                self.O_true = True
            self.filled = True


class Game:
    def __init__(self):
        self.run = True
        self.width = self.height = 600
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (255, 255, 255)
        self.color_2 = (0, 0, 0)
        self.pos = (0, 0)
        self.board = [' ' for i in range(10)]
        self.mouse_click = 0
        self.X_Wins = False
        self.O_Wins = False
        self.Is_Draw = False
        self.font = pygame.font.Font('freesansbold.ttf', 40)
        self.mouse_down = False

    def checkWinner(self):
# Filling The Board with the letters #-----------------------------------------------------#
        if B_1.filled:
            if B_1.X_true:
                self.board[1] = 'X'
            if B_1.O_true:
                self.board[1] = 'O'

        if B_2.filled:
            if B_2.X_true:
                self.board[2] = 'X'
            if B_2.O_true:
                self.board[2] = 'O'

        if B_3.filled:
            if B_3.X_true:
                self.board[3] = 'X'
            if B_3.O_true:
                self.board[3] = 'O'

        if B_4.filled:
            if B_4.X_true:
                self.board[4] = 'X'
            if B_4.O_true:
                self.board[4] = 'O'

        if B_5.filled:
            if B_5.X_true:
                self.board[5] = 'X'
            if B_5.O_true:
                self.board[5] = 'O'

        if B_6.filled:
            if B_6.X_true:
                self.board[6] = 'X'
            if B_6.O_true:
                self.board[6] = 'O'

        if B_7.filled:
            if B_7.X_true:
                self.board[7] = 'X'
            if B_7.O_true:
                self.board[7] = 'O'

        if B_8.filled:
            if B_8.X_true:
                self.board[8] = 'X'
            if B_8.O_true:
                self.board[8] = 'O'

        if B_9.filled:
            if B_9.X_true:
                self.board[9] = 'X'
            if B_9.O_true:
                self.board[9] = 'O'
# Filling The Board with the letters #-----------------------------------------------------#

# Checking for The Winner #----------------------------------------------------------------#
        if (self.board[7] == 'X' and self.board[8] == 'X' and self.board[9] == 'X') or (self.board[4] == 'X' and self.board[5] == 'X' and self.board[6] == 'X') or (self.board[1] == 'X' and self.board[2] == 'X' and self.board[3] == 'X') or (self.board[1] == 'X' and self.board[4] == 'X' and self.board[7] == 'X') or (self.board[2] == 'X' and self.board[5] == 'X' and self.board[8] == 'X') or (self.board[3] == 'X' and self.board[6] == 'X' and self.board[9] == 'X') or (self.board[1] == 'X' and self.board[5] == 'X' and self.board[9] == 'X') or (self.board[3] == 'X' and self.board[5] == 'X' and self.board[7] == 'X'):
            self.X_Wins = True

        elif (self.board[7] == 'O' and self.board[8] == 'O' and self.board[9] == 'O') or (self.board[4] == 'O' and self.board[5] == 'O' and self.board[6] == 'O') or (self.board[1] == 'O' and self.board[2] == 'O' and self.board[3] == 'O') or (self.board[1] == 'O' and self.board[4] == 'O' and self.board[7] == 'O') or (self.board[2] == 'O' and self.board[5] == 'O' and self.board[8] == 'O') or (self.board[3] == 'O' and self.board[6] == 'O' and self.board[9] == 'O') or (self.board[1] == 'O' and self.board[5] == 'O' and self.board[9] == 'O') or (self.board[3] == 'O' and self.board[5] == 'O' and self.board[7] == 'O'):
            self.O_Wins = True
    
        else:
            if self.board.count(' ') == 1:
               self.Is_Draw = True

# Checking for The Winner #----------------------------------------------------------------#

    def draw_text(self):
        if self.X_Wins:
            self.text = G.font.render("X Wins!", True, self.color_2, G.color)
            self.text_rect = self.text.get_rect()
            self.text_rect.center = (300, 50)
            G.win.blit(self.text, self.text_rect)

        if self.O_Wins:
            self.text_2 = G.font.render("O Wins!", True, self.color_2, G.color)
            self.text_rect_2 = self.text_2.get_rect()
            self.text_rect_2.center = (300, 50)
            G.win.blit(self.text_2, self.text_rect_2)

        if self.Is_Draw:
            self.text_3 = G.font.render("It's a tie!", True, self.color_2, G.color)
            self.text_rect_3 = self.text_3.get_rect()
            self.text_rect_3.center = (300, 50)
            G.win.blit(self.text_3, self.text_rect_3)

    def Run(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.mouse_click = 0

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        self.mouse_down = True

# Checking Collision # ----------------------------------------------------------------#                   
                    B_1.check_Mouse_collision()
                    B_2.check_Mouse_collision()
                    B_3.check_Mouse_collision()
                    B_4.check_Mouse_collision()
                    B_5.check_Mouse_collision()
                    B_6.check_Mouse_collision()
                    B_7.check_Mouse_collision()
                    B_8.check_Mouse_collision()
                    B_9.check_Mouse_collision()
# Checking Collision # ----------------------------------------------------------------#

            self.win.fill(self.color)

# Drawing Boxes # ----------------------------------------------------------------#
            B_1.draw()
            B_2.draw()
            B_3.draw()
            B_4.draw()
            B_5.draw()
            B_6.draw()
            B_7.draw()
            B_8.draw()
            B_9.draw()
# Drawing Boxes # ----------------------------------------------------------------#
   
            G.checkWinner()
            G.draw_text()
            self.clock.tick(30)
            pygame.display.update()



# Making multiple Boxes # ----------------------------------------------------------------#
B_1 = Box(100, 100)
B_2 = Box(235, 100)
B_3 = Box(370, 100)
B_4 = Box(100, 235)
B_5 = Box(235, 235)
B_6 = Box(370, 235)
B_7 = Box(100, 370)
B_8 = Box(235, 370)
B_9 = Box(370, 370)
# Making multiple Boxes # ----------------------------------------------------------------#
G = Game()
G.Run()

