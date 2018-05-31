import pygame
from src.Attack import Attack
from src.CustomAttack import CustomAttack
from players.Player import Player
from src.Cooldown import Cooldown
from utils.Sound import Sound
from datastructures.CircularQueue import CircularQueue
from utils.PunDatabase import PunDatabase
from utils.Colors import colors

font = pygame.font.SysFont("Comic Sans MS", 16)

class Smo(Player):

    def __init__(self, x, y, handler):
        health = 110
        damage = 10
        win_quote = "up to the board"
        lose_quote = "this will delay my victory"
        name = "Smo"
        defense = .5
        movespeed = 5

        super().__init__(health, damage, win_quote, lose_quote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.special_active = False
        self.special_range = 300
        self.startdefense = defense
        self.rangedcount = 0
        self.rangedavailable = True
        self.attackavailable = True
        self.special_available = True
        self.special_cooldown = Cooldown(5)
        self.special_duration = Cooldown(3)
        self.damage = damage
        self.pundatabase = PunDatabase()
        self.pun = self.pundatabase.getRandomPun()
        self.target_health_update()

    def GeneratePun(self):
        self.pun = self.pundatabase.getRandomPun()

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True

    def target_health_update(self):
        if self.handler.getPlayer1().name == "Smo":
            self.target_health = self.handler.getPlayer2().health
        else:
            self.target_health = self.handler.getPlayer1().health


    def update(self, screen):
        super().update(screen)

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()

        if self.special_active and not self.sleeping:
            self.special_duration.update()
            screen.blit(font.render(self.pun, False, colors.get("BLACK")), (self.rect.x, self.rect.y - 100))
            if self.handler.getPlayer1().name == "Smo":
                if abs(self.rect.x - self.handler.getPlayer2().rect.x) <= self.special_range and abs(self.rect.y - self.handler.getPlayer2().rect.y) <= self. special_range:
                    if (self.target_health - 10) <= self.handler.getPlayer2().health:
                        self.handler.player2.takeDamage(10)
            if self.handler.getPlayer2().name == "Smo":
                if abs(self.rect.x - self.handler.getPlayer1().rect.x) <= self.special_range and abs(self.rect.y - self.handler.getPlayer1().rect.y) <= self.special_range:
                    if (self.target_health - 10) <= self.handler.getPlayer1().health:
                        self.handler.player1.takeDamage(10)
            if self.special_duration.isDone():
                self.GeneratePun()
                self.special_cooldown.update()
                self.target_health_update()
                self.special_active = False
