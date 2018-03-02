import pygame
from players.Player import Player


class David(Player):

    # TODO Give real data

    def __init__(self, x, y, handler, playNum):
        health = 150
        damage = 10
        winQuote = "I always start the party"
        loseQuote = "Zzz"
        name = "David"
        defense = .5

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, handler.getPlatformArray(), handler.getAttackList(), handler,
                         defense)

    def special(self):
        pass  # add special here (Puts enemy to sleep)
