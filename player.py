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
        if self.jumpCount <= 1:
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
        self.health -= takenDamage

    def gravityUpdate(self):
        if self.ychange == 0:
            self.ychange = 1
        else:
            self.ychange += self.gravity

    def update(self, screen):
        self.gravityUpdate()
        self.moveX()
        self.moveY()
        screen.blit(self.sprite, [self.x, self.y])

    def checkEntityCollision(self):
        return False

    def checkPlatformCollision(self):
        return pygame.sprite.spritecollide(self, self.platArray, False) != []

    def moveX(self):
        self.x += self.xchange
        self.rect.x = self.x
        platList = pygame.sprite.spritecollide(self, self.platArray, False)
        for platform in platList:
            if self.xchange > 0 and self.rect.right < platform.rect.right:  # Moving right and left of platform
                self.x = platform.rect.left - self.width
            elif self.xchange < 0 and self.rect.left > platform.rect.left:  # Moving left and right of platform
                self.x = platform.rect.right
            self.xchange = 0

    def moveY(self):
        self.y += self.ychange
        self.rect.y = self.y
        platList = pygame.sprite.spritecollide(self, self.platArray, False)
        for platform in platList:
            if self.ychange > 0 and self.rect.bottom < platform.rect.bottom :  # Moving down and over platform
                self.rect.bottom = platform.rect.top
            elif self.ychange < 0 and self.rect.top > platform.rect.top:  # Moving up and under platform
                self.rect.top = platform.rect.bottom
            self.y = self.rect.y
            self.ychange = 0
            self.resetJump()

    def attack(self, image, screen):
        self.handler.getAttackList().add(Attack(self.x, self.y, "ranged", 1, 0, 0, screen, image, 20, self.handler))
        self.handler.getAttackList().add(Attack(self.x, self.y, "ranged", 1, 0, 0, screen, image, 20, self.handler))

    def goToSleepForAnExtendedPeriodOfTime(self):
        self.ychange = -5

    def getX(self):
        return self.x

    def getY(self):
        return self.y

