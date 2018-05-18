from levels.Level import Level
from src.Platform import Platform
import time

class Mazelevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/Levels/Mazemap.png")

        self.p1 = Platform(screen, 21, 122, 155, 122)
        self.p2 = Platform(screen, 220, 122, 870, 122)
        self.p3 = Platform(screen, 945, 122, 1080, 122)
        self.platformGroup.add(self.p1)
        self.platformGroup.add(self.p2)
        self.platformGroup.add(self.p3)

    def update(self, screen):
        pass