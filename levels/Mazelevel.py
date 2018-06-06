from levels.Level import Level
from src.Platform import Platform
import time

class Mazelevel(Level):

    def __init__(self, screen, handler):
        super().__init__(screen, "media/Levels/Mazemap.png", handler)

        self.p1 = Platform(screen, 21, 125, 130, 0)
        self.p2 = Platform(screen, 220, 125, 650, 0)
        self.p3 = Platform(screen, 945, 125, 135, 0)
        self.platformGroup.add(self.p1)
        self.platformGroup.add(self.p2)
        self.platformGroup.add(self.p3)

    def update(self, screen):
        pass