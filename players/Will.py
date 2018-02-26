import pygame
from players.Player import Player


class Will(Player):
    def __init__(self, x, y, platArray, handler, defense, playNum):
        health = 100
        damage = 15
        winQuote = "yikes"
        loseQuote = "yikes"
        name = "Will"

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, platArray, handler, defense, playNum)

    def special(self):
        count = 0
        if count == 0:
            start_time = pygame.time.get_ticks()
            count += 1
        seconds = 0
        while seconds <= 2:
            seconds = (pygame.time.get_ticks() - start_time) / 1000
            print("Current time: " + str(seconds))
            self.xchange = 0
            self.ychange = 0
            self.defense = 0
