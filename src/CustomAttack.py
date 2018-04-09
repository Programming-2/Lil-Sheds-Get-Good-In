import pygame
from src.Attack import Attack


class CustomAttack(Attack):
    def __init__(self, player, damage, handler, x_speed, y_speed):
        self.player = player
        self.damage = damage
        self.handler = handler
        super().__init__(self.player, self.damage, self.handler)

        self.changex = x_speed
        self.changey = y_speed
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y
