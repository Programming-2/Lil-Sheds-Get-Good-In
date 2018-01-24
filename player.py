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
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def jump(self):
        self.ychange = -10

    def update(self, screen):
        screen.blit(self.sprite, [self.x, self.y])
        self.x += self.xchange
        self.y += self.ychange
        self.rect.topleft = self.x, self.y
