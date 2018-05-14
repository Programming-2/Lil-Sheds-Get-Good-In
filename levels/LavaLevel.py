from levels.Level import Level
from src.Platform import Platform


class LavaLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/Levels/LavaMap.png")

        # TODO Add platforms
        self.p1 = Platform(screen, 135, 510, 56, 290, -1)
        self.p2 = Platform(screen, 262, 409, 49, 391, -1)
        self.p3 = Platform(screen, 437, 315, 324, 485, -1)
        self.p4 = Platform(screen, 824, 408, 56, 392, -1)
        self.p5 = Platform(screen, 943, 495, 59, 306, -1)
        self.platformGroup.add(self.p1)
        self.platformGroup.add(self.p2)
        self.platformGroup.add(self.p3)
        self.platformGroup.add(self.p4)
        self.platformGroup.add(self.p5)

    def update(self, screen):
        pass
