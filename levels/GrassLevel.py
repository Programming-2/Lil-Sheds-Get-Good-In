from levels.Level import Level
from src.Platform import Platform


class GrassLevel(Level):

    def __init__(self, screen, handler):
        super().__init__(screen, "media/Levels/field_map.png", handler)
        self.plat1 = Platform(screen, 0, 650, 1100, 150)
        self.plat2 = Platform(screen, 350, 400, 400, 50)
        self.platformGroup.add(self.plat1)
        self.platformGroup.add(self.plat2)

    def update(self, screen):
        pass
