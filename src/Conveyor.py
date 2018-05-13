from src.Platform import Platform


class Conveyor(Platform):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 10, 10, 0)
