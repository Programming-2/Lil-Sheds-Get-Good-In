import pygame
from levels.Level import Level
from src.Platform import Platform


class LavaLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/LavaMap.png")

        # TODO Add platforms
        self.lWall = Platform(screen, -100, 0, 100, 800)
        self.rWall = Platform(screen, 1100, 0, 100, 800)
        self.p1 = Platform(screen, 65, 585, 70, 215)
        self.p2 = Platform(screen, 262, 441, 48, 328)
        self.p3 = Platform(screen, 943, 399, 58, 400)
        self.p4 = Platform(screen, 761, 564, 92, 170)
        self.p5 = Platform(screen, 736, 316, 25, 486)
        self.p6 = Platform(screen, 437, 316, 42, 488)
        self.p7 = Platform(screen, 438, 316, 322, 32)
        self.p8 = Platform(screen, 510, 288, 52, 27)
        self.p9 = Platform(screen, 659, 256, 78, 59)
        self.platformGroup = pygame.sprite.Group()
        self.platformGroup.add(self.lWall)
        self.platformGroup.add(self.rWall)
        self.platformGroup.add(self.p1)
        self.platformGroup.add(self.p2)
        self.platformGroup.add(self.p3)
        self.platformGroup.add(self.p4)
        self.platformGroup.add(self.p5)
        self.platformGroup.add(self.p6)
        self.platformGroup.add(self.p7)
        self.platformGroup.add(self.p8)
        self.platformGroup.add(self.p9)

    def update(self):
        pass
