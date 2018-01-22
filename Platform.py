#Platform class

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, len, height):
        super().__init__()
        self.x = x
        self.y = y
        self.len = len
        self.height = height
        #yes