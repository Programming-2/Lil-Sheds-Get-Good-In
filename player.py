import pygame
import colors
from attack import Attack


class Player(pygame.sprite.Sprite):

    def __init__(self, sprite, health, damage, winQuote, loseQuote, name, x, y, platArray, screen, testProjectile):
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
        self.ranged_attack = Attack(self.x, self.y, "ranged", 1, 0, 0, screen, testProjectile)

    def jump(self):
        if self.jumpCount < 1:
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

    def takeDamage(self):
        self.health -= self.takenDamage

    def gravityUpdate(self):
        if pygame.sprite.spritecollide(self, self.platArray, False) == []:
            self.ychange += self.gravity
        else:
            self.ychange = 0
            self.resetJump()

    def update(self, screen):
        self.hitList = pygame.sprite.spritecollide(self, self.platArray, False)
        for element in self.hitList:
            if self.xchange > 0:
                self.rect.right = element.rect.left
                if self.rect.left > element.rect.left:
                    self.xchange = 0
            elif self.xchange < 0:
                self.rect.left = element.rect.right
                if self.rect.right < element.rect.right:
                    self.xchange = 0
            if self.ychange > 0:
                self.resetJump()
                self.rect.bottom = element.rect.top
            elif self.ychange < 0:
                self.resetJump()
                self.rect.top = element.rect.bottom
        self.x += self.xchange
        self.y += self.ychange
        screen.blit(self.sprite, [self.x, self.y])
        self.rect.topleft = self.x, self.y
        self.gravityUpdate()

        self.ranged_attack.updatePlayerCoords(self.x, self.y)

    def getAttack(self):
        return self.ranged_attack