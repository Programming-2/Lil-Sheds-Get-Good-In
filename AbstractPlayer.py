import pygame
from entity import Entity


class AbstractPlayer(Entity):

    def __init__(self, startx, starty, image):
        super().__init__(startx, starty, 0, 0, image)
