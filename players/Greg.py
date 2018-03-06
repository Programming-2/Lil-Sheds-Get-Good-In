import pygame
from players.Player import Player


class Greg(Player):

    # TODO Give real data

    def __init__(self, x, y, handler, playNum):
        health = 100
        damage = 15
        winQuote = "Broken like Katarina"
        loseQuote = "I don't even care"
        name = "Greg"

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, handler.getPlatformArray(), handler.getAttackList(), handler, 0.5)

    def special(self):
        pass  # special here (reverses enemy controls)
