#Platform class
import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, length, height):
        super().__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)
