import pygame
import random
from players.Player import Player
from src.Cooldown import Cooldown

class JaccobBonkley(Player):

    def __init__(self, x, y, handler):
        health = 70
        damage = 20
        defense = .9
        movespeed = 10
        winQuote = "Size doesn't mean everything"
        loseQuote = "It's my team's fault"
        name = "JaccobBonkley"
        self.handler = handler

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.bullet_speed = 20
        self.special_cooldown = Cooldown(5)
        self.special_duration = Cooldown(2)
        self.number = 0
        self.special_active = False
        self.keyboard = pygame.image.load("media/Misc/Keyboard.png").convert()


    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True
            self.number = random.randint(1, 6)

    def update(self, screen):
        self.moveX()
        self.moveY()
        self.gravityUpdate()

        if self.xchange > 0:
            self.facing = 1
        elif self.xchange < 0:
            self.facing = -1

        self.attackUpdate(screen)

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()

        if self.special_active and not self.sleeping:
            self.special_duration.update()
            if self.number == 5:
                if not self.special_duration.isDone():
                    pygame.transform.rotate(self.keyboard, 90)
                    screen.blit(self.keyboard, [self.rect.x + 50,self.rect.y+10])
                else:
                    self.special_active = False
                    self.handler.getPlayer1().stunned = False
                    self.handler.getPlayer2().stunned = False
                    self.special_cooldown.update()
            else:
                pass

        screen.blit(self.sprite, [self.rect.x, self.rect.y])
