import pygame, math

pygame.init()

class Buttons:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.width =  self.height = 50
        self.color = (240, 240, 240)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):

        self.rect = pygame.draw.rect(A.win, self.color, pygame.Rect(self.x, self.y, self.width, self.height), 2, 2, 2, 2)

        self.num_text = A.text.render(format(self.value), True, self.color, A.color)
        self.num_text_rect = self.num_text.get_rect()
        self.num_text_rect.center = ((self.x + 24), (self.y + 24))
        A.win.blit(self.num_text, self.num_text_rect)

class Add_button:
    def __init__(self):
        self.x = 200
        self.y = 110
        self.width = 50
        self.height = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_visible = None
        self.add_pressed = False

    def draw(self):
        self.rect = pygame.draw.rect(A.win, (240, 240, 240), pygame.Rect(self.x, self.y, self.width, self.height), 2, 2, 2, 2)
        self.text = A.text.render("+", True, (240, 240, 240), A.color)
        self.text_rext = self.text.get_rect()
        self.text_rext.center = (self.x + 24, self.y + 48)
        A.win.blit(self.text, self.text_rext)


        if self.rect.collidepoint(A.pos):
            self.is_visible = True
            A.num_1_full = True
            self.add_pressed = True

        if self.is_visible:
            if not E.invisible:
                A.win.blit(self.text, (175, 30))
           
class Subtract_button:
    def __init__(self):
        self.x = 260
        self.y = 110
        self.width = 50
        self.height = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_visible = None
        self.subtract_pressed = False

    def draw(self):
        self.rect = pygame.draw.rect(A.win, (240, 240, 240), pygame.Rect(self.x, self.y, self.width, self.height), 2, 2, 2, 2)
        self.text = A.text.render("-", True, (240, 240, 240), A.color)
        self.text_rext = self.text.get_rect()
        self.text_rext.center = (self.x + 24, self.y + 48)
        A.win.blit(self.text, self.text_rext)


        if self.rect.collidepoint(A.pos):
                self.is_visible = True
                A.num_1_full = True
                self.subtract_pressed = True
            
        if self.is_visible:
            if not E.invisible:
                A.win.blit(self.text, (175, 30))

class Multiply_button:
    def __init__(self):
        self.x = 320
        self.y = 110
        self.width = 50
        self.height = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_visible = None
        self.product_pressed = False

    def draw(self):
        self.rect = pygame.draw.rect(A.win, (240, 240, 240), pygame.Rect(self.x, self.y, self.width, self.height), 2, 2, 2, 2)
        self.text = A.text.render("*", True, (240, 240, 240), A.color)
        self.text_rext = self.text.get_rect()
        self.text_rext.center = (self.x + 24, self.y + 48)
        A.win.blit(self.text, self.text_rext)


        if self.rect.collidepoint(A.pos):
                self.is_visible = True
                A.num_1_full = True
                self.product_pressed = True
            

    
        if self.is_visible:
            if not E.invisible:
                A.win.blit(self.text, (175, 30))

class Divide_button:
    def __init__(self):
        self.x = 200
        self.y = 220
        self.width = 170
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_visible = None
        self.divide_pressed = False

    def draw(self):
        self.rect = pygame.draw.rect(A.win, (240, 240, 240), pygame.Rect(self.x, self.y, self.width, self.height), 2, 2, 2, 2)
        self.text = A.text.render("/", True, (240, 240, 240), A.color)
        self.text_rext = self.text.get_rect()
        self.text_rext.center = (self.x + 85, self.y + 24)
        A.win.blit(self.text, self.text_rext)


        if self.rect.collidepoint(A.pos):
                self.is_visible = True
                A.num_1_full = True

    
        if self.is_visible:
            if not E.invisible:
                A.win.blit(self.text, (175, 30))

class Enter:
    def __init__(self):
        self.x = 200
        self.y = 290
        self.width = 170
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.invisible = False

    def draw(self):
        self.rect = pygame.draw.rect(A.win, (240, 240, 240), pygame.Rect(self.x, self.y, self.width, self.height), 2, 2, 2,2) 
        self.text = A.text.render("Enter", True, (240, 240, 240), A.color)
        self.text_rext = self.text.get_rect()
        self.text_rext.center = (self.x + 80, self.y + 24)
        A.win.blit(self.text, self.text_rext)


        if self.rect.collidepoint(A.pos):
            self.invisible = True
            if Add.add_pressed == False and Subtract.subtract_pressed == False and Product.product_pressed == False:
                Divide.divide_pressed = True

class Clear:
    def __init__(self):
        self.x = 200
        self.y = 350
        self.width = 170
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.invisible = False

    def draw(self):
        self.rect = pygame.draw.rect(A.win, (240, 240, 240), pygame.Rect(self.x, self.y, self.width, self.height), 2, 2, 2,2) 
        self.text = A.text.render("C", True, (240, 240, 240), A.color)
        self.text_rext = self.text.get_rect()
        self.text_rext.center = (self.x + 80, self.y + 24)
        A.win.blit(self.text, self.text_rext)


        if self.rect.collidepoint(A.pos):
            A.num_1 = "0"
            A.num_2 = "0"
            A.num_1_full = False
            Add.add_pressed = False
            Add.is_visible = False
            Subtract.subtract_pressed = False
            Subtract.is_visible = False
            Product.product_pressed = False
            Product.is_visible = False
            Divide.divide_pressed = False
            Divide.is_visible = False
            E.invisible = False

