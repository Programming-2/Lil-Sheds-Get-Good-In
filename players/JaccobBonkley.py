import pygame
import random
from players.Player import Player
from src.Cooldown import Cooldown
from datastructures.CircularQueue import CircularQueue


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
        self.special_cooldown = Cooldown(1)
        self.special_duration = Cooldown(5)
        self.number = 0
        self.special_active = False
        self.keyboard = pygame.image.load("media/Misc/Keyboard.png").convert_alpha()
        self.keyboard2 = pygame.image.load("media/Misc/Keyboard2.png").convert_alpha()
        self.mr_smo = pygame.image.load("media/Players/TestSprite.png").convert_alpha()
        self.num = 0

        self.keyboardAnimation = CircularQueue()
        for a in range(0, -90, -5):
            self.keyboardAnimation.addData(pygame.transform.rotate(self.keyboard, a))

        self.keyboardAnimation2 = CircularQueue()
        for b in range(-90, -180, -5):
            self.keyboardAnimation2.addData(pygame.transform.rotate(self.keyboard2, b))



    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True
            self.number = random.randint(1, 6)
        if not self.special_cooldown.isDone():
            self.num = 0

    def update(self, screen):
        self.moveX()
        self.moveY()
        self.gravityUpdate()

        if self.xchange > 0:
            self.facing = 1
        elif self.xchange < 0:
            self.facing = -1

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()

        if self.special_active and not self.sleeping:
            if self.number == 5:
                self.special_duration.update()
                self.special_duration = Cooldown(1)
                if not self.special_duration.isDone():
                    if self.facing == 1:
                        screen.blit(self.keyboardAnimation.get(), (self.rect.x + 70, self.rect.y - 50))
                    if self.facing == -1:
                        screen.blit(self.keyboardAnimation2.get(), (self.rect.x - 70, self.rect.y - 50))

                else:
                    self.special_active = False
                    self.handler.getPlayer1().stunned = False
                    self.handler.getPlayer2().stunned = False
                    self.special_cooldown.update()
                    self.num = 0
            else:
                self.special_duration = Cooldown(5)
                if not self.special_duration.isDone():
                    self.handler.getPlayer1().stunned = True
                    self.handler.getPlayer2().stunned = True
                    if self.facing == 1:
                        if self.num != (self.rect.x - 70):
                            screen.blit(self.mr_smo, (self.num, self.rect.y - 15))
                            self.num += 5
                        if self.num == (self.rect.x - 70):
                            screen.blit(self.mr_smo, (self.num, self.rect.y - 15))
                            screen.blit(self.keyboardAnimation.get(), (self.rect.x - 70, self.rect.y - 50))
                            self.takeDamage(20)
                    if self.facing == -1:
                        if self.num != (1080 - self.rect.x):
                            screen.blit(self.mr_smo, (1150 - self.num, self.rect.y - 15))
                            self.num += 5
                        if self.num == (1080 - self.rect.x):
                            screen.blit(self.mr_smo, (1150 - self.num, self.rect.y - 15))
                            screen.blit(self.keyboardAnimation2.get(), (self.rect.x + 70, self.rect.y - 50))
                            self.takeDamage(20)
                else:
                    self.special_active = False
                    self.handler.getPlayer1().stunned = False
                    self.handler.getPlayer2().stunned = False
                    self.special_cooldown.update()
                    self.num = 0

        screen.blit(self.sprite, [self.rect.x, self.rect.y])
