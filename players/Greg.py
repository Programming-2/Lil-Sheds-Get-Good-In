import pygame
from players.Player import Player
from src.Attack import Attack


class Greg(Player):

    # TODO Give real data

    def __init__(self, x, y, handler, playNum):
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
        self.damage_special = 5
        self.startgravity = self.gravity

    def special(self):
        if self.special_available:
            self.special_active = True

    def update(self, screen):
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
                seconds = (pygame.time.get_ticks() - self.start_time) / 1000
                self.xchange = 0
                self.ychange = 0
                self.gravity = 0
                self.handler.getAttackList().add(Attack(self.rect.x + self.width, self.rect.y + self.height - 50, 15, 0, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x - 30, self.rect.y + self.height - 50, -15, 0, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x + self.width / 2, self.rect.y + self.height, 0, 15, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x + self.width / 2, self.rect.y - 30, 0, -15, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x + self.width, self.rect.y + self.height, 10.65, 10.65, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x - 30, self.rect.y + self.height + 11, -10.65, 10.65, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x + self.width, self.rect.y - 30, 10.65, -10.65, "ranged", self.damage_special, 0, 0, screen, self.attacksprite, 20, self.handler))
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
