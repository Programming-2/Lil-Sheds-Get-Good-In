import pygame
from players.Player import Player


class Collin(Player):
    def __init__(self, x, y, handler, playNum):
        health = 120
        damage = 20
        winQuote = "ROOOOOOSE"
        loseQuote = "at least I still have Kaitlin"
        name = "Collin"
        movespeed = 5
        defense = .6

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.handler = handler
        # attacks
        self.attacking = False
        self.enemydistx = 0
        self.enemydisty = 0

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
            '''if self.attacking:
                if self.handler.getPlayer1().name == "Collin":
                    self.enemydistx = self.rect.x - self.handler.getPlayer2().rect.x
                    if self.facing == 1 and:
                        self.handler.getPlayer2().takeDamage(20)'''
