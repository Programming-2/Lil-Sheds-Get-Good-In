import pygame
from players.Will import Will


class Handler:

    def __init__(self, screen, attackList, stateManager, platformArray, level, keyManager):
        self.attackList = attackList
        self.stateManager = stateManager
        self.platformArray = platformArray
        self.screen = screen
        self.done = False
        self.player1 = Will(0, 0, self)
        self.player2 = Will(0, 0, self)
        self.player1MoveSpeed = self.player1.movespeed
        self.player2MoveSpeed = self.player2.movespeed
        self.level = level
        self.projectileimage = pygame.image.load("media/Misc/projectileTest.png")
        self.keyManager = keyManager
        self.tick = 0

    def getAttackList(self):
        return self.attackList

    def setAttackList(self, list):
        self.attackList = list

    def getPlayer1(self):
        return self.player1

    def setPlayer1(self, player1):
        self.player1 = player1

    def getPlayer2(self):
        return self.player2

    def setPlayer2(self, player2):
        self.player2 = player2

    def getStateManager(self):
        return self.stateManager

    def getDone(self):
        return self.done

    def setDone(self, done):
        self.done = done

    def setPlatformArray(self, array):
        self.platformArray = array

    def getPlatformArray(self):
        return self.platformArray

    def getProjectileImage(self):
        return self.projectileimage

    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level = level

    def getPlayer1MoveSpeed(self):
        return self.player1MoveSpeed

    def setPlayer1MoveSpeed(self, player1MoveSpeed):
        self.player1MoveSpeed = player1MoveSpeed

    def getPlayer2MoveSpeed(self):
        return self.player2MoveSpeed

    def setPlayer2MoveSpeed(self, player2MoveSpeed):
        self.player2MoveSpeed = player2MoveSpeed

    def getOtherPlayer(self, currentPlayer):
        if currentPlayer == self.player1:
            return self.player2
        else:
            return self.player1

    def getKeyManager(self):
        return self.keyManager

    def updateTick(self):
        self.tick += 1

    def getTick(self):
        return self.tick