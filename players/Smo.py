import pygame
from src.Attack import Attack
from src.CustomAttack import CustomAttack
from players.Player import Player
from src.Cooldown import Cooldown
from utils.Sound import Sound
from datastructures.CircularQueue import CircularQueue


class Smo(Player):

    def __init__(self, x, y, handler):
        health = 110
        damage = 55
        winQuote = "up to the board"
        loseQuote = "this will delay my victory"
        name = "Smo"
        defense = .5
        movespeed = 5

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.special_active = False
        self.special_range =  50
        self.startdefense = defense
        self.rangedcount = 0
        self.rangedavailable = False
        self.attackavailable = False
        self.special_available = True
        self.special_cooldown = Cooldown(5)
        self.special_duration = Cooldown(1)
        self.damage = damage

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True

    def attack(self, screen):
        self.rangedavailable = True

    def update(self, screen):
        super().update(screen)

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()

        if self.special_active and not self.sleeping:
            pass
        