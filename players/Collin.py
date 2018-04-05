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
