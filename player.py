import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, sprite, health, damage, winQuote, loseQuote, name, x, y):
        super().__init__()
        self.sprite = sprite
        self.health = health
        self.damage = damage
        self.winQuote = winQuote
        self.loseQuote = loseQuote
        self.name = name
        self.x = x
        self.y = y
        self.xchange = 0
        self.ychange = 0
        self.gravity = 0.25

    def update(self, screen):
        screen.blit(self.img, [self.x, self.y])
        self.x += self.xchange
        self.y += self.ychange
