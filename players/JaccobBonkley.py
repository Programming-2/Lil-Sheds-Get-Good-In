from players.Player import Player


class JaccobBonkley(Player):

    # TODO Give real data

    def __init__(self, x, y, handler, playNum):
        health = 80
        damage = 25
        defense = .8
        winQuote = "Size doesn't mean everything"
        loseQuote = "It's my team's fault"
        name = "JaccobBonkley"

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, handler.getPlatformArray(), handler, playNum, defense)

        self.movespeed = 10
        self.playNum = playNum
        self.bullet_speed = 25
