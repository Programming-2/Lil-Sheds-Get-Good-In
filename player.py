import pygame
import colors
from attack import Attack


class Player(pygame.sprite.Sprite):

    def __init__(self, health, damage, winQuote, loseQuote, name, x, y, platArray, handler, defense):
        super().__init__()
        self.duckSprite = pygame.image.load("media/TestCrouchSprite.png").convert()
        self.stanSprite = pygame.image.load("media/BaseSprite.png").convert()
        self.sprite = self.stanSprite
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
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.jumpCount = 0
        self.takenDamage = 0
        self.handler = handler
        self.defense = defense
        self.facing = 1 #-1 for left, 1 for right

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
        self.health -= (takenDamage * self.defense)

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

        if self.xchange > 0:
            self.facing = 1
        elif self.xchange < 0:
            self.facing = -1

    def checkEntityCollision(self):
        return False

    def duck(self):
        self.y += self.stanSprite.get_height() - self.duckSprite.get_height()
        self.sprite = self.duckSprite
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def unduck(self):
        self.y -= self.stanSprite.get_height() - self.duckSprite.get_height()
        self.sprite = self.stanSprite
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def moveX(self):
        self.x += self.xchange
        self.rect.x = self.x
        platList = pygame.sprite.spritecollide(self, self.platArray, False)
        for platform in platList:
            if self.xchange > 0 and self.rect.right < platform.rect.right:  # Moving right and left of platform
                self.rect.right = platform.rect.left
            elif self.xchange < 0 and self.rect.left > platform.rect.left:  # Moving left and right of platform
                self.rect.left = platform.rect.right
            self.x = self.rect.x
            self.xchange = 0

    def moveY(self):
        self.y += self.ychange
        self.rect.y = self.y
        platList = pygame.sprite.spritecollide(self, self.platArray, False)
        for platform in platList:
            if self.ychange > 0 and self.rect.bottom < platform.rect.bottom:  # Moving down and over platform
                self.rect.bottom = platform.rect.top
                self.resetJump()
            elif self.ychange < 0 and self.rect.top > platform.rect.top:  # Moving up and under platform
                self.rect.top = platform.rect.bottom
                self.resetJump()
            self.y = self.rect.y
            self.ychange = 0

    def attack(self, image, screen, player):
        if self.facing == -1:
            self.handler.getAttackList().add(Attack(self.x - 20, self.y, 5 * self.facing, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
        else:
            self.handler.getAttackList().add(Attack(self.x + self.width, self.y, 5 * self.facing, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))


    def goToSleepForAnExtendedPeriodOfTime(self):
        self.ychange = -5

    def getX(self):
        return self.x

    def getY(self):
        return self.y

