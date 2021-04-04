import pygame

import os

from movement.config import Config

class Animation:
    def __init__(self, window_size):
        self.__image = pygame.image.load(os.path.join(*Config.animation_filename)).convert_alpha()

        self.__sprite_width = self.__image.get_width()/10
        self.__sprite_height = self.__image.get_height()/2
        self.__spritesRight = []
        self.__spritesLeft = []
        for i in range(10):
            self.__spritesRight.append(self.__image.subsurface(i * self.__sprite_width, 0, self.__sprite_width, self.__sprite_height))
            self.__spritesLeft.append(self.__image.subsurface(i * self.__sprite_width, self.__sprite_height, self.__sprite_width, self.__sprite_height))

        self.__is_moving_right = True
        self.__is_moving_left = False

        self.__animationBit = 0
        self.__position = pygame.math.Vector2(0 - self.__sprite_width/2, window_size[1] - self.__sprite_height)

    def handle_input(self, pressed, key):
        pass

    def update(self, delta):
        move = pygame.math.Vector2(0.0, 0.0)

        if self.__is_moving_right:
            move.x += Config.animation_speed
        if self.__is_moving_left:
            move.x -= Config.animation_speed

        self.__position += move * delta

        if self.__animationBit == 9:
            self.__animationBit = 1

        self.__animationBit = min(self.__animationBit + Config.animation_speed / Config.animation_speed * delta / 100, 9)

        if self.__position.x >= (Config.screen_size[0] - self.__sprite_width):
            self.__is_moving_right = False
            self.__is_moving_left = True

        elif self.__position.x <= 0:
            self.__is_moving_right = True
            self.__is_moving_left = False

    def render(self, dest):
        if self.__is_moving_right:
            dest.blit(self.__spritesRight[int(self.__animationBit)], self.__position.xy)
        if self.__is_moving_left:
            dest.blit(self.__spritesLeft[int(self.__animationBit)], self.__position.xy)

    def release(self):
        pass