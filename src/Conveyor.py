from src.Platform import Platform


class Conveyor(Platform):

    def __init__(self, x, y):
        super().__init__(None, x, y, 10, 10, 0)
