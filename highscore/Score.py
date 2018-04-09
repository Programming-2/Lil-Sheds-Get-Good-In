class Score:

    def __init__(self, name, wins, losses):
        self.name = name
        self.wins = wins
        self.losses = losses

    def getName(self):
        return self.name

    def getWins(self):
        return self.wins

    def setWins(self, newData):
        self.wins = newData

    def getLosses(self):
        return self.losses

    def setLosses(self, newData):
        self.losses = newData
