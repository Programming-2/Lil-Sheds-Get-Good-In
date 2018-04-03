import pygame
from players.Player import Player
from src.Attack import Attack
from utils.Handler import Handler


class Greg(Player):

    # TODO Give real data

    def __init__(self, x, y, handler):
        health = 100
        damage = 15
        winQuote = "Broken like Katarina"
        loseQuote = "I don't even care"
        name = "Greg"
        movespeed = 5
        defense = .7

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.count = 0
        self.special_available = True
        self.special_active = False
        self.special_total_cooldown = 5
        self.special_cooldown = self.special_total_cooldown
        self.special_count = 0
        self.special_start_time = 0
        self.specialsprite = pygame.image.load("media\GregSpecial.png")
        self.specialframe1 = pygame.image.load("media\GregSpecial1.png")
        self.specialframe2 = pygame.image.load("media\GregSpecial2.png")
        self.specialnum = 1
        self.damage_special = 25
        self.startgravity = self.gravity
        self.attacking = False
        self.attackcount = 0
        self.attackradius = 150
        self.ranged_total_cooldown = 2
        self.ranged_cooldown = self.ranged_total_cooldown
        self.ranged_available = True
        self.ranged_count = 0
        self.ranged_start_time = 0

    def attack(self, screen):
        if self.ranged_available:
            self.attacking = True
            if self.facing == 1:
                if self.rect.x < 900:
                    self.rect.x += 200
                elif self.rect.x >= 900:
                    self.rect.x += (1100 - self.rect.x - self.width)
                if self.handler.getPlayer1().name == "Greg":
                    if self.attackradius + (self.width * .5) >= self.handler.getPlayer2().rect.x - self.rect.x >= -self.attackradius + (self.width * .5) and self.attackradius + (self.width * .5) >= self.handler.getPlayer2().rect.y - self.rect.y >= -self.attackradius + (self.width * .5):
                        self.handler.getPlayer2().takeDamage(25)
                elif self.handler.getPlayer2().name == "Greg":
                    if self.attackradius + (self.width * .5) >= self.handler.getPlayer1().rect.x - self.rect.x >= -self.attackradius + (self.height * .5) and self.attackradius + (self.width * .5) >= self.handler.getPlayer1().rect.y - self.rect.y >= -self.attackradius + (self.height * .5):
                        self.handler.getPlayer1().takeDamage(25)
            if self.facing == -1:
                if self.rect.x > 200:
                    self.rect.x -= 200
                elif self.rect.x <= 200:
                    self.rect.x = 0
                if self.handler.getPlayer1().name == "Greg":
                    if 150 >= self.handler.getPlayer2().rect.x - self.rect.x >= -150:
                        self.handler.getPlayer2().takeDamage(25)
                elif self.handler.getPlayer2().name == "Greg":
                    if 150 >= self.handler.getPlayer1().rect.x - self.rect.x >= -150:
                        self.handler.getPlayer1().takeDamage(25)
            self.ranged_available = False

    def special(self):
        if self.special_available:
            self.special_active = True

    def update(self, screen):
        if not self.ranged_available:
            self.ranged_cooldown = 0
            if self.ranged_count == 0:
                self.ranged_start_time = pygame.time.get_ticks()
                self.ranged_count = 1
            self.ranged_cooldown = (pygame.time.get_ticks() - self.ranged_start_time) / 1000
            if self.ranged_cooldown >= 2:
                self.ranged_available = True
                self.ranged_count = 0
        if self.attacking:
            if self.attackcount % 2 == 1:
                screen.blit(self.specialframe1, (self.rect.x - 125, self.rect.y - 125))
            if self.attackcount % 2 == 0:
                screen.blit(self.specialframe2, (self.rect.x - 125, self.rect.y - 125))
            self.attackcount += 1
            if self.attackcount > 4:
                self.attacking = False
                self.attackcount = 1
        self.screen = screen
        if not self.special_active:
            self.gravityUpdate()
            self.moveX()
            self.moveY()

            if self.xchange > 0:
                self.facing = 1
            elif self.xchange < 0:
                self.facing = -1

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
                self.specialnum += 1
                if self.specialnum > 8:
                    self.specialnum = 1
                seconds = (pygame.time.get_ticks() - self.start_time) / 1000
                self.xchange = 0
                self.ychange = 0
                self.gravity = 0
                if self.specialnum == 1:
                    self.handler.getAttackList().add(Attack(self.rect.x + self.width, self.rect.y + self.height - 50, 15, 0, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                if self.specialnum == 2:
                    self.handler.getAttackList().add(Attack(self.rect.x - 30, self.rect.y + self.height - 50, -15, 0, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                if self.specialnum == 3:
                    self.handler.getAttackList().add(Attack(self.rect.x + self.width / 2, self.rect.y + self.height, 0, 15, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                if self.specialnum == 4:
                    self.handler.getAttackList().add(Attack(self.rect.x + self.width / 2, self.rect.y - 30, 0, -15, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                if self.specialnum == 5:
                    self.handler.getAttackList().add(Attack(self.rect.x + self.width, self.rect.y + self.height, 10.65, 10.65, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                if self.specialnum == 6:
                    self.handler.getAttackList().add(Attack(self.rect.x - 30, self.rect.y + self.height + 11, -10.65, 10.65, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                if self.specialnum == 7:
                    self.handler.getAttackList().add(Attack(self.rect.x + self.width, self.rect.y - 30, 10.65, -10.65, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                if self.specialnum == 8:
                    self.handler.getAttackList().add(Attack(self.rect.x - 30, self.rect.y - 30, -10.65, -10.65, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
            if seconds > 1:
                self.special_active = False
                self.special_available = False
                self.gravity = self.startgravity
                self.sprite = self.stansprite
                self.count = 0
                self.sprite = self.stansprite

        screen.blit(self.sprite, [self.rect.x, self.rect.y])
        self.attackUpdate(screen)
