class Setting():
    def __init__(self):
        # display screen size
        self.screen_width = 720
        self.screen_height = 960
        # bgColor
        self.bg_color = (0, 0, 0)

        self.block_width = 10
        self.block_height = 10
        # food params
        self.food_color = (255, 0, 0)
        # snake params
        self.snake_head_color = (255, 255, 255)
        self.snake_body_color = (155, 155, 155)

        self.snake_speed = 2

        self.snake_speed_factor = 10
        # 加快游戏节奏
        self.speedup_scale = 10
        # 得分随节奏加快提高
        self.score_scale = 1.5

    def accelerate_speed(self):
        if self.snake_speed < 60:
            self.snake_speed *= self.speedup_scale

    def init_dynamic_speed(self):
        self.snake_speed = 1
