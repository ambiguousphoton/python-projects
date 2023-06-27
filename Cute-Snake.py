import pygame
import time
import random
from enum import Enum
from collections import namedtuple

pygame.init()

class Directions(Enum):
    RIGHT  = 1
    LEFT   = 2
    UP     = 3
    DOWN   = 4

Point = namedtuple('Point', 'x', 'y')

BLOCK = 20
class Snake_Game:
    def __init__(self, w = 500, h = 500):
        self.w = w
        self.h = h
        self.dispaly = pygame.display.set_mode(self.w, self.h)
        pygame.display.set_caption("Cute Snake")
        self.Clock = pygame.time.Clock()

        self.direction = Directions.RIGHT
        self.head = Point(self.w//2, self.h//2)
        self.snake = [self.head, Point(self.head.x - BLOCK, self.head.y), 
                      Point(self.head.x - (2 * BLOCK), self.head.y)]

        self.score = 0
        self.food = None
        self.place_food()

    def place_food(self):
        x = (random.randint(0, self.w - BLOCK) // 3) * 3
        y = (random.randint(0, self.y - BLOCK) // 3) * 3
        self.food = Point(x, y)
        if self.food in self.snake:
            self.place_food()

    def play_step(self):
        game_over = False
        return game_over, self.score

if __name__ == '__main__':
    game = Snake_Game()

    while True:
        game_over, score = game.play_step()

        if game_over == True:
            break
 
    pygame.quit()