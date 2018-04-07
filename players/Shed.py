import pygame
from players.Player import Player
from src.Cooldown import Cooldown


class Shed(Player):

    def __init__(self, x, y, handler):
        health = 200
        damage = 20
        winQuote = "Robotics taught me that"
        loseQuote = "I could've been watching Robotics competitions"
        name = "Lil' Shed"
        movespeed = 5
        defense = .7

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        # Misc
        self.current_tick = 0
        self.jump_pressed = False
        self.duck_pressed = False

        # Ranged
        self.ranged_cooldown = Cooldown(0.5)

        # Special
        self.special_cooldown = Cooldown(8)
        self.special_active = False

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True

    def jump(self):
        self.jump_pressed = True

    def duck(self):
        self.duck_pressed = True

    def unduck(self):
        pass

    def update(self, screen):
        self.screen = screen
        self.moveX()
        self.moveY()
        screen.blit(self.sprite, [self.rect.x, self.rect.y])

        if self.xchange > 0:
            self.facing = 1
        elif self.xchange < 0:
            self.facing = -1

        if self.jump_pressed and not self.jumpreleased:
            self.ychange -= 0.25
        if self.duck_pressed and not self.duckreleased:
            self.ychange += 0.25
        if self.jumpreleased and self.ychange < 0:
            self.ychange += 0.25
        if self.duckreleased and self.ychange > 0:
            self.ychange -= 0.25
