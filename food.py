# _*_ coding: UTF-8 _*_
from pygame.sprite import Sprite


class Food(Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def blit(self):
        self.screen.blit(self)
