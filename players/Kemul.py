import pygame
from players.Player import Player
from src.Cooldown import Cooldown


class Kemul(Player):

    def __init__(self, x, y, handler):
        health = 110
        damage = 20
        win_quote = "Chewbacca"
        lose_quote = "Chewbacca"
        name = "Kemul"
        defense = .7
        movespeed = 5

        super().__init__(health, damage, win_quote, lose_quote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.special_active = False
        self.special_cooldown = Cooldown(3)
        self.special_duration = Cooldown(2)
        self.caravan_sprite = pygame.image.load("media/Players/Kemul/Kemul 2.png").convert_alpha()
        self.caravan_x = 1100
        self.caravan_y = 0
        self.caravan_loaded = True

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True
            self.caravan_y = self.handler.getOtherPlayer(self).rect.y

    def update(self, screen):
        super().update(screen)

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()

        if self.special_active and not self.sleeping:
            self.special_duration.update()
            if not self.special_duration.isDone():
                self.caravan_x -= 20
                screen.blit(self.caravan_sprite, [self.caravan_x, self.caravan_y])
                if -15 < (self.handler.getOtherPlayer(self).rect.x - self.caravan_x) < 15 and -15 < (self.handler.getOtherPlayer(self).rect.y - self.caravan_y) < 15 and self.caravan_loaded:
                    self.handler.getOtherPlayer(self).takeDamage(20)
                    self.caravan_loaded = False
            else:
                self.special_active = False
                self.caravan_x = 1100
                self.caravan_loaded = True
                self.special_cooldown.update()
