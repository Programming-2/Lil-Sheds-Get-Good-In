#Parent Level Class
from abc import abstractmethod

import pygame
pygame.init()


class Level():
    def __init__(self, screen, back_img):
        self.__screen = screen
        self.__back_img = back_img

    @abstractmethod
    def update(self):
        pass