class App:
    def __init__(self):
        self.width = 400
        self.height = 410
        self.win = pygame.display.set_mode((self.width, self.height))
        self.title = pygame.display.set_caption("Calculator!")
        self.Run = True
        self.color = (110, 110, 110)
        self.box_x = self.box_y = 20
        self.num_rect = pygame.Rect(self.box_x, self.box_y, 360, 60)
        self.text = pygame.font.Font(pygame.font.get_default_font(), 30)
        self.num_1 = "0"
        self.num_2 = "0"
        self.pos = (0, 0)
        self.num_1_full = False
        self.num_1_float =  0
        self.num_2_float =  0
        self.ans = 0

    def draw(self):
        self.num_rect = pygame.draw.rect(self.win, (250, 250, 250), pygame.Rect(self.box_x, self.box_y, 360, 60), 2, 2, 2, 2)
        
        if not E.invisible:
            self.num_text_1 = A.text.render(format(self.num_1), True, (240, 240, 240), self.color)
            self.num_text_1_rect = self.num_text_1.get_rect()
            self.num_text_1_rect.center = (75, 50)
            self.win.blit(self.num_text_1, self.num_text_1_rect)

            self.num_text_2 = A.text.render(format(self.num_2), True, (240, 240, 240), self.color)
            self.num_text_2_rect = self.num_text_2.get_rect()
            self.num_text_2_rect.center = (300, 50)
            self.win.blit(self.num_text_2, self.num_text_2_rect)

    def handle_calculations(self):
        self.num_1_float = float(self.num_1)
        self.num_2_float = float(self.num_2)

        if Add.add_pressed:
            self.ans = self.num_1_float + self.num_2_float
        
        if Subtract.subtract_pressed:
            self.ans =  self.num_1_float - self.num_2_float

        if Product.product_pressed:
            self.ans =  self.num_1_float * self.num_2_float

        if Divide.divide_pressed:
            self.ans =  self.num_1_float / self.num_2_float

        if E.invisible:
            self.ans_text = A.text.render(format(self.ans), True, (240, 240, 240), self.color)
            self.ans_text_rect = self.ans_text.get_rect()
            self.ans_text_rect.center = (200, 50)
            self.win.blit(self.ans_text, self.ans_text_rect)

    def main(self):
        while self.Run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.Run =  False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()


                    if B_1.rect.collidepoint(self.pos):
                        if not self.num_1_full:
                            self.num_1 += B_1.value
                        else:
                            self.num_2 += B_1.value

                    if B_2.rect.collidepoint(self.pos):
                        if not self.num_1_full:
                            self.num_1 += B_2.value
                        else:
                            self.num_2 += B_2.value

                    if B_3.rect.collidepoint(self.pos):
                        if not self.num_1_full:
                            self.num_1 += B_3.value
                        else:
                            self.num_2 += B_3.value

                    if B_4.rect.collidepoint(self.pos):
                        if not self.num_1_full:
                            self.num_1 += B_4.value
                        else:
                            self.num_2 += B_4.value

                    if B_5.rect.collidepoint(self.pos):
                        if not self.num_1_full:
                            self.num_1 += B_5.value
                        else:
                            self.num_2 += B_5.value

                    if B_6.rect.collidepoint(self.pos):
                        if not self.num_1_full:
                            self.num_1 += B_6.value
                        else:
                            self.num_2 += B_6.value

                    if B_7.rect.collidepoint(self.pos):
                        if not self.num_1_full:
                            self.num_1 += B_7.value
                        else:
                            self.num_2 += B_7.value

                    if B_8.rect.collidepoint(self.pos):
                        if not self.num_1_full:
                            self.num_1 += B_8.value
                        else:
                            self.num_2 += B_8.value

                    if B_9.rect.collidepoint(self.pos):
                        if not self.num_1_full:
                            self.num_1 += B_9.value
                        else:
                            self.num_2 += B_9.value

                    if B_dot.rect.collidepoint(self.pos):
                        if not self.num_1_full:
                            self.num_1 += B_dot.value
                        else:
                            self.num_2 += B_dot.value

                    if B_0.rect.collidepoint(self.pos):
                        if not self.num_1_full:
                            self.num_1 += B_0.value
                        else:
                            self.num_2 += B_0.value

            self.win.fill(self.color)
            A.draw()
            B_1.draw()
            B_2.draw()
            B_3.draw()
            B_4.draw()
            B_5.draw()
            B_6.draw()
            B_7.draw()
            B_8.draw()
            B_9.draw()
            B_0.draw()
            B_dot.draw()
            Add.draw()
            Subtract.draw()
            Product.draw()
            Divide.draw()
            E.draw()
            A.handle_calculations()
            C.draw()
            pygame.display.update()

            

A =  App()
B_1 = Buttons(20, 110, "1")
B_2 = Buttons(80, 110, "2")
B_3 = Buttons(140, 110, "3")
B_4 = Buttons(20, 170, "4")
B_5 = Buttons(80, 170, "5")
B_6 = Buttons(140, 170, "6")
B_7 = Buttons(20, 230, "7")
B_8 = Buttons(80, 230, "8")
B_9 = Buttons(140, 230, "9")
B_0 = Buttons(50, 290, "0")
B_dot = Buttons(110, 290, ".")
Add = Add_button()
Subtract = Subtract_button()
Product = Multiply_button()
Divide = Divide_button()
E = Enter()
C = Clear() 
A.main()