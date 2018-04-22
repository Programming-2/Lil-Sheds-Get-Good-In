import pygame
from players.Player import Player
from dataStructures.CircularQueue import CircularQueue
from src.CustomAttack import CustomAttack
from src.Cooldown import Cooldown


class Collin(Player):
    def __init__(self, x, y, handler):
        health = 120
        damage = 10
        winQuote = "ROOOOOOSE"
        loseQuote = "at least I still have Kaitlin"
        name = "Collin"
        movespeed = 5
        defense = .6

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.handler = handler
        self.currenttick = 0
        # attacks
        self.damage = damage
        self.attacking = False
        self.enemydistx = 0
        self.enemydisty = 0
        # media
        left_attack1 = pygame.image.load("media/Players/Collin/CollinRangedLeft1.png").convert_alpha()
        left_attack2 = pygame.image.load("media/Players/Collin/CollinRangedLeft2.png").convert_alpha()
        right_attack1 = pygame.image.load("media/Players/Collin/CollinRangedRight1.png").convert_alpha()
        right_attack2 = pygame.image.load("media/Players/Collin/CollinRangedRight2.png").convert_alpha()
        self.leftAnimation = CircularQueue()
        self.leftAnimation.addData(left_attack1)
        self.leftAnimation.addData(left_attack2)
        self.rightAnimation = CircularQueue()
        self.rightAnimation.addData(right_attack1)
        self.rightAnimation.addData(right_attack2)
        self.rightAttImg = self.rightAnimation.get()
        self.leftAttImg = self.leftAnimation.get()

        # special
        self.special_sprite = pygame.image.load("media/Players/Collin/CollinSpecial.png")
        self.specialAnimation = CircularQueue()
        for i in range(0, 72):
            self.specialAnimation.addData(pygame.transform.rotate(self.special_sprite, i * 5))
        self.special_cooldown = Cooldown(5)
        self.special_damage = 50
        self.special_active = False

    def attack(self, screen):
        self.attacking = True

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True

    def update(self, screen):
        self.currenttick += 1
        # original
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

        # attacks
        if self.attacking and not self.released:
            self.movespeed = 2
            targetPlayer = self.handler.getOtherPlayer(self)
            self.enemydistx = self.rect.x - targetPlayer.rect.x
            self.enemydisty = self.rect.y - targetPlayer.rect.y
            if self.facing == -1:
                if self.currenttick % 4 == 0:
                    self.leftAttImg = self.leftAnimation.get()
                screen.blit(self.leftAttImg, (self.rect.x - 330, self.rect.y + 15))
                if 330 > self.enemydistx > 0 > self.enemydisty > -60:
                    if self.currenttick % 5 == 0:
                        targetPlayer.takeDamage(self.damage)
            if self.facing == 1:
                if self.currenttick % 4 == 0:
                    self.rightAttImg = self.rightAnimation.get()
                screen.blit(self.rightAttImg, (self.rect.x + self.width, self.rect.y + 15))
                if 0 > self.enemydistx > -330 - self.width and 0 > self.enemydisty > -60:
                    if self.currenttick % 5 == 0:
                        targetPlayer.takeDamage(self.damage)
        else:
            self.movespeed = 5

        if self.special_active and not self.stunned:
            if self.facing == 1:
                self.rose = CustomAttack(self, self.special_damage, self.handler, 5, -5, self.special_sprite, .15, self.specialAnimation)
                self.rose.rect.y -= 20
            elif self.facing == -1:
                self.rose = CustomAttack(self, self.special_damage, self.handler, -5, -5, self.special_sprite, .15, self.specialAnimation)
                self.rose.rect.y -= 20
            self.handler.getAttackList().add(self.rose)
            self.special_cooldown.update()
        if not self.special_cooldown.isDone():
            self.special_active = False
            self.special_cooldown.update()
