import pygame
from pygame.rect import Rect
from pygame.sprite import Sprite


class Snake(Sprite):
    def __init__(self, game_setting, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.setting = game_setting

        self.snakePosition = [20, 0]
        self.snakeSegments = [[20, 0], [10, 0], [0, 0]]

        self.head_color = game_setting.snake_head_color
        self.body_color = game_setting.snake_body_color

        self.width = game_setting.block_width
        self.height = game_setting.block_height

        # 移动标志
        self.moving_right = True
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.count = 0

    def update_position(self):
        self.count += 1
        self.snakeSegments.insert(0, list(self.snakePosition))
        self.snakeSegments.pop()

    def update(self):
        if self.moving_left and not self.moving_right and self.snakePosition[0] > 0:
            self.snakePosition[0] -= self.setting.snake_speed_factor
            self.update_position()
        if self.moving_right and not self.moving_left \
                and self.snakePosition[0] < (self.screen_rect.right - self.setting.block_width):
            self.snakePosition[0] += self.setting.snake_speed_factor
            self.update_position()
        if self.moving_up and not self.moving_down and self.snakePosition[1] > 0:
            self.snakePosition[1] -= self.setting.snake_speed_factor
            self.update_position()
        if self.moving_down and not self.moving_up \
                and self.snakePosition[1] < (self.screen_rect.bottom - self.setting.block_height):
            self.snakePosition[1] += self.setting.snake_speed_factor
            self.update_position()

    def blit_snake(self):
        for snakeSegment in self.snakeSegments[1:]:
            rect = Rect(snakeSegment[0], snakeSegment[1], self.width, self.height)
            pygame.draw.rect(self.screen, self.body_color, rect)

        head_rect = Rect(self.snakePosition[0], self.snakePosition[1], self.width, self.height)
        pygame.draw.rect(self.screen, self.head_color, head_rect)

    def eat_food(self):
        self.snakeSegments.insert(0, list(self.snakePosition))
