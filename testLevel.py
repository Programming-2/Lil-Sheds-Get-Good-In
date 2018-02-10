# Child class of level, serves as a test
from level import Level
from platform import Platform


class TestLevel(Level):
    def __init__(self, screen):
        super().__init__(screen, "media/field_map.png")
        self.ground = Platform(screen, 100, 500, 900, 50)

