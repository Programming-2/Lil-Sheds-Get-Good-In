import pygame
from attack import Attack
from players.Player import Player


class Will(Player):
    def __init__(self, x, y, platArray, handler, playNum):
        health = 110
        damage = 15
        winQuote = "yikes"
        loseQuote = "yikes"
        name = "Will"
        defense = .5

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, platArray, handler, playNum, defense)

        self.special_active = False
        self.count = 0
        self.start_time = 0
        self.startgravity = self.gravity
        self.startdefense = defense
        self.specialsprite = pygame.image.load("media/WillSpecial.png")
        self.attacksprite = pygame.image.load("media/projectileTest.png")
        self.rangedcount = 0
        self.rangedavailable = True
        self.rangedstarttime = 0
        self.rangedcooldown = 0
        self.damage_special = 1.5 * damage
        self.special_available = True
        self.special_cooldown = 0
        self.special_total_cooldown = 5
        self.special_count = 0
        self.special_start_time = 0

    def special(self):
        if self.special_available:
            self.special_active = True

    def attack(self, image, screen, player):
        if self.rangedavailable:
            if self.facing == -1:
                self.handler.getAttackList().add(Attack(self.x - 25, self.y, 15 * self.facing, 2, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                self.handler.getAttackList().add(Attack(self.x - 25, self.y, 15 * self.facing, 1, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                self.handler.getAttackList().add(Attack(self.x - 25, self.y, 15 * self.facing, 0, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                self.handler.getAttackList().add(Attack(self.x - 25, self.y, 15 * self.facing, -1, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                self.handler.getAttackList().add(Attack(self.x - 25, self.y, 15 * self.facing, -2, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                self.rangedavailable = False
            elif self.facing == 1:
                self.handler.getAttackList().add(Attack(self.x + self.width + 5, self.y, 15 * self.facing, 2, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                self.handler.getAttackList().add(Attack(self.x + self.width + 5, self.y, 15 * self.facing, 1, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                self.handler.getAttackList().add(Attack(self.x + self.width + 5, self.y, 15 * self.facing, 0, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                self.handler.getAttackList().add(Attack(self.x + self.width + 5, self.y, 15 * self.facing, -1, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
                self.handler.getAttackList().add(Attack(self.x + self.width + 5, self.y, 15 * self.facing, -2, "ranged", 1, 3, 5, screen, image, 20, self.handler, player))
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

        if not self.special_available:
            self.special_cooldown = 0
            if self.special_count == 0:
                self.special_start_time = pygame.time.get_ticks()
                self.special_count = 1
            self.special_cooldown = (pygame.time.get_ticks() - self.special_start_time) / 1000
            if self.special_cooldown >= self.special_total_cooldown:
                self.special_available = True
                self.special_count = 0

        if self.special_active and not self.sleeping:
            self.sprite = self.specialsprite
            if self.count == 0:
                self.start_time = pygame.time.get_ticks()
                self.count += 1
            seconds = 0
            if seconds <= 1:
                self.rangedavailable = False
                seconds = (pygame.time.get_ticks() - self.start_time) / 1000
                print("Current time: " + str(seconds))
                self.xchange = 0
                self.ychange = 0
                self.defense = 0
                self.gravity = 0
            if seconds > 1:
                self.special_available = False
                self.handler.getAttackList().add(Attack(self.x + self.width, self.y + self.height - 50, 15, 0, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler, self.playNum))
                self.handler.getAttackList().add(Attack(self.x - 20, self.y + self.height - 50, -15, 0, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler, self.playNum))
                self.handler.getAttackList().add(Attack(self.x + self.width / 2, self.y + self.height, 0, 15, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler, self.playNum))
                self.handler.getAttackList().add(Attack(self.x + self.width / 2, self.y - 20, 0, -15, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler, self.playNum))
                self.handler.getAttackList().add(Attack(self.x + self.width, self.y + self.height, 10.65, 10.65, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler, self.playNum))
                self.handler.getAttackList().add(Attack(self.x - 20, self.y + self.height, -10.65, 10.65, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler, self.playNum))
                self.handler.getAttackList().add(Attack(self.x + self.width, self.y - 20, 10.65, -10.65, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler, self.playNum))
                self.handler.getAttackList().add(Attack(self.x - 20, self.y - 20, -10.65, -10.65, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler, self.playNum))
                self.special_active = False
                self.gravity = self.startgravity
                self.defense = self.startdefense
                self.sprite = self.stansprite
                self.rangedavailable = True
                self.count = 0

        if self.playNum == 1:
            if pygame.sprite.spritecollide(self.handler.getPlayer2(), self.handler.getAttackList(), False):
                self.handler.getPlayer2().takeDamage(self.damage)
                pygame.sprite.spritecollide(self.handler.getPlayer2(), self.handler.getAttackList(), True)
        if self.playNum == 2:
            if pygame.sprite.spritecollide(self.handler.getPlayer1(), self.handler.getAttackList(), False):
                self.handler.getPlayer1().takeDamage(self.damage)
                pygame.sprite.spritecollide(self.handler.getPlayer1(), self.handler.getAttackList(), True)

        screen.blit(self.sprite, [self.x, self.y])
