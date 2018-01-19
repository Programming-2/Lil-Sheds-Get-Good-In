#Child class of level, serves as a test
from level import Level

class TestLevel(Level):
    def __init__(self, screen):
        super.__init__(screen, "media/field_map.png")
        self.ground = 650