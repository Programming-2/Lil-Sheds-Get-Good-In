import pygame
import colors
from entity import Entity
from handler import Handler


class Attack(Entity):

    def __init__(self, player_x, player_y, attack_name, damage, full_cooldown, cooldown, screen, image, range):
        super().__init__(player_x, player_y, image)
        self.attack_name = attack_name
        self.damage = damage
        self.cooldown = cooldown
        self.x = player_x
        self.y = player_y
        self.screen = screen
        self.full_cooldown = full_cooldown
        self.image = image
        self.rect = pygame.Rect(image.get_rect())
        #self.range = range
        self.range = range
        #self.sound = sound

    def attack(self):
        if self.cooldown == 0:
            #self.sound.play()
            return self.damage

    def ranged_attack(self, screen):
        if self.cooldown == 0:
            super().render(screen)

    def melee_attack(self):
        if Handler.getPlayer1.getX() - Handler.getPlayer2.getXrr() <= self.range or Handler.getPlayer1.y - Handler.getPlayer2.y <= self.range:
            Handler.getPlayer2.takeDamgage(self.damage)

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.cooldown == 0:
            self.cooldown += self.full_cooldown

    def updatePlayerCoords(self, x, y):
        self.x = x
        self.y = y
