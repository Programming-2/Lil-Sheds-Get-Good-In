import pygame
from levels.Level import Level
from Platform import Platform


class GrassLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/LavaMap.png")

        # TODO Add platforms
        self.lWall = Platform(screen, -100, 0, 100, 800)
        self.rWall = Platform(screen, 1100, 0, 100, 800)
        self.platformGroup = pygame.sprite.Group()
        self.platformGroup.add(self.lWall)
        self.platformGroup.add(self.rWall)

    def update(self):
        pass
