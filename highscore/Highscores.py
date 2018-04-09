from highscore.Score import Score


class Highscores:

    def __init__(self):
        self.orderedScores = []
        self.scores = {}

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

    def writeScores(self):
        # TODO Write scores to file
        pass
