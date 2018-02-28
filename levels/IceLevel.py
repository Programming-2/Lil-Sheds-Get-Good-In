import pygame
from level import Level
from platform import Platform


class IceLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/SnowMap.png")

        # TODO Add platforms

    def update(self):
        pass
