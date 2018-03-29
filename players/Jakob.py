import pygame
from players.Player import Player


class Jakob(Player):

    # TODO Give real data

    def __init__(self, x, y, handler, playNum):
        health = 100
        damage = 15
        winQuote = "Robotics taught me that"
        loseQuote = "I could've been watching Robotics competitions"
        name = "Jakob"
        movespeed = 5
        defense = .5

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

    def special(self):
        pass  # special here (reverses enemy controls)
