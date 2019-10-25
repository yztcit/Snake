import sys

import pygame


def confirm_direction(snake):
    if snake.moving_right:
        snake.moving_left = False
        snake.moving_up = False
        snake.moving_down = False
    if snake.moving_left:
        snake.moving_right = False
        snake.moving_up = False
        snake.moving_down = False
    if snake.moving_up:
        snake.moving_down = False
        snake.moving_left = False
        snake.moving_right = False
    if snake.moving_down:
        snake.moving_up = False
        snake.moving_left = False
        snake.moving_right = False


def check_keydown_events(event, game_setting, snake):
    if event.key == pygame.K_RIGHT and not snake.moving_left:
        snake.moving_right = True
        snake.moving_up = False
        snake.moving_down = False
        game_setting.accelerate_speed()
    elif event.key == pygame.K_LEFT and not snake.moving_right:
        snake.moving_left = True
        snake.moving_up = False
        snake.moving_down = False
        game_setting.accelerate_speed()
    elif event.key == pygame.K_UP and not snake.moving_down:
        snake.moving_up = True
        snake.moving_left = False
        snake.moving_right = False
        game_setting.accelerate_speed()
    elif event.key == pygame.K_DOWN and not snake.moving_up:
        snake.moving_down = True
        snake.moving_left = False
        snake.moving_right = False
        game_setting.accelerate_speed()


def check_keyup_events(event, game_setting, snake):
    # 长按方向加速，松开减速
    if event.key == pygame.K_RIGHT:
        confirm_direction(snake)
        game_setting.init_dynamic_speed()
    elif event.key == pygame.K_LEFT:
        confirm_direction(snake)
        game_setting.init_dynamic_speed()
    elif event.key == pygame.K_UP:
        confirm_direction(snake)
        game_setting.init_dynamic_speed()
    elif event.key == pygame.K_DOWN:
        confirm_direction(snake)
        game_setting.init_dynamic_speed()

    elif event.key == pygame.K_ESCAPE:
        game_over()


def keyboard_listener(game_setting, snake):
    for event in pygame.event.get():
        # 点击右上角 x 退出
        if event.type == pygame.QUIT:
            game_over()
        # 检测鼠标点击
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_setting, snake)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, game_setting, snake)


def snake_eat_food(snake, food):
    if snake.snakePosition[0] == food.pos[0] and snake.snakePosition[1] == food.pos[1]:
        snake.eat_food()
        food.update()


def update_screen(game_setting, screen, snake, food):
    """更新屏幕上的图像，并刷新"""
    # 每次循环时都重新绘制屏幕
    screen.fill(game_setting.bg_color)

    # 在指定位置绘制蛇
    snake.blit_snake()

    # 在指定位置绘制食物
    food.blit_food()

    # 让最新绘制的屏幕可见
    pygame.display.flip()


def game_over():
    pygame.quit()
    sys.exit()
