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

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, platArray, handler, defense)

        self.special_active = False
        self.count = 0
        self.start_time = 0
        self.startgravity = self.gravity
        self.startdefense = defense
        self.specialsprite = pygame.image.load("media/WillSpecial.png")
        self.attacksprite = pygame.image.load("media/projectileTest.png")
        self.enemy = enemy
        self.rangedcount = 0
        self.rangedavailable = True
        self.rangedstarttime = 0
        self.rangedcooldown = 0
        self.playerNum = playNum

    def special(self):
        self.special_active = True

    def attack(self, image, screen, player):
        if self.rangedavailable:
            if self.ychange > 0 and self.xchange == 0:
                self.handler.getAttackList().add(Attack(self.x + self.width / 2, self.y + self.height + 5, 3, 15, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(1)
                self.handler.getAttackList().add(Attack(self.x + self.width / 2, self.y + self.height + 5, 1, 15, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(1)
                self.handler.getAttackList().add(Attack(self.x + self.width / 2, self.y + self.height + 5, -1, 15, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(1)
                self.handler.getAttackList().add(Attack(self.x + self.width / 2, self.y + self.height + 5, -3, 15, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(1)
                self.rangedavailable = False
            elif self.ychange < 0 and self.xchange == 0:
                self.handler.getAttackList().add(Attack(self.x + self.width / 2, self.y - 5, 3, -15, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(2)
                self.handler.getAttackList().add(Attack(self.x + self.width / 2, self.y - 5, 1, -15, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(2)
                self.handler.getAttackList().add(Attack(self.x + self.width / 2, self.y - 5, -1, -15, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(2)
                self.handler.getAttackList().add(Attack(self.x + self.width / 2, self.y - 5, -3, -15, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(2)
                self.rangedavailable = False
            elif self.facing == -1:
                self.handler.getAttackList().add(Attack(self.x - 25, self.y, 15 * self.facing, 3, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(3)
                self.handler.getAttackList().add(Attack(self.x - 25, self.y, 15 * self.facing, 1, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(3)
                self.handler.getAttackList().add(Attack(self.x - 25, self.y, 15 * self.facing, -1, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(3)
                self.handler.getAttackList().add(Attack(self.x - 25, self.y, 15 * self.facing, -3, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(3)
                self.rangedavailable = False
            elif self.facing == 1:
                self.handler.getAttackList().add(Attack(self.x + self.width + 5, self.y, 15 * self.facing, 3, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(4)
                self.handler.getAttackList().add(Attack(self.x + self.width + 5, self.y, 15 * self.facing, 1, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(4)
                self.handler.getAttackList().add(Attack(self.x + self.width + 5, self.y, 15 * self.facing, -1, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(4)
                self.handler.getAttackList().add(Attack(self.x + self.width + 5, self.y, 15 * self.facing, -3, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                print(4)
                self.rangedavailable = False

    def update(self, screen):
        if not self.special_active:
            self.gravityUpdate()
            self.moveX()
            self.moveY()

            if self.xchange > 0:
                self.facing = 1
            elif self.xchange < 0:
                self.facing = -1

            if not self.rangedavailable:
                self.rangedcooldown = 0
                if self.rangedcount == 0:
                    self.rangedstarttime = pygame.time.get_ticks()
                    self.rangedcount = 1
                self.rangedcooldown = (pygame.time.get_ticks() - self.rangedstarttime) / 1000
                if self.rangedcooldown >= .75:
                    self.rangedavailable = True
                    self.rangedcount = 0

        if self.special_active:
            self.sprite = self.specialsprite
            if self.count == 0:
                self.start_time = pygame.time.get_ticks()
                self.count += 1
            seconds = 0
            if seconds <= 2:
                self.rangedavailable = False
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
                self.rangedavailable = True

        screen.blit(self.sprite, [self.x, self.y])
