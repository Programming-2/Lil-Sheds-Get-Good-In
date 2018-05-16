import pygame


class Button:

    def __init__(self, action, x, y, width, handler):
        self.action = action
        self.x = x
        self.y = y
        self.width = width
        self.handler = handler
        self.button = pygame.image.load("media/Misc/greenButton.png").convert_alpha()
        self.buttonPressed = pygame.image.load("media/Misc/redButton.png").convert_alpha()
        self.released = True

    def update(self, screen):
        screen.blit(self.button, [self.x, self.y])

        if (self.handler.player1.crouching or self.handler.player2.crouching) and self.playerInRange():
            screen.blit(self.buttonPressed, [self.x, self.y])
            if self.released:
                self.released = False
                self.action()

        if not((self.handler.player1.crouching or self.handler.player2.crouching) and self.playerInRange()):
            self.released = True

    def playerInRange(self):
        player1 = self.handler.player1
        player2 = self.handler.player2

        if (self.x < player1.rect.x < self.x + self.width and self.y - player1.rect.height - 6 < player1.rect.y < self.y + 6) or (self.x < player2.rect.x < self.x + self.width and self.y - player2.rect.height - 6 < player2.rect.y < self.y + 6):
            return True

        return False
