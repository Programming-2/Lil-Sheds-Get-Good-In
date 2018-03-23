import pygame
from levels.Level import Level
from src.Platform import Platform


class LavaLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/LavaMap.png")

        # TODO Add platforms
        self.lWall = Platform(screen, -100, -1000, 100, 1800)
        self.rWall = Platform(screen, 1100, -1000, 100, 1800)
        self.p1 = Platform(screen, 135, 510, 56, 290)
        self.p2 = Platform(screen, 262, 409, 49, 391)
        self.p3 = Platform(screen, 437, 315, 324, 485)
        self.p4 = Platform(screen, 824, 408, 56, 392)
        self.p5 = Platform(screen, 943, 495, 59, 306)
        self.platformGroup = pygame.sprite.Group()
        self.platformGroup.add(self.lWall)
        self.platformGroup.add(self.rWall)
        self.platformGroup.add(self.p1)
        self.platformGroup.add(self.p2)
        self.platformGroup.add(self.p3)
        self.platformGroup.add(self.p4)
        self.platformGroup.add(self.p5)

    def update(self):
        pass
