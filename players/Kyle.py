import pygame
from players.Player import Player


class Kyle(Player):

    # TODO Give real data

    def __init__(self, x, y, handler, playNum):
        health = 100
        damage = 15
        winQuote = "Are the platforms fixed yet?"
        loseQuote = "I\'d better try to fix that... emphasis on try"
        name = "Kyle"

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, handler.getPlatformArray(), handler, playNum, 0.5)

    def special(self):
        pass  # special here (reflects attacks, own do less damage for duration)
