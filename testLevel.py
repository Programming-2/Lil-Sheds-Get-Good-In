# Child class of level, serves as a test
from level import Level


class TestLevel(Level):
    def __init__(self, screen, main):
        from Platform import Platform
        super().__init__(screen, "media/field_map.png")
        self.__main = main
        self.ground = Platform(0, 650, 1100, 150)

