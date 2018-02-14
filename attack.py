import pygame
from entity import Entity


class Attack(Entity):

    def __init__(self, player_x, player_y, attack_name, damage, full_cooldown, cooldown, screen, image, range, handler):
        super().__init__(player_x, player_y, image)
        self.attack_name = attack_name
        self.damage = damage
        self.cooldown = cooldown
        self.x = player_x
        self.y = player_y
        self.screen = screen
        self.full_cooldown = full_cooldown
        self.image = image
        #self.rect = pygame.Rect(image.get_rect())
        self.range = range
        self.handler = handler
        #self.sound = sound

    def attack(self):
        if self.cooldown == 0:
            #self.sound.play()
            return self.damage

    def ranged_attack(self, screen):
        if self.cooldown == 0:
            super().render(screen)

    def p1_melee_attack(self):
        if abs(self.handler.getPlayer1().getX() - self.handler.getPlayer2().getX()) <= self.range and abs(self.handler.getPlayer1().getY() - self.handler.getPlayer2().getY()) <= self.range:
            self.handler.getPlayer2().takeDamage(self.damage)

    def p2_melee_attack(self):
        if abs(self.handler.getPlayer2().getX() - self.handler.getPlayer1().getX()) <= self.range and abs(self.handler.getPlayer2().getY() - self.handler.getPlayer1().getY()) <= self.range:
            self.handler.getPlayer1().takeDamage(self.damage)

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.cooldown == 0:
            self.cooldown += self.full_cooldown

    def updatePlayerCoords(self, x, y):
        self.x = x
        self.y = y
