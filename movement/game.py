#!/usr/bin/env python3

import pygame
import os

from movement.config import Config
from movement.animation import Animation

class Game:

    def __init__(self):
        pygame.init()

        self.__screen = pygame.display.set_mode(Config.screen_size,0,32)
        pygame.display.set_caption(Config.game_title)

        self.__animation = Animation(self.__screen.get_size())

        self.__running = False

    def run(self):
        self.__running = True

        last = pygame.time.get_ticks()
        time_since_last_update = 0
        while self.__running:
            delta, last = self.__calc_delta(last)

            time_since_last_update += delta
            while time_since_last_update > Config.time_per_frame:
                time_since_last_update -= Config.time_per_frame

                self.__process_events()
                self.__update(Config.time_per_frame)

            self.__render()

        self.__quit()

    def __process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False

            if event.type == pygame.KEYDOWN:
                self.__animation.handle_input(True, event.key)
            if event.type == pygame.KEYUP:
                self.__animation.handle_input(False, event.key)

    def __update(self, delta):
        self.__animation.update(delta)

    def __render(self):
        self.__screen.fill(Config.background_color)
        self.__animation.render(self.__screen)
        pygame.display.update()

    def __quit(self):
        self.__animation.release()
        pygame.quit()

    def __calc_delta(self, last):
        current = pygame.time.get_ticks()
        delta = current - last
        return delta, current