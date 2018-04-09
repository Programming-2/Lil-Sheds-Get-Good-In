from highscore.Highscores import Highscores

h = Highscores()
h.updateUser("Jakob", 10, 3)
h.updateUser("Will", 8, 5)
h.updateUser("Kyle", 6, 8)
h.updateUser("Dave", 5, 2)
h.updateUser("Jakob", 11, 3)
h.updateUser("Will", 8, 6)
h.updateUser("Dave", 10, 2)
h.writeScores()
