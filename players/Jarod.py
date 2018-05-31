import pygame
from src.Attack import Attack
from src.CustomAttack import CustomAttack
from players.Player import Player
from src.Cooldown import Cooldown
import random


class Jarod(Player):

    def __init__(self, x, y, handler):
        health = 110
        damage = 8
        win_quote = "yikes"
        lose_quote = "yikes"
        name = "Jarod"
        defense = .5
        movespeed = 5

        super().__init__(health, damage, win_quote, lose_quote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.special_active = False
        self.special_available = False
        self.special_cooldown = Cooldown(5)
        self.damage = damage
        self.rangedavailable = False
        self.released = True
        self.tick = 0

    def special(self):
        pass

    def attack(self, screen):
        self.rangedavailable = True

    def update(self, screen):
        if self.tick != 0:
            self.xchange /= 2

        super().update(screen)

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()

        if self.rangedavailable and not self.released:
            self.tick += 1
            self.ranged_cooldown.current_cooldown = self.tick / 60
            if self.ranged_cooldown.current_cooldown <= 1:
                if self.tick % 15 == 0:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 12 * self.facing, 0))
            elif self.ranged_cooldown.current_cooldown <= 2:
                if self.tick % 12 == 0:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 12 * self.facing, random.randint(-1, 1)))
            elif self.ranged_cooldown.current_cooldown <= 3:
                if self.tick % 8 == 0:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 12 * self.facing, random.randint(-1, 1)))
            elif self.ranged_cooldown.current_cooldown <= 4:
                if self.tick % 6 == 0:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 12 * self.facing, random.randint(-2, 2)))
            elif self.ranged_cooldown.current_cooldown > 4:
                if self.tick % 4 == 0:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 12 * self.facing, random.randint(-2, 2)))
        else:
            self.tick = 0
