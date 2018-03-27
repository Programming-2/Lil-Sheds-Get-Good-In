import pygame
from src.Attack import Attack
from players.Player import Player


class Will(Player):

    # TODO Give real data

    def __init__(self, x, y, handler):
        health = 110
        damage = 55
        winQuote = "yikes"
        loseQuote = "yikes"
        name = "Will"
        defense = .5
        movespeed = 5

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.special_active = False
        self.count = 0
        self.start_time = 0
        self.startgravity = self.gravity
        self.startdefense = defense
        self.specialsprite = pygame.image.load("media/WillSpecial.png")
        self.attacksprite = pygame.image.load("media/Will/Attack3.png")
        self.attack1 = pygame.image.load("media/Will/Attack1.png")
        self.attack2 = pygame.image.load("media/Will/Attack2.png")
        self.attack3 = pygame.image.load("media/Will/Attack3.png")
        self.attack4 = pygame.image.load("media/Will/Attack4.png")
        self.rangedcount = 0
        self.rangedavailable = False
        self.rangedstarttime = 0
        self.rangedendtime = 0
        self.rangedcooldown = 0
        self.attackavailable = False
        self.damage_special = 1.5 * damage
        self.special_available = True
        self.special_total_cooldown = 5
        self.special_cooldown = self.special_total_cooldown
        self.special_count = 0
        self.special_start_time = 0
        self.released = False
        self.damage = damage

    def special(self):
        if self.special_available:
            self.special_active = True

    def attack(self, screen):
        self.rangedavailable = True

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
                self.rangedavailable = False
                seconds = (pygame.time.get_ticks() - self.start_time) / 1000
                self.xchange = 0
                self.ychange = 0
                self.defense = 0
                self.gravity = 0
            if seconds > 1:
                self.special_available = False
                self.handler.getAttackList().add(Attack(self.rect.x + self.width, self.rect.y + self.height - 50, 15, 0, "ranged", self.damage_special, 0, 0, screen, self.attack3, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x - 30, self.rect.y + self.height - 50, -15, 0, "ranged", self.damage_special, 0, 0, screen, self.attack3, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x + self.width / 2, self.rect.y + self.height, 0, 15, "ranged", self.damage_special, 0, 0, screen, self.attack3, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x + self.width / 2, self.rect.y - 30, 0, -15, "ranged", self.damage_special, 0, 0, screen, self.attack3, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x + self.width, self.rect.y + self.height, 10.65, 10.65, "ranged", self.damage_special, 0, 0, screen, self.attack3, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x - 30, self.rect.y + self.height + 11, -10.65, 10.65, "ranged", self.damage_special, 0, 0, screen, self.attack3, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x + self.width, self.rect.y - 30, 10.65, -10.65, "ranged", self.damage_special, 0, 0, screen, self.attack3, 20, self.handler))
                self.handler.getAttackList().add(Attack(self.rect.x - 30, self.rect.y - 30, -10.65, -10.65, "ranged", self.damage_special, 0, 0, screen, self.attack3, 20, self.handler))
                self.special_active = False
                self.gravity = self.startgravity
                self.defense = self.startdefense
                self.sprite = self.stansprite
                self.count = 0

        if self.rangedavailable:
            secondsheld = (self.rangedendtime - self.rangedstarttime) / 1000
            if secondsheld <= 1 and self.released:
                self.damage = 10
                self.bullet_speed = 10
                self.attacksprite = self.attack1
                self.attackavailable = True
            elif secondsheld <= 2 and self.released:
                self.damage = 25
                self.bullet_speed = 15
                self.attacksprite = self.attack2
                self.attackavailable = True
            elif secondsheld <= 3 and self.released:
                self.damage = 60
                self.bullet_speed = 20
                self.attacksprite = self.attack3
                self.attackavailable = True
            elif secondsheld <= 4 and self.released:
                self.damage = 120
                self.bullet_speed = 25
                self.attacksprite = self.attack4
                self.attackavailable = True
            elif secondsheld > 4 and self.released:
                self.damage = secondsheld * 40
                self.bullet_speed = 30
                self.attacksprite = self.attack4
                self.attackavailable = True
            if self.attackavailable:
                if self.facing == -1:
                    self.handler.getAttackList().add(Attack(self.rect.x - 25, self.rect.y, self.bullet_speed * self.facing, 0, "ranged", self.damage, 3, 5, self.screen, self.attacksprite, 20, self.handler))
                    self.rangedavailable = False
                    self.attackavailable = False
                elif self.facing == 1:
                    self.handler.getAttackList().add(Attack(self.rect.x + self.width + 5, self.rect.y, self.bullet_speed * self.facing, 0, "ranged", self.damage, 3, 5, self.screen, self.attacksprite, 20, self.handler))
                    self.rangedavailable = False
                    self.attackavailable = False

        screen.blit(self.sprite, [self.rect.x, self.rect.y])
        self.attackUpdate(screen)
