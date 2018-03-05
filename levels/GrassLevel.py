import pygame
from levels.Level import Level
from src.Platform import Platform


class GrassLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/field_map.png")
        self.ground = Platform(screen, 0, 650, 1100, 150)
        self.lWall = Platform(screen, -100, 0, 100, 800)
        self.rWall = Platform(screen, 1100, 0, 100, 800)
        self.cPlat = Platform(screen, 350, 400, 400, 50)
        self.platformGroup = pygame.sprite.Group()
        self.platformGroup.add(self.ground)
        self.platformGroup.add(self.lWall)
        self.platformGroup.add(self.rWall)
        self.platformGroup.add(self.cPlat)

    def update(self):
        pass
