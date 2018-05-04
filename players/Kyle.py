import pygame
from players.Player import Player
from src.Platform import Platform
from src.Cooldown import Cooldown
from utils.Colors import colors
import random


class Kyle(Player):

    def __init__(self, x, y, handler):
        health = 110
        damage = 15
        winQuote = "Are the platforms fixed yet?"
        loseQuote = "I\'d better try to fix that... emphasis on try"
        name = "Kyle"
        defense = .6
        movespeed = 5

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.platformcount = 0
        self.special_cooldown = Cooldown(3)

        self.spriteList = [pygame.image.load("media/Players/Kyle/Kyle.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/Kyle1.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/Kyle2.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/Kyle3.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/Kyle4.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/Kyle5.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/Kyle6.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/Kyle7.png").convert_alpha()]
        self.frame = 0

    def special(self):
        if self.special_cooldown.isDone():
            if self.platformcount == 1:
                self.handler.getPlatformArray().remove(self.specialplatform)
                self.platformcount = 0
            if 0 <= self.rect.x <= 1100 and 0 <= self.rect.y <= 800:
                self.specialplatform = Platform(self.screen, self.rect.x - 50, self.rect.y + self.height + 10, self.width + 100, 25, 1)
                self.handler.getPlatformArray().add(self.specialplatform)
                self.platformcount += 1
            self.special_cooldown.update()

    def determineSprite(self):
        if self.frame >= len(self.spriteList) or self.xchange == 0:
            self.frame = 0
        self.sprite = self.spriteList[self.frame]
        self.frame += 1
        if self.facing == -1:
            self.sprite = pygame.transform.flip(self.sprite, True, False)


    def update(self, screen):
        if not self.special_cooldown.isDone():
            self.special_cooldown.update()
        self.screen = screen
        self.gravityUpdate()
        self.moveX()
        self.moveY()
        self.determineSprite()
        screen.blit(self.sprite, [self.rect.x, self.rect.y])

        if self.xchange > 0:
            self.facing = 1
        elif self.xchange < 0:
            self.facing = -1

        for p in self.handler.getPlatformArray():
            if p.height == 25:
                pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), p.rect)
