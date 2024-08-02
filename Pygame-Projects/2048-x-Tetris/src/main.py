import pygame
import random

pygame.init()

from block import Block

class App:
    def __init__(self):
        self.width, self.height = 600, 750
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (255, 150, 150)
        self.block_list = []
        self.falling_list = []
        self.time_since_last_generation = pygame.time.get_ticks()
        self.time_difference = 2000

    def load_initial_block(self):
        for _ in range(6):
            block = Block([2, 3, 4, 5, 6, 7][_] * 75, random.choice([8, 9]) * 75)
            block.falling = False
            self.block_list.append(block)

    def check_collision(self):
        for block_ in self.block_list:
            for block in self.falling_list:
                if block.x == block_.x:
                    if block.y + block.height == block_.y:
                        block.falling = False
                        block.y == block_.y - block.height
                        self.falling_list.remove(block)
                        self.block_list.append(block)
                        break


                if block.y >= self.height - block.height:
                    block.falling = False
                    block.y = self.height - block.height
                    self.falling_list.remove(block)
                    self.block_list.append(block)
                    break

    def delete_extra(self):
        for block in self.block_list:
            if not block.falling and block.y == 75:
                self.block_list.remove(block)

    def can_move(self, block_, direction):

        target_x = (block_.x + (75 * direction))

        if target_x < 0 or target_x >= self.width:
            return False
        
        for block in self.block_list:
            if block.x == target_x and block.y == block_.y:
                return False
            
        return True

    def merge(self):
        for block_ in self.block_list:
            for block in self.block_list:
                if not block == block_:
                    if block.x == block_.x and (block.y == block_.y - block.height or block_.y == block.y - block.height) and (block.value[0] == block_.value[0]):
                        self.block_list.remove(block)
                        pygame.time.wait(50)
                        block_.value[0] *= 2
                        block_.update_color()

                    elif block.y == block_.y and (block.x == block_.x - block.width or block_.x == block.x - block.width) and (block.value[0] == block_.value[0]):
                        self.block_list.remove(block)
                        pygame.time.wait(50)
                        block_.value[0] *= 2
                        block_.update_color()

    def main_function(self):

        self.load_initial_block()

        Running = True
        while Running:

            self.current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False

                if event.type == pygame.KEYDOWN:
                    if len(self.falling_list) > 0:
                        block_to_change = self.falling_list[len(self.falling_list)  - 1]
                        if event.key == pygame.K_LEFT and self.can_move(block_to_change, -1):
                            block_to_change.x -= 75
                        if event.key == pygame.K_RIGHT and self.can_move(block_to_change, 1):
                            block_to_change.x += 75

            self.draw()

            if self.current_time - self.time_since_last_generation >= self.time_difference:
                new_block = Block(random.choice([0, 1, 2, 3, 4]) * 75, -25)
                self.falling_list.append(new_block)
                self.time_since_last_generation = self.current_time

    def draw(self):

        self.win.fill(self.color)

        for block in self.falling_list:
            block.draw(self.win)

        for block in self.block_list:
            block.draw(self.win)

        self.merge()

        self.delete_extra()
        self.check_collision()

        pygame.draw.line(self.win, (0, 0, 0), (0, 150), (self.width, 150), 5)

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    App().main_function()