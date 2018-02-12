import pygame
import colors
from attack import Attack


class Player(pygame.sprite.Sprite):

    def __init__(self, sprite, health, damage, winQuote, loseQuote, name, x, y, platArray, handler):
        super().__init__()
        self.sprite = sprite
        self.health = health
        self.damage = damage
        self.winQuote = winQuote
        self.loseQuote = loseQuote
        self.name = name
        self.x = x
        self.y = y
        self.platArray = platArray
        self.xchange = 0
        self.ychange = 0
        self.gravity = 0.25
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.jumpCount = 0
        self.takenDamage = 0
        self.handler = handler

    def jump(self):
        if self.jumpCount < 100:
            self.ychange = -10
            self.jumpCount += 1

    def resetJump(self):
        self.jumpCount = 0

    def LoseQuote(self):
        text = (self.loseQuote, True, colors.colors.get("BLACK"))
        return text

    def WinQuote(self):
        text = (self.winQuote, True, colors.colors.get("BLACK"))
        return text

    def takeDamage(self, takenDamage):
        self.health -= self.takenDamage

    def gravityUpdate(self):
        if not(self.checkPlatformCollision()):
            self.ychange += self.gravity
        else:
            self.resetJump()

    def update(self, screen):
        self.moveX()
        self.moveY()
        self.gravityUpdate()
        screen.blit(self.sprite, [self.x, self.y])
        self.rect.topleft = self.x, self.y

    def checkEntityCollision(self):
        return False

    def checkPlatformCollision(self):
        return pygame.sprite.spritecollide(self, self.platArray, False) != []

    def moveX(self):
        tempXChange = self.xchange
        self.x += self.xchange
        if self.xchange > 0: #Moving right
            if not(self.checkPlatformCollision()):
                self.x += self.xchange
            else:
                self.xchange = 0
                self.x -= 1
        elif self.xchange < 0: #Moving left:
            if not(self.checkPlatformCollision()):
                self.x += self.xchange
            else:
                self.xchange = 0
                self.x += 1
        self.x -= tempXChange

    def moveY(self):
        tempYChange = self.ychange
        self.y += self.ychange
        if self.ychange > 0: #Moving down
            if not(self.checkPlatformCollision()):
                self.y += self.ychange
            else:
                self.ychange = 0
                self.y -= 1
        elif self.ychange < 0: #Moving up
            if not(self.checkPlatformCollision()):
                self.y += self.ychange
            else:
                self.ychange = 0
                self.y += 1
        self.y -= tempYChange
    def attack(self, image, screen):
        self.handler.getAttackList().add(Attack(self.x, self.y, "ranged", 1, 0, 0, screen, image))

    def goToSleepForAnExtendedPeriodOfTime(self):
        self.ychange = -5

    def getX(self):
        return self.x

    def getY(self):
        return self.y

