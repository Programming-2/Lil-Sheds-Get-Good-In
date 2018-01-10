import pygame


class player(pygame.sprite.Sprite):

    def __init__(self, img, health, damage, win_quote, lose_quote, name):
        super().__init__()
        self.img = img
        self.health = health
        self.damage = damage
        self.win_quote = win_quote
        self.lose_quote = lose_quote
        self.name = 