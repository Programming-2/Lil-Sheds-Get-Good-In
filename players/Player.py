import pygame
from utils import Colors
from src.Attack import Attack
from src.MeleeAttack import MeleeAttack
from src.Cooldown import Cooldown
from utils.Sound import Sound


class Player(pygame.sprite.Sprite):

    def __init__(self, health, damage, winQuote, loseQuote, name, x, y, movespeed, platArray, attackList, handler, defense):
        super().__init__()
        self.i = 0
        self.sprite = pygame.image.load("media/Players/" + name + "/" + name + ".png").convert_alpha()
        self.stansprite = pygame.image.load("media/Players/" + name + "/" + name + ".png").convert_alpha()
        self.crouchsprite = pygame.image.load("media/Players/" + name + "/" + name + "Crouch.png").convert_alpha()
        self.attacksprite = pygame.image.load("media/Misc/projectileRight.png").convert_alpha()
        self.leftsprite = pygame.transform.flip(self.sprite, True, False)
        self.rightsprite = self.stansprite
        self.leftcrouchsprite = pygame.transform.flip(self.crouchsprite, True, False)
        self.rightcrouchsprite = self.crouchsprite
        self.hitSound = Sound("DeathSound")
        self.attacksound = Sound("GunFiring")
        self.gregMeleeHit = Sound("Knife Slice Into Flesh Sound Effect")
        self.rapidFire = Sound("HEAVY MACHINE GUN SOUND EFFECT(1)")
        self.hoverOver = Sound("Beep2")
        self.deathsound = Sound("LongDeathSound")
        #self.jumpSound = Sound("y2mate.com - cartoon_boing_sound_effect_3_rm_qHuXXvpk")
        self.BIGGsound = Sound("BIGGDeathSound")
        self.rightAttackSprite = self.attacksprite
        self.leftAttackSprite = pygame.transform.rotate(self.attacksprite, 180)
        self.damage = damage
        self.maxHP = health
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
        self.meleeattack = MeleeAttack(20, self, self.handler)

        self.jumpreleased = False
        self.duckreleased = False
        self.crouching = False

    def setPlatArray(self, arr):
        self.platArray = arr

    def setMoveSpeed(self, movespeed):
        self.movespeed = movespeed

    def jump(self):
        if self.jumpCount <= 1:
            self.ychange = -10
            self.jumpCount += 1
            #self.jumpSound.playSound()

    def unjump(self):
        pass

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
        self.hitSound.playSound()
    
    def takeTrueDamage(self, takenDamage):
        self.health -= takenDamage
        self.BIGGsound.playSound()

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

    def checkEntityCollision(self):
        return False

    def duck(self):
        self.crouching = True
        self.rect.y += self.stansprite.get_height() - self.crouchsprite.get_height()
        if self.facing == 1:
            self.sprite = self.rightcrouchsprite
        if self.facing == -1:
            self.sprite = self.leftcrouchsprite
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
        self.gravity = 1

    def unduck(self):
        if self.crouching:
            self.crouching = False
            self.rect.y -= self.stansprite.get_height() - self.crouchsprite.get_height()
            if self.facing == 1:
                self.sprite = self.rightsprite
            if self.facing == -1:
                self.sprite = self.leftsprite
            self.width = self.sprite.get_width()
            self.height = self.sprite.get_height()
            self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
            self.gravity = 0.25

    def moveX(self):
        if self.xchange < 0 and not self.crouching:
            self.sprite = self.leftsprite
        if self.xchange > 0 and not self.crouching:
            self.sprite = self.rightsprite
        if self.xchange < 0 and self.crouching:
            self.sprite = self.leftcrouchsprite
        if self.xchange > 0 and self.crouching:
            self.sprite = self.rightcrouchsprite
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

    def moveLeft(self):
        self.xchange = self.movespeed * -1

    def moveRight(self):
        self.xchange = self.movespeed

    def attackUpdate(self, screen):
        self.attackList.update(screen)

    def attack(self, screen):
        self.handler.getAttackList().add(Attack(self, self.damage, self.handler))

    def meleeAttack(self, screen):
        self.meleeattack.attack(screen)

    def special(self):
        pass  # abstract

    def goToSleepForAnExtendedPeriodOfTime(self):
        self.deathsound.playSound()
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

    def __eq__(self, other):
        return other.toString() == self.name
