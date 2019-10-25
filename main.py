import pygame
import time

from food.food import Food
from setting.setting import Setting
import setting.game_functions as gf
from snake.snake import Snake


def run_game():
    # 游戏配置信息
    game_setting = Setting()

    # 初始化游戏，并创建一个屏幕对象
    pygame.init()
    fps_clock = pygame.time.Clock()
    # 图标
    icon = pygame.image.load("res/snake.png")
    screen = pygame.display.set_mode(
        [game_setting.screen_width, game_setting.screen_width]
    )
    pygame.display.set_caption("Greedy Snake")
    pygame.display.set_icon(icon)

    # 创建一条蛇
    snake = Snake(game_setting, screen)
    # 创建一个食物
    food = Food(game_setting, screen, snake)

    # 游戏的主循环
    while True:
        gf.keyboard_listener(game_setting, snake)

        snake.update()

        gf.snake_eat_food(snake, food)

        gf.update_screen(game_setting, screen, snake, food)
        fps_clock.tick(game_setting.snake_speed)


run_game()
