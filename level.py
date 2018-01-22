#Parent Level Class
from abc import abstractmethod
import pygame

pygame.init()


class Level():
    def __init__(self, screen, backImg):
        self.__screen = screen
        self.__backImg = backImg
        self.__gravity = 0.25

    def getBackImg(self):
        return self.__backImg

    def getGravity(self):
        return self.__gravity

    @abstractmethod
    def update(self):
        pass

