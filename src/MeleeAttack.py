class MeleeAttack():
    def __init__(self, damage, player, handler):
        self.damage = damage
        self.handler = handler
        self.player = player
        self.attackrange = 100

    def attack(self):
        if self.player.facing == 1:
            if self.handler.getPlayer1().name == self.player.name:
                if 0 < self.handler.getPlayer2().rect.x - self.player.rect.x < self.attackrange and -self.player.height <= self.handler.getPlayer2().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer2().takeDamage(self.damage)
                elif -self.attackrange > self.handler.getPlayer2().rect.x - self.player.rect.x > 0 and 0 < self.handler.getPlayer2().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer2().takeDamage(self.damage)
            if self.handler.getPlayer2().name == self.player.name:
                if 0 < self.handler.getPlayer1().rect.x - self.player.rect.x < self.attackrange and -self.player.height <= self.handler.getPlayer1().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer1().takeDamage(self.damage)
                elif -self.attackrange > self.handler.getPlayer1().rect.x - self.player.rect.x > 0 and 0 < self.handler.getPlayer1().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer1().takeDamage(self.damage)

        if self.player.facing == -1:
            if self.handler.getPlayer1().name == self.player.name:
                if 0 > self.handler.getPlayer2().rect.x - self.player.rect.x > -self.attackrange and -self.player.height <= self.handler.getPlayer2().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer2().takeDamage(self.damage)
                elif self.attackrange < self.handler.getPlayer2().rect.x - self.player.rect.x < 0 and 0 > self.handler.getPlayer2().rect.y - self.player.rect.y > -self.player.height:
                    self.handler.getPlayer2().takeDamage(self.damage)
            if self.handler.getPlayer2().name == self.player.name:
                if 0 > self.handler.getPlayer1().rect.x - self.player.rect.x > -self.attackrange and -self.player.height <= self.handler.getPlayer1().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer1().takeDamage(self.damage)
                elif self.attackrange < self.handler.getPlayer1().rect.x - self.player.rect.x < 0 and 0 < self.handler.getPlayer1().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer1().takeDamage(self.damage)
