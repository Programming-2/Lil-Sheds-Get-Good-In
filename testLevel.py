# Child class of level, serves as a test
from level import Level


class TestLevel(Level):
    def __init__(self, screen, main):
        super().__init__(screen, "media/field_map.png")
<<<<<<< HEAD
    
=======
        self.__ground = 650
        self.__main = main
>>>>>>> 46d1ebfe342b79cc4f611f79f694b54e7f3ce333
