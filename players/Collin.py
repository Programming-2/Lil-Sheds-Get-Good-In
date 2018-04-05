import pygame
from players.Player import Player


class Collin(Player):
    def __init__(self, x, y, handler):
        health = 120
        damage = 2
        winQuote = "ROOOOOOSE"
        loseQuote = "at least I still have Kaitlin"
        name = "Collin"
        movespeed = 5
        defense = .6

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.handler = handler
        # attacks
        self.damage = damage
        self.attacking = False
        self.enemydistx = 0
        self.enemydisty = 0
        self.left_attack = pygame.image.load("media/CollinRangedLeft.png")
        self.right_attack = pygame.image.load("media/CollinRangedRight.png")

    def attack(self, screen):
        self.attacking = True

    def update(self, screen):
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
            if self.handler.getPlayer1().name == "Collin":
                self.enemydistx = self.rect.x - self.handler.getPlayer2().rect.x
                self.enemydisty = self.rect.y - self.handler.getPlayer2().rect.y
                if self.facing == -1:
                    screen.blit(self.left_attack, (self.rect.x - 330, self.rect.y + 15))
                    if 0 < self.enemydistx < 330 and 0 < self.enemydisty < 60:
                        self.handler.getPlayer2().takeDamage(self.damage)
                if self.facing == 1:
                    screen.blit(self.right_attack, (self.rect.x + self.width, self.rect.y + 15))
                    if 0 > self.enemydistx > -330 and 0 > self.enemydisty > -60:
                        self.handler.getPlayer2().takeDamage(self.damage)
            if self.handler.getPlayer2().name == "Collin":
                self.enemydistx = self.rect.x - self.handler.getPlayer1().rect.x
                self.enemydisty = self.rect.y - self.handler.getPlayer1().rect.y
                if self.facing == -1:
                    screen.blit(self.left_attack, (self.rect.x - 330, self.rect.y + 15))
                    if 0 < self.enemydistx < 330 and 0 < self.enemydisty < 60:
                        self.handler.getPlayer1().takeDamage(self.damage)
                if self.facing == 1:
                    screen.blit(self.right_attack, (self.rect.x + self.width, self.rect.y + 15))
                    if 0 > self.enemydistx > -330 and 0 > self.enemydisty > -60:
                        self.handler.getPlayer1().takeDamage(self.damage)
