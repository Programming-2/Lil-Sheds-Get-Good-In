import pygame
import random
from attack import Attack
from players.Player import Player


class Will(Player):
    def __init__(self, x, y, platArray, handler, playNum, enemy):
        health = 100
        damage = 15
        winQuote = "yikes"
        loseQuote = "yikes"
        name = "Will"
        defense = .8

        super().__init__(health, winQuote, loseQuote, name, x, y, platArray, handler, defense)

        self.special_active = False
        self.count = 0
        self.start_time = 0
        self.startgravity = self.gravity
        self.startdefense = defense
        self.specialsprite = pygame.image.load("media/WillSpecial.png")
        self.attacksprite = pygame.image.load("media/projectileTest.png")
        self.enemy = enemy

    def special(self):
        self.special_active = True

    def update(self, screen):
        if not self.special_active:
            self.gravityUpdate()
            self.moveX()
            self.moveY()

            if self.xchange > 0:
                self.facing = 1
            elif self.xchange < 0:
                self.facing = -1

        if self.special_active:
            self.sprite = self.specialsprite
            if self.count == 0:
                self.start_time = pygame.time.get_ticks()
                self.count += 1
            seconds = 0
            if seconds <= 2:
                seconds = (pygame.time.get_ticks() - self.start_time) / 1000
                print("Current time: " + str(seconds))
                self.xchange = 0
                self.ychange = 0
                self.defense = 0
                self.gravity = 0
                self.handler.getAttackList().add(Attack(self.x + self.width / 2, self.y + self.height - 50, random.randint(-10, 10), random.randint(-5, 5), "ranged", self.damage, 0, 0, screen, self.attacksprite, 20, self.handler, self.playerNum))
                if pygame.sprite.spritecollide(self.enemy, self.handler.getAttackList(), False):
                    self.enemy.takeDamage(self.damage)
                    pygame.sprite.spritecollide(self.enemy, self.handler.getAttackList(), True)
            if seconds > 2:
                self.special_active = False
                self.count = 0
                self.gravity = self.startgravity
                self.defense = self.startdefense
                self.sprite = self.stansprite

        screen.blit(self.sprite, [self.x, self.y])
