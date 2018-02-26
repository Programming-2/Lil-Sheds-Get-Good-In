from states.StateManager import StateManager

class Handler:

    def __init__(self, attackList, stateManager):
        self.attackList = attackList
        self.stateManager = stateManager
        self.done = False
        self.player1 = 0
        self.player2 = 0

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
