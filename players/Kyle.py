import pygame
from players.Player import Player
from src.Platform import Platform
from src.Cooldown import Cooldown
from utils.Colors import colors
from src.Attack import Attack
import random


class Kyle(Player):

    def __init__(self, x, y, handler):
        health = 110
        damage = 45
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
        self.crouchSpriteList = [pygame.image.load("media/Players/Kyle/KyleCrouch.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/KyleCrouch1.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/KyleCrouch2.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/KyleCrouch3.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/KyleCrouch4.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/KyleCrouch5.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/KyleCrouch6.png").convert_alpha(),
                           pygame.image.load("media/Players/Kyle/KyleCrouch7.png").convert_alpha()]
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
        self.frame += 1
        if self.frame >= len(self.spriteList) or self.xchange == 0:
            self.frame = 0
        if not self.crouching:
            self.sprite = self.spriteList[self.frame]
        else:
            self.sprite = self.crouchSpriteList[self.frame]

        if self.facing == -1:
            self.sprite = pygame.transform.flip(self.sprite, True, False)

    def attack(self, screen):
        self.handler.getAttackList().add(Attack(self, self.damage, self.handler, 5))

    def moveX(self):
        self.rect.x += self.xchange
        platList = pygame.sprite.spritecollide(self, self.platArray, False)
        for platform in platList:
            if self.xchange > 0 and self.rect.right < platform.rect.right:  # Moving right and left of platform
                self.rect.right = platform.rect.left
            elif self.xchange < 0 and self.rect.left > platform.rect.left:  # Moving left and right of platform
                self.rect.left = platform.rect.right
            self.xchange = 0

    def update(self, screen):
        if not self.special_cooldown.isDone():
            self.special_cooldown.update()
        self.determineSprite()
        super().update(screen)

        for p in self.handler.getPlatformArray():
            if p.height == 25:
                pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), p.rect)
