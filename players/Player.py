import pygame
from utils import Colors
from src.Attack import Attack
from src.Cooldown import Cooldown
from utils.Colors import colors

# TODO Figure out why sprite draws weird/gets cut


class Player(pygame.sprite.Sprite):

    def __init__(self, health, damage, winQuote, loseQuote, name, x, y, movespeed, platArray, attackList, handler, defense):
        super().__init__()
        self.i = 0
        self.sprite = pygame.image.load("media/Players/" + name + "/" + name + ".png").convert()
        self.stansprite = pygame.image.load("media/Players/" + name + "/" + name + ".png").convert()
        self.crouchsprite = pygame.image.load("media/Players/" + name + "/" + name + "Crouch.png").convert()
        self.rightAttackSprite = pygame.image.load("media/Misc/projectileRight.png").convert_alpha()
        self.leftAttackSprite = pygame.image.load("media/Misc/projectileLeft.png").convert_alpha()
        self.damage = damage
        self.health = health
        self.winQuote = winQuote
        self.loseQuote = loseQuote
        self.name = name
        self.platArray = platArray
        self.attackList = attackList
        self.xchange = 0
        self.ychange = 0
        self.movespeed = movespeed
        self.gravity = 0.25
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.jumpCount = 0
        self.takenDamage = 0
        self.handler = handler
        self.defense = defense
        self.stunned = False
        self.sleeping = False
        self.facing = 1  # -1 for left, 1 for right
        self.special_cooldown = Cooldown(0)
        self.ranged_cooldown = Cooldown(0)
        self.bullet_speed = 15

    def setPlatArray(self, arr):
        self.platArray = arr

    def setMoveSpeed(self, movespeed):
        self.movespeed = movespeed

    def jump(self):
        if self.jumpCount <= 1:
            self.ychange = -10
            self.jumpCount += 1

    def resetJump(self):
        self.jumpCount = 0

    def LoseQuote(self):
        text = (self.loseQuote, True, Colors.colors.get("BLACK"))
        return text

    def WinQuote(self):
        text = (self.winQuote, True, Colors.colors.get("BLACK"))
        return text

    def takeDamage(self, takenDamage):
        self.health -= round(takenDamage * self.defense)

    def gravityUpdate(self):
        if self.ychange == 0:
            self.ychange = 1
        else:
            self.ychange += self.gravity

    def update(self, screen):
        self.screen = screen
        self.gravityUpdate()
        self.moveX()
        self.moveY()
        screen.blit(self.sprite, [self.rect.x, self.rect.y])

        if self.xchange > 0:
            self.facing = 1
        elif self.xchange < 0:
            self.facing = -1

        self.attackUpdate(screen)

    def checkEntityCollision(self):
        return False

    def duck(self):
        self.rect.y += self.stansprite.get_height() - self.crouchsprite.get_height()
        self.sprite = self.crouchsprite
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)

    def unduck(self):
        self.rect.y -= self.stansprite.get_height() - self.crouchsprite.get_height()
        self.sprite = self.stansprite
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)

    def moveX(self):
        self.rect.x += self.xchange
        platList = pygame.sprite.spritecollide(self, self.platArray, False)
        for platform in platList:
            if self.xchange > 0 and self.rect.right < platform.rect.right:  # Moving right and left of platform
                self.rect.right = platform.rect.left
            elif self.xchange < 0 and self.rect.left > platform.rect.left:  # Moving left and right of platform
                self.rect.left = platform.rect.right
            self.xchange = 0

    def moveY(self):
        self.rect.y += self.ychange
        platList = pygame.sprite.spritecollide(self, self.platArray, False)
        for platform in platList:
            if self.ychange > 0 and self.rect.bottom < platform.rect.bottom:  # Moving down and over platform
                self.rect.bottom = platform.rect.top
                self.resetJump()
            elif self.ychange < 0 and self.rect.top > platform.rect.top:  # Moving up and under platform
                self.rect.top = platform.rect.bottom
                self.resetJump()
            self.ychange = 0

    def attackUpdate(self, screen):
        for e in self.attackList:
            if e.x < 0 or e.x > screen.get_size()[0]:
                self.attackList.remove(e)
            if e.y < 0 or e.y > screen.get_size()[1]:
                self.attackList.remove(e)
            e.render(screen)
            e.move()
            if pygame.sprite.spritecollide(self, self.attackList, False):
                pygame.sprite.spritecollide(self, self.attackList, True)
                self.takeDamage(e.damage)

    def attack(self, screen):
        if self.facing == -1:
            self.handler.getAttackList().add(Attack(self.rect.x - 50, self.rect.y, self.bullet_speed * self.facing, 0, "ranged", self.damage, 3, 5, screen, self.leftAttackSprite, 20, self.handler))
        elif self.facing == 1:
            self.handler.getAttackList().add(Attack(self.rect.x + self.width + 30, self.rect.y, self.bullet_speed * self.facing, 0, "ranged", self.damage, 3, 5, screen, self.rightAttackSprite, 20, self.handler))

    def special(self):
        pass  # abstract

    def goToSleepForAnExtendedPeriodOfTime(self):
        self.ychange = -5
        self.sleeping = True
        self.i += 1
        if self.i == 180:
            self.i = 0
            self.handler.getStateManager().resetStates()
            self.handler.getStateManager().setCurrentState("MainMenuState")

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def setX(self, x):
        self.rect.x = x

    def toString(self):
        return self.name
