import pygame
from players.Player import Player
from src.CustomAttack import CustomAttack
from src.Cooldown import Cooldown
from animation.Animation import Animation
from animation.AnimationManager import AnimationManager


class Greg(Player):

    def __init__(self, x, y, handler):
        health = 1000
        damage = 75
        win_quote = "Broken like Katarina"
        lose_quote = "I don't even care"
        name = "Greg"
        movespeed = 5
        defense = .7

        super().__init__(health, damage, win_quote, lose_quote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.count = 0
        self.special_active = False
        self.special_cooldown = Cooldown(5)
        self.special_duration = Cooldown(1)
        self.attacksprite = pygame.image.load("media/Misc/fist.png").convert()
        self.specialsprite = pygame.image.load("media/Players/Greg/GregSpecial.png").convert()
        self.specialframe1 = pygame.image.load("media/Players/Greg/GregSpecial1.png").convert_alpha()
        self.specialframe2 = pygame.image.load("media/Players/Greg/GregSpecial2.png").convert_alpha()
        self.specialnum = 1
        self.damage_ranged = 200
        self.damage_special = 125
        self.startgravity = self.gravity
        self.attacking = False
        self.attackcount = 0
        self.attackradius = 100
        self.ranged_cooldown = Cooldown(2)
        self.walk_animation_delay = 8

        # Animation
        self.walkSpriteList = [
            pygame.image.load("media/Players/Greg/Greg1.png").convert_alpha(),
            pygame.image.load("media/Players/Greg/Greg2.png").convert_alpha(),
            pygame.image.load("media/Players/Greg/Greg3.png").convert_alpha(),
            pygame.image.load("media/Players/Greg/Greg4.png").convert_alpha()
        ]

        self.walkAnimation = Animation(self.handler, self, self.walkSpriteList)

        self.animation_manager = AnimationManager(self, self.walkAnimation)

    def attack(self, screen):
        if self.ranged_cooldown.isDone():
            self.attacking = True
            targetPlayer = self.handler.getOtherPlayer(self)
            if self.facing == 1:
                if self.rect.x <= 900 - self.width:
                    self.rect.x += 200
                elif self.rect.x > 900 - self.width:
                    self.rect.x += (1100 - self.rect.x - self.width)
                if self.attackradius + (self.width * .5) >= targetPlayer.rect.x - self.rect.x >= -self.attackradius + (self.width * .5) and self.attackradius + (self.width * .5) >= self.handler.getPlayer2().rect.y - self.rect.y >= -self.attackradius + (self.width * .5):
                    targetPlayer.takeDamage(self.damage_ranged)
                    self.gregMeleeHit.playSound()
            if self.facing == -1:
                if self.rect.x >= 200:
                    self.rect.x += -200
                elif self.rect.x < 200:
                    self.rect.x += -self.rect.x
                if 150 >= targetPlayer.rect.x - self.rect.x >= -150 and 150 >= targetPlayer.rect.y - self.rect.y >= -150:
                    targetPlayer.takeDamage(self.damage_ranged)
                    self.gregMeleeHit.playSound()
            self.ranged_cooldown.update()

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True

    def moveX(self):
        self.rect.x += self.xchange
        platList = pygame.sprite.spritecollide(self, self.platArray, False)
        for platform in platList:
            if self.xchange > 0 and self.rect.right < platform.rect.right:  # Moving right and left of platform
                self.rect.right = platform.rect.left
            elif self.xchange < 0 and self.rect.left > platform.rect.left:  # Moving left and right of platform
                self.rect.left = platform.rect.right
            self.xchange = 0

    def duck(self):
        self.gravity = 1

    def unduck(self):
        self.gravity = .25

    def update(self, screen):
        self.animation_manager.update()
        if not self.ranged_cooldown.isDone():
            self.ranged_cooldown.update()
        if self.attacking:
            if self.attackcount % 2 == 1:
                screen.blit(self.specialframe1, (self.rect.x - 125, self.rect.y - 125))
            if self.attackcount % 2 == 0:
                screen.blit(self.specialframe2, (self.rect.x - 125, self.rect.y - 125))
            self.attackcount += 1
            if self.attackcount > 6:
                self.attacking = False
                self.attackcount = 1
        if not self.special_active:
            super().update(screen)

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()

        if self.special_active and not self.sleeping:
            self.sprite = self.specialsprite
            self.special_duration.update()
            if not self.special_duration.isDone():
                self.specialnum += 1
                if self.specialnum > 8:
                    self.specialnum = 1
                self.xchange = 0
                self.ychange = 0
                self.gravity = 0
                if self.specialnum == 1:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage_special, self.handler, 15, 0))
                if self.specialnum == 2:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage_special, self.handler, 15, 15))
                if self.specialnum == 3:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage_special, self.handler, 0, 15))
                if self.specialnum == 4:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage_special, self.handler, -15, 15))
                if self.specialnum == 5:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage_special, self.handler, -15, 0))
                if self.specialnum == 6:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage_special, self.handler, -15, -15))
                if self.specialnum == 7:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage_special, self.handler, 0, -15))
                if self.specialnum == 8:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage_special, self.handler, 15, -15))
            if self.special_duration.isDone():
                self.special_active = False
                self.gravity = self.startgravity
                self.sprite = self.stansprite
                self.sprite = self.stansprite
                self.special_cooldown.update()
            screen.blit(self.sprite, [self.rect.x, self.rect.y])
