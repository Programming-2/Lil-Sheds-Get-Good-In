import pygame
from players.Player import Player


class Kyle(Player):
    def __init__(self, health, damage, winQuote, loseQuote, name, x, y, platArray, handler, playNum, defense):
        health = 100
        damage = 15
        winQuote = "Are the platforms fixed yet?"
        loseQuote = "I\'d better try to fix that... emphasis on try"
        name = "Kyle"

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, platArray, handler, playNum, defense)

    def special(self):
        pass  # special here (reflects attacks, own do less damage for duration)
