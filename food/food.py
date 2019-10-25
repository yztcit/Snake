# _*_ coding: UTF-8 _*_
import random

import pygame

from pygame.sprite import Sprite


class Food(Sprite):

    def __init__(self, game_setting, screen, snake):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.max_x = (self.screen_rect.right - game_setting.block_width) / 10
        self.max_y = (self.screen_rect.bottom - game_setting.block_height) / 10

        self.color = game_setting.food_color

        # 在(0, 0)处创建一个食物，再调整其位置
        self.pos = [0, 0]
        self.pos[0] = snake.snakePosition[0] + len(snake.snakeSegments) * game_setting.block_width
        self.width = game_setting.block_width
        self.height = game_setting.block_height
        self.rect = pygame.Rect(
            self.pos[0], self.pos[1],
            self.width, self.height
        )

    def blit_food(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def random_food(self):
        x = random.randrange(1, self.max_x)
        y = random.randrange(1, self.max_y)
        self.pos = [int(x * 10), int(y * 10)]

    def update(self):
        self.random_food()
        self.rect = pygame.Rect(
            self.pos[0], self.pos[1],
            self.width, self.height
        )
