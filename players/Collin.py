import pygame
from players.Player import Player


class Collin(Player):
    def __init__(self, x, y, handler):
        health = 120
        damage = 5
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
        self.left_attack1 = pygame.image.load("media/Players/Collin/CollinRangedLeft1.png").convert_alpha()
        self.left_attack2 = pygame.image.load("media/Players/Collin/CollinRangedLeft2.png").convert_alpha()
        self.right_attack1 = pygame.image.load("media/Players/Collin/CollinRangedRight1.png").convert_alpha()
        self.right_attack2 = pygame.image.load("media/Players/Collin/CollinRangedRight2.png").convert_alpha()

        # special

    def attack(self, screen):
        self.attacking = True

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True

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
            self.movespeed = 2
            targetPlayer = self.handler.getOtherPlayer(self)
            self.enemydistx = self.rect.x - targetPlayer.rect.x
            self.enemydisty = self.rect.y - targetPlayer.rect.y
            if self.facing == -1:
                if self.currenttick % 4 < 2:
                    screen.blit(self.left_attack1, (self.rect.x - 330, self.rect.y + 15))
                if self.currenttick % 4 >= 2:
                    screen.blit(self.left_attack2, (self.rect.x - 330, self.rect.y + 15))
                if 0 < self.enemydistx < 330 and 0 < self.enemydisty < 60:
                    if self.currenttick % 5 == 0:
                        self.handler.getPlayer2().takeDamage(self.damage)
            if self.facing == 1:
                if self.currenttick % 4 < 2:
                    screen.blit(self.right_attack1, (self.rect.x + self.width, self.rect.y + 15))
                if self.currenttick % 4 >= 2:
                    screen.blit(self.right_attack2, (self.rect.x + self.width, self.rect.y + 15))
                if 0 > self.enemydistx > -330 - self.width and 0 > self.enemydisty > -60:
                    if self.currenttick % 5 == 0:
                        self.handler.getPlayer2().takeDamage(self.damage)
        else:
            self.movespeed = 5
        self.currenttick += 1
