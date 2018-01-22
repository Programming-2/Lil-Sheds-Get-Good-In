# Child class of level, serves as a test
from level import Level
from platform import Platform


class TestLevel(Level):
    def __init__(self, screen):
        super().__init__(screen, "media/field_map.png")
        self.ground = Platform(0, 650, 1100, 150)

