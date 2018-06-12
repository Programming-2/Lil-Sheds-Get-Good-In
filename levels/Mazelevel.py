from levels.Level import Level
from src.Platform import Platform
import time

class Mazelevel(Level):

    def __init__(self, screen, handler):
        super().__init__(screen, "media/Levels/Mazemap.png", handler)

        self.p1 = Platform(screen, 127, 94, 28, 96)
        self.p2 = Platform(screen, 946, 94, 29, 96)
        self.p3 = Platform(screen, 281, 1, 538, 121)
        self.p4 = Platform(screen, 454, 93, 191, 233)
        self.p5 = Platform(screen, (0-100), 93, 154, 129)
        self.p6 = Platform(screen, 946, 93, 154, 29)
        self.p7 = Platform(screen, 126, 295, 222, 28)
        self.p8 = Platform(screen, 753, 295, 192, 28)
        self.p9 = Platform(screen, 348, 459, 403, 43)
        self.p10 = Platform(screen, 126, 319, 33, 353)
        self.p11 = Platform(screen, 126, 644, 223, 28)
        self.p12 = Platform(screen, 946, 295, 29, 353)
        self.p13 = Platform(screen, 753, 644, 223, 28)
        self.p14 = Platform(screen, 454, 568, 192, 208)
        self.p15 = Platform(screen, 21, 777, 2063, 24)
        self.p16 = Platform(screen, 83, 460, 47, 41)
        self.p17 = Platform(screen, 970, 460, 47, 41)
        self.platformGroup.add(self.p1)
        self.platformGroup.add(self.p2)
        self.platformGroup.add(self.p3)
        self.platformGroup.add(self.p4)
        self.platformGroup.add(self.p5)
        self.platformGroup.add(self.p6)
        self.platformGroup.add(self.p7)
        self.platformGroup.add(self.p8)
        self.platformGroup.add(self.p9)
        self.platformGroup.add(self.p10)
        self.platformGroup.add(self.p11)
        self.platformGroup.add(self.p12)
        self.platformGroup.add(self.p13)
        self.platformGroup.add(self.p14)
        self.platformGroup.add(self.p15)
        self.platformGroup.add(self.p16)
        self.platformGroup.add(self.p17)

    def update(self, screen):
        pass