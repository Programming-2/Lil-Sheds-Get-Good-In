import pygame
import colors
from entity import Entity


class Attack(Entity):

    def __init__(self, player_x, player_y, attack_name, damage, full_cooldown, cooldown, screen, image):
        self.attack_name = attack_name
        self.damage = damage
        self.cooldown = cooldown
        self.player_x = player_x
        self.player_y = player_y
        self.screen = screen
        self.full_cooldown = full_cooldown
        self.image = image
        #self.range = range
        #self.sound = sound

    def attack(self):
        if self.cooldown == 0:
            #self.sound.play()
            return self.damage

    def ranged_attack(self, screen):
        if self.cooldown == 0:
            self.render(screen)

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.cooldown == 0:
            self.cooldown += self.full_cooldown

    def render(self, screen):
        screen.blit(self.image, [self.player_x, self.player_y])
