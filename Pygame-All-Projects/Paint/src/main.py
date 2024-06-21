import pygame

pygame.init()

from pixel import Pixel
from color_buttons import ColorButton
from utility_btns import UtilityBtn

class Window:
    def __init__(self):
        self.width, self.height = 700, 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.surface_width, self.surface_height = 500, 500
        self.Run = True
        self.pixel_list = []
        self.pixel_width, self.pixel_height = 5, 5
        self.previous_pixel_width, self.previous_pixel_height = 0, 0
        self.pixels_x = self.surface_width//self.pixel_width
        self.pixels_y = self.surface_height//self.pixel_height
        self.initial_x = (self.width - self.surface_width)//2
        self.initial_y = (self.height - self.surface_height)//2
        self.drawing = False
        self.mouse_color = (10, 10, 10)
        self.brush = True
        self.mirror = False
        self.clear = False
        self.color_btn_list = []
        self.change_size = False
        self.utility_buttons_list = []
        self.value_of_pixel = 5
        self.change_btns = []
        self.font = pygame.font.SysFont('monospace', 20)

    def fill_pixels(self):

        for i in range(self.pixels_x):
            for j in range(self.pixels_y):
                pixel = Pixel((self.initial_x + (i * self.pixel_width)), (self.initial_y + (j * self.pixel_height)), self.pixel_width, self.pixel_height)

                self.pixel_list.append(pixel)

    def change_pixel_size(self):

        #if (self.pixel_width != self.previous_pixel_width):

            self.pixel_width = self.value_of_pixel
            self.pixel_height = self.value_of_pixel

            self.pixels_x = (self.surface_width//self.pixel_width)
            self.pixels_y = (self.surface_height//self.pixel_height)

            self.surface_width = self.pixels_x * self.pixel_width
            self.surface_height = self.pixels_y * self.pixel_height

            self.initial_x = (self.width - self.surface_width) // 2
            self.initial_y = (self.height - self.surface_height) // 2

            self.pixel_list.clear()

            for i in range(self.pixels_x):
                for j in range(self.pixels_y):
                    pixel = Pixel((self.initial_x + (i * self.pixel_width)), (self.initial_y + (j * self.pixel_height)), self.pixel_width, self.pixel_height)
                    self.pixel_list.append(pixel)

    def size_change_buttons(self):
        
        pygame.draw.rect(self.win, (0, 0, 0), pygame.Rect(330, 625, 40, 40), 5, 5, 5, 5)
        
        text = self.font.render(format(self.value_of_pixel), True, (0, 0, 0))
        rect = text.get_rect(center = (350, 640))
        self.win.blit(text, rect)

        IncrementButton = UtilityBtn(270, 625, "+")
        DecrementButton = UtilityBtn(390, 625, "-")

        self.change_btns.append(IncrementButton)
        self.change_btns.append(DecrementButton)

    def color_buttons(self):

        color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (0, 0, 0), (255, 255, 255)]
        
        for i in range(4):
            for j in range(2):
                btn = ColorButton((self.surface_width + 100 + 4  + (i * 24)), (100 + (j * 24)), (0, 0, 0))
                self.color_btn_list.append(btn)

        for btn in self.color_btn_list:
            btn.color = color_list[self.color_btn_list.index(btn)]

    def utility_buttons(self):

        text = ["Erase", "Mirror", "Clear", "Size"]
        
        for i in range(2):
            for j in range(2):
                btn = UtilityBtn((self.surface_width + 106 + (i * 46)), (150 + (j * 46)), "")
                self.utility_buttons_list.append(btn)

        for btn in self.utility_buttons_list:
            btn.text = text[self.utility_buttons_list.index(btn)]

    def clear_srcn(self):

        for pixel in self.pixel_list:
            pixel.color = (255, 255, 255)
            pixel.previous_color = (255, 255, 255)

    def get_mirror_pixel(self, pixel):

        center = (self.width)//2

        mirror_pixel = None
    
        if pixel.x < center:
            distance = pixel.x - (self.initial_x)

            mirror_pixel_x = (self.initial_x + self.surface_width) - distance - self.pixel_width

            for pixl in self.pixel_list:
                if pixl.x == mirror_pixel_x:
                    if pixl.y == pixel.y:
                        mirror_pixel = pixl

        elif pixel.x >= center:

            distance = (self.initial_x + self.surface_width) - pixel.x - self.pixel_width

            mirror_pixel_x = (self.initial_x + distance)

            for pixl in self.pixel_list:
                if pixl.x == mirror_pixel_x:
                    if pixl.y == pixel.y:
                        mirror_pixel = pixl

        return mirror_pixel
            
    def main(self):

        self.fill_pixels()
        self.color_buttons()
        self.utility_buttons()

        while self.Run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.drawing = True
                    pos = pygame.mouse.get_pos()

                    if self.change_btns[0].rect.collidepoint(pos):
                        if self.value_of_pixel < 26:
                            self.value_of_pixel += 1

                    if self.change_btns[1].rect.collidepoint(pos):
                        if self.value_of_pixel > 4:
                            self.value_of_pixel -= 1

                    if self.utility_buttons_list[0].rect.collidepoint(pos):
                        self.brush = not self.brush

                    if self.utility_buttons_list[1].rect.collidepoint(pos):
                        self.mirror = not self.mirror

                    if self.utility_buttons_list[2].rect.collidepoint(pos):
                        self.clear_srcn()

                    if self.utility_buttons_list[3].rect.collidepoint(pos):
                        self.change_pixel_size()
                        self.previous_pixel_width = self.pixel_width

                    for btn in self.color_btn_list:
                        if btn.rect.collidepoint(pos):
                            self.mouse_color = btn.color

                if event.type == pygame.MOUSEBUTTONUP:
                    self.drawing = False

                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    for pixel in self.pixel_list:
                        if pixel.rect.collidepoint(pos):
                            if self.drawing:
                                if self.brush:
                                    pixel.previous_color = self.mouse_color
                                    pixel.color = self.mouse_color
                                    if self.mirror:
                                        mirror_pixel = self.get_mirror_pixel(pixel)
                                        if mirror_pixel:
                                            mirror_pixel.color = self.mouse_color
                                            mirror_pixel.previous_color = self.mouse_color
                                else:
                                    pixel.previous_color = (255, 255, 255)
                                    pixel.color = (255, 255, 255)
                            else:
                                pixel.color = (100, 100, 100, 200)
                        else:
                            pixel.color = pixel.previous_color
            
            self.win.fill((100, 100, 100))

            for pixel in self.pixel_list:
                pixel.draw(self.win)

            for btn in self.color_btn_list:
                btn.draw(self.win)

            for btn in self.utility_buttons_list:
                btn.draw(self.win)

            self.size_change_buttons()

            for btn in self.change_btns:
                btn.draw(self.win)

            pygame.display.update()
            pygame.time.Clock().tick(60)


W = Window()
W.main()