import pygame
from levels.Level import Level
from src.Platform import Platform


class IceLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/Levels/SnowMap.png")

        self.ground1 = Platform(screen, 0, 473, 225, 200)
        self.ground2 = Platform(screen, 224, 576, 616, 200)
        self.ground3 = Platform(screen, 841, 394, 259, 200)
        self.platformGroup.add(self.ground1)
        self.platformGroup.add(self.ground2)
        self.platformGroup.add(self.ground3)

    def update(self):
        pass
