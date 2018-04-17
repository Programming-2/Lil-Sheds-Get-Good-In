import pygame
from players.Player import Player
from src.Cooldown import Cooldown


class Jakob(Player):

    def __init__(self, x, y, handler):
        health = 100
        damage = 15
        winQuote = "Robotics taught me that"
        loseQuote = "I could've been watching Robotics competitions"
        name = "Jakob"
        movespeed = 5
        defense = .5
        self.handler = handler

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(),
                         handler.getAttackList(), handler, defense)
        self.start_time = 0
        self.current_time = 0
        self.const = 0
        self.attacksprite = pygame.image.load("media/Players/David/DavidAttack.png").convert()
        self.specialsprite = pygame.image.load("media/Players/David/DavidSpecial.png").convert()
        self.special_cooldown = Cooldown(3)
        self.special_duration = Cooldown(5)
        self.special_start_time = 0
        self.special_count = 0
        self.special_active = False
        self.targetMoveSpeed = 0
        self.ticks = pygame.time.get_ticks()
        self.seconds = 0
        self.player = (self.handler.getPlayer1().name == "Jakob")

    def special(self):
        if self.special_cooldown.isDone():
            if not self.special_active:
                if not self.player:
                    temp1 = self.handler.getPlayer2().duck
                    self.handler.getPlayer2().duck = self.handler.getPlayer2().jump
                    self.handler.getPlayer2().jump = temp1
                    temp2 = self.handler.getPlayer2().unduck
                    self.handler.getPlayer2().unduck = self.handler.getPlayer2().unjump
                    self.handler.getPlayer2().unjump = temp2
                else:
                    temp1 = self.handler.getPlayer1().duck
                    self.handler.getPlayer1().duck = self.handler.getPlayer1().jump
                    self.handler.getPlayer1().jump = temp1
                    temp2 = self.handler.getPlayer1().unduck
                    self.handler.getPlayer1().unduck = self.handler.getPlayer1().unjump
                    self.handler.getPlayer1().unjump = temp2
            self.special_active = True

    def update(self, screen):
        self.moveX()
        self.moveY()
        self.gravityUpdate()

        if self.xchange > 0:
            self.facing = 1
        elif self.xchange < 0:
            self.facing = -1

        self.attackUpdate(screen)
        self.current_time = pygame.time.get_ticks()

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()

        if self.special_active and not self.sleeping:
            self.special_duration.update()
            if not self.special_duration.isDone():
                if not self.player:
                    self.handler.getPlayer2().xchange *= -1
                else:
                    self.handler.getPlayer1().xchange *= -1

            else:
                self.special_active = False
                self.special_cooldown.update()

        screen.blit(self.sprite, [self.rect.x, self.rect.y])
