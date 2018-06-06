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

        if self.handler.player1.crouching and self.playerInRange(self.handler.player1):
            screen.blit(self.buttonPressed, [self.x, self.y])
            if self.released:
                self.released = False
                self.action()
        if self.handler.player2.crouching and self.playerInRange(self.handler.player2):
            screen.blit(self.buttonPressed, [self.x, self.y])
            if self.released:
                self.released = False
                self.action()

        if not((self.handler.player1.crouching or self.handler.player2.crouching) and self.playerInRange()):
            self.released = True

    def playerInRange(self, player):
        if self.x < player.rect.x < self.x + self.width and self.y - player.rect.height - 6 < player.rect.y < self.y + 6
            return True

        return False
