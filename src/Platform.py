# Platform class
import pygame
from src.Cooldown import Cooldown


class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, length, height, duration):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.image = pygame.Surface([self.length, self.height])
        self.rect = self.image.get_rect()
        self.duration = duration
        self.platform_cooldown = Cooldown(duration)

    def update(self):
        self.rect.topleft = self.x, self.y
        if self.duration != -1:
            self.platform_cooldown.update()
