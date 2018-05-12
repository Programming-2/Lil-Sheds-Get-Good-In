import pygame
from players.Player import Player
from src.Cooldown import Cooldown


class PlayerTemplate(Player):

    def __init__(self, x, y, handler):
        health = 100
        damage = 10
        winQuote = "Win Quote"
        loseQuote = "Lose quote"
        name = "Name"
        movespeed = 5
        defense = .5
        self.handler = handler

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(),
                         handler.getAttackList(), handler, defense)

    def special(self):
        pass

    def update(self, screen):
        self.moveX()
        self.moveY()
        self.gravityUpdate()

        if self.xchange > 0:
            self.facing = 1
        elif self.xchange < 0:
            self.facing = -1

        screen.blit(self.sprite, [self.rect.x, self.rect.y])
