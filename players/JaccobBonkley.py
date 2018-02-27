from players.Player import Player


class JaccobBonkley(Player):
    def __init__(self, x, y, platArray, handler, playNum):
        health = 80
        damage = 25
        defense = .9
        winQuote = "Size doesn't mean everything"
        loseQuote = "It's my team's fault"
        name = "JaccobBonkley"

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, platArray, handler, playNum, defense)

        self.movespeed = 10
        self.playNum = playNum
