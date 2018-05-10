from src.Platform import Platform


class ConveyorBelt(Platform):
    def __init__(self, screen, handler, x, y, length, height, speed, direction):
        print("CODE IS GAY")
        self.handler = handler
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.speed = speed
        self.direction = direction

        super().__init__(screen, x, y, length, height, duration=-1)
