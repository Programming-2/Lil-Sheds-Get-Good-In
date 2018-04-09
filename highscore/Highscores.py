from highscore.Score import Score


class Highscores:

    def __init__(self):
        self.orderedScores = []
        self.scores = {}
        self.loadScores()

    def updateUser(self, name, wins, losses):
        if name in self.scores:
            self.scores.get(name).setWins(wins)
            self.scores.get(name).setLosses(losses)
        else:
            self.scores[name] = Score(name, wins, losses)

        if name in self.orderedScores:
            self.orderedScores.remove(name)

        compWinPercent = wins / losses
        for i in range(0, len(self.orderedScores)):
            winPercent = self.scores[self.orderedScores[i]].getWins() / self.scores[self.orderedScores[i]].getLosses()
            if compWinPercent > winPercent:
                self.orderedScores.insert(i, name)
                return

        self.orderedScores.append(name)

    def loadScores(self):
        try:
            file = open("highscores.txt", "r")
        except FileNotFoundError:
            return
        line = file.readline()
        while not line == "":
            line = line.split(" ")
            name = line[0]
            wins = line[1]
            losses = line[2]
            self.orderedScores.append(name)
            self.scores[name] = Score(name, int(wins), int(losses))
            line = file.readline()
        file.close()

    def writeScores(self):
        file = open("highscores.txt", "w")
        for name in reversed(self.orderedScores):
            wins = self.scores.get(name).getWins()
            losses = self.scores.get(name).getLosses()
            file.write(name + " " + str(wins) + " " + str(losses) + "\n")
        file.close()
