class Button:

    def __init__(self, action, img, x, y, handler):
        self.action = action
        self.img = img
        self.x = x
        self.y = y
        self.handler = handler
        self.buttonPressed = False

    def update(self, screen):
        screen.blit(self.img, [self.x, self.y])

        if self.buttonPressed:
            self.buttonPressed = False
