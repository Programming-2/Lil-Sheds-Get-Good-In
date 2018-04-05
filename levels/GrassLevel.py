import pygame
from levels.Level import Level
from src.Platform import Platform


class GrassLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/field_map.png")
        self.ground = Platform(screen, 0, 650, 1100, 150)
        self.cPlat = Platform(screen, 350, 400, 400, 50)
        self.platformGroup.add(self.ground)
        self.platformGroup.add(self.cPlat)

    def update(self):
        pass
