class Button:

    def __init__(self, action, img, x, y, width, handler):
        self.action = action
        self.img = img
        self.x = x
        self.y = y
        self.width = width
        self.handler = handler

    def update(self, screen):
        screen.blit(self.img, [self.x, self.y])

        if (self.handler.player1.isCrouching or self.handler.player2.isCrouching) and self.playerInRange():
            self.action()

    def playerInRange(self):
        player1 = self.handler.player1
        player2 = self.handler.player2

        if (self.x < player1.rect.x < self.x + self.width and self.y - 6 < player1.rect.y < self.y + 6) or (self.x < player2.rect.x < self.x + self.width and self.y - 6 < player2.rect.y < self.y + 6):
            return True

        return False
