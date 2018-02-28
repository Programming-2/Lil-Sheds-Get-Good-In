import pygame
from players.Player import Player


class Jakob(Player):
    def __init__(self, health, damage, winQuote, loseQuote, name, x, y, platArray, handler, playNum, defense):
        health = 100
        damage = 15
        winQuote = "Robotics taught me that"
        loseQuote = "I could've been watching Robotics competitions"
        name = "Jakob"

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, platArray, handler, playNum, defense)

    def special(self):
        pass  # special here (reverses enemy controls)
