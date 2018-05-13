class Button:

    def __init__(self, action, img, x, y):
        self.action = action
        self.img = img
        self.x = x
        self.y = y

    def preformAction(self):
        self.action()

    def update(self, screen):
        screen.blit(self.img, [self.x, self.y])
