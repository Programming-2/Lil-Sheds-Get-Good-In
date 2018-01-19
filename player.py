import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, health, damage, winQuote, loseQuote, name, posx, posy):
        super().__init__()
        # self.img = img
        self.health = health
        self.damage = damage
        self.winQuote = winQuote
        self.loseQuote = loseQuote
        self.name = name
        self.posx = posx
        self.posy = posy
        self.xchange = 0
        self.ychange = 0

    def update(self):
        self.posx += self.xchange
        self.posy += self.ychange
