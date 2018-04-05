import pygame
from players.Player import Player


class Shed(Player):

    # TODO Give real data

    def __init__(self, x, y, handler):
        health = 170
        damage = 5
        winQuote = "Robotics taught me that"
        loseQuote = "I could've been watching Robotics competitions"
        name = "Jakob"
        movespeed = 5
        defense = .7

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

    def special(self):
        pass  # special here (reverses enemy controls)
