import pygame
import colors

class Attack():

    def __init__(self, player_x, player_y, attack_name, damage, full_cooldown, cooldown, screen ):
        self.attack_name = attack_name
        self.damage = damage
        self.cooldown = cooldown
        self.player_x = player_x
        self.player_y = player_y
        self.screen = screen
        self.full_cooldown = full_cooldown
        #self.range = range
        #self.sound = sound

    def attack(self):
        if self.cooldown == 0:
            #self.sound.play()
            return self.damage

    def ranged_attack(self):
        if self.cooldown == 0:
            pygame.draw.rect(self.screen, colors.colors.get("RED"), [self.player_x, self.player_y, 10, 10], 0)

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.cooldown == 0:
            self.cooldown += self.full_cooldown

