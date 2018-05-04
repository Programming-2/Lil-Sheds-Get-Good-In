import pygame

class MeleeAttack():
    def __init__(self, damage, player, handler):
        self.damage = damage
        self.handler = handler
        self.player = player
        self.attackrange = 100
        self.lfist = pygame.transform.rotate(pygame.image.load("media/Misc/fist.png").convert_alpha(), 90)
        self.rfist = pygame.transform.flip(self.lfist, True, False)

    def attack(self, screen):
        if self.player.facing == 1:
            if self.handler.getPlayer1().name == self.player.name:
                screen.blit(self.rfist, [self.handler.getPlayer1().rect.x + self.handler.getPlayer1().width + 5, self.handler.getPlayer1().rect.y + 20])
                if 0 < self.handler.getPlayer2().rect.x - self.player.rect.x < self.attackrange and -self.player.height <= self.handler.getPlayer2().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer2().takeDamage(self.damage)
                elif -self.attackrange > self.handler.getPlayer2().rect.x - self.player.rect.x > 0 and 0 < self.handler.getPlayer2().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer2().takeDamage(self.damage)
            if self.handler.getPlayer2().name == self.player.name:
                screen.blit(self.rfist, [self.handler.getPlayer2().rect.x + self.handler.getPlayer2().width + 5, self.handler.getPlayer2().rect.y + 20])
                if 0 < self.handler.getPlayer1().rect.x - self.player.rect.x < self.attackrange and -self.player.height <= self.handler.getPlayer1().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer1().takeDamage(self.damage)
                elif -self.attackrange > self.handler.getPlayer1().rect.x - self.player.rect.x > 0 and 0 < self.handler.getPlayer1().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer1().takeDamage(self.damage)

        if self.player.facing == -1:
            if self.handler.getPlayer1().name == self.player.name:
                screen.blit(self.lfist, [self.handler.getPlayer1().rect.x - 25, self.handler.getPlayer1().rect.y + 20])
                if 0 > self.handler.getPlayer2().rect.x - self.player.rect.x > -self.attackrange and -self.player.height <= self.handler.getPlayer2().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer2().takeDamage(self.damage)
                elif self.attackrange < self.handler.getPlayer2().rect.x - self.player.rect.x < 0 and 0 > self.handler.getPlayer2().rect.y - self.player.rect.y > -self.player.height:
                    self.handler.getPlayer2().takeDamage(self.damage)
            if self.handler.getPlayer2().name == self.player.name:
                screen.blit(self.lfist, [self.handler.getPlayer2().rect.x - 25, self.handler.getPlayer2().rect.y + 20])
                if 0 > self.handler.getPlayer1().rect.x - self.player.rect.x > -self.attackrange and -self.player.height <= self.handler.getPlayer1().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer1().takeDamage(self.damage)
                elif self.attackrange < self.handler.getPlayer1().rect.x - self.player.rect.x < 0 and 0 < self.handler.getPlayer1().rect.y - self.player.rect.y < self.player.height:
                    self.handler.getPlayer1().takeDamage(self.damage)
