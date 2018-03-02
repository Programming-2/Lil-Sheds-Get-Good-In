import pygame
from levels.Level import Level
from Platform import Platform


class IceLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/SnowMap.png")

        # TODO Add platforms
        self.lWall = Platform(screen, -100, 0, 100, 800)
        self.rWall = Platform(screen, 1100, 0, 100, 800)
        self.ground1 = Platform(screen, 0, 473, 225, 200)
        self.ground2 = Platform(screen, 224, 576, 616, 200)
        self.ground3 = Platform(screen, 841, 394, 259, 200)
        self.platformGroup = pygame.sprite.Group()
        self.platformGroup.add(self.lWall)
        self.platformGroup.add(self.rWall)
        self.platformGroup.add(self.ground1)
        self.platformGroup.add(self.ground2)
        self.platformGroup.add(self.ground3)

    def update(self):
        pass
