import pygame
from players.Player import Player


class David(Player):
    def __init__(self, x, y, platArray, handler, playNum):
        health = 150
        damage = 10
        winQuote = "I always start the party"
        loseQuote = "Zzz"
        name = "David"
        defense = .5

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, platArray, handler, playNum, defense)

    def special(self):
        pass  # add special here (Puts enemy to sleep)
