import pygame
import colors


class Player(pygame.sprite.Sprite):

    def __init__(self, sprite, health, damage, winQuote, loseQuote, name, x, y, platArray):
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

    def takeDamage(self):
        self.health -= self.takenDamage

    def update(self, screen):
        screen.blit(self.sprite, [self.x, self.y])
        self.hitList = pygame.sprite.spritecollide(self, self.platArray, False)
        if self.hitList != []:
            if self.xchange > 0:
                self.resetJump()
                self.x +=self.xchange
                self.xchange = 0
            elif self.xchange < 0:
                self.resetJump()
                self.x += self.xchange
                self.xchange = 0
            if self.ychange > 0:
                self.resetJump()
                self.ychange = 0
                self.y = self.hitList[0].y - self.height
            elif self.ychange < 0:
                self.resetJump()
                self.ychange = 0
                self.y = self.hitList[0].y - self.height
        else:
            self.x += self.xchange
            self.y += self.ychange

        self.rect.topleft = self.x, self.y