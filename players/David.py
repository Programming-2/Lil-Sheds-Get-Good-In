import pygame
from players.Player import Player
from src.Cooldown import Cooldown


class David(Player):

    def __init__(self, x, y, handler):
        health = 120
        damage = 15
        win_quote = "Frankly, I do not enjoy most party-related activities, and I typically prefer small gatherings at most."
        lose_quote = "Zzz"
        name = "David"
        defense = .4
        movespeed = 3
        self.handler = handler

        super().__init__(health, damage, win_quote, lose_quote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.attacksprite = pygame.image.load("media/Players/David/DavidAttack.png").convert()
        self.specialsprite = pygame.image.load("media/Players/David/DavidSpecial.png").convert_alpha()
        # special
        self.special_cooldown = Cooldown(5)
        self.special_duration = Cooldown(1)
        self.special_active = False
        self.targetMoveSpeed = 0

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True

    def update(self, screen):
        super().update(screen)

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()

        if self.special_active and not self.sleeping:
            self.special_duration.update()
            if not self.special_duration.isDone():
                screen.blit(self.specialsprite, (0, 0))
                if self.handler.getPlayer1().name == "David":
                    self.handler.getPlayer2().stunned = True
                if self.handler.getPlayer2().name == "David":
                    self.handler.getPlayer1().stunned = True
            else:
                self.special_active = False
                if self.handler.getPlayer1().name == "David":
                    self.handler.getPlayer2().stunned = False
                if self.handler.getPlayer2().name == "David":
                    self.handler.getPlayer1().stunned = False
                self.special_cooldown.update()

