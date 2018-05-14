# Parent Level Class
from abc import abstractmethod
import pygame
from src.Platform import Platform

pygame.init()


class Level():
    def __init__(self, screen, backImg):
        self.__screen = screen
        self.__backImg = backImg
        self.lWall = Platform(screen, -500, -1000, 500, 2300)
        self.rWall = Platform(screen, 1100, -1000, 500, 2300)
        self.ceiling = Platform(screen, -500, -1500, 2100, 500)
        self.ground = Platform(screen, -500, 900, 2100, 500)
        self.platformGroup = pygame.sprite.Group()
        self.platformGroup.add(self.lWall)
        self.platformGroup.add(self.rWall)
        self.platformGroup.add(self.ceiling)
        self.platformGroup.add(self.ground)


    def getBackImg(self):
        return self.__backImg

    @abstractmethod
    def update(self):
        pass
