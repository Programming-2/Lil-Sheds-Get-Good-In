#Parent Level Class
from abc import abstractmethod
import pygame

pygame.init()


class Level():
    def __init__(self, screen, backImg):
        self.__screen = screen
        self.__backImg = backImg

    def getBackImg(self):
        return self.__backImg

    @abstractmethod
    def update(self):
        pass

