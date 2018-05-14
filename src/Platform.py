# Platform class
import pygame
from src.Cooldown import Cooldown


class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, length, height, duration=-1, speed=0, fallspeed=0):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.image = pygame.Surface([self.length, self.height])
        self.rect = self.image.get_rect()
        self.duration = duration
        self.speed = speed
        self.platform_cooldown = Cooldown(duration)
        self.fallspeed = fallspeed

    def entMove(self, entity):
        entity.xchange += self.speed

    def fall(self):
        self.y += self.fallspeed
        self.fallspeed += .25

    def update(self):
        self.rect.topleft = self.x, self.y
        if self.duration != -1:
            self.platform_cooldown.update()
