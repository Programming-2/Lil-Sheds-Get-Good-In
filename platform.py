# Platform class
import pygame
import colors


class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, length, height):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.image = pygame.Surface([self.length, self.height])
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = self.x, self.y
