import pygame
from players.Player import Player
from utils.Handler import Handler


class David(Player):

    # TODO Give real data

    def __init__(self, x, y, handler, playNum):
        health = 150
        damage = 10
        winQuote = "I always start the party"
        loseQuote = "Zzz"
        name = "David"
        defense = .5
        self.handler = handler

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, handler.getPlatformArray(), handler.getAttackList(), handler,
                         defense)
        self.attacksprite = pygame.image.load("media/DavidAttack.png")
        self.special_cooldown = 0
        self.special_active = False
        self.special_available = True
        self.playNum = playNum

    def special(self):
        if self.playNum == 1:
            self.handler.setPlayer2MoveSpeed(0)
        if self.playNum == 2:
            self.handler.setPlayer1MoveSpeed(0)