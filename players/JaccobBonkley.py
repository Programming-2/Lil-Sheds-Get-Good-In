from players.Player import Player


class JaccobBonkley(Player):

    # TODO Give real data

    def __init__(self, x, y, handler, playNum):
        health = 70
        damage = 20
        defense = .9
        movespeed = 10
        winQuote = "Size doesn't mean everything"
        loseQuote = "It's my team's fault"
        name = "JaccobBonkley"

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.playNum = playNum
        self.bullet_speed = 20
