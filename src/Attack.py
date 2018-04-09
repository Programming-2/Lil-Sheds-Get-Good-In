import pygame
from src.Entity import Entity


class Attack(pygame.sprite.Sprite):

    def __init__(self, player, damage, handler):
        super().__init__()
        self.player = player
        self.player_x = player.rect.x
        self.player_y = player.rect.y
        self.direction = player.facing
        self.travel_speed = 15
        self.changex = self.travel_speed * self.direction
        self.changey = 0
        self.attacksprite = player.attacksprite
        self.left_attack = pygame.transform.rotate(self.attacksprite, 180)
        self.right_attack = player.attacksprite
        self.damage = damage
        self.handler = handler
        # self.sound = sound
        self.rect = pygame.Rect(self.player_x, self.player_y, self.left_attack.get_width(), self.left_attack.get_height())
        if self.direction == 1:
            self.rect.x += player.width
        self.name = player.name
        self.damage = player.damage

    def updatePlayer(self):
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y
        self.direction = self.player.facing

    def update(self, screen):
        self.changex = self.travel_speed * self.direction
        self.rect.x += self.changex
        self.rect.y += self.changey
        if self.direction == -1:
            screen.blit(self.left_attack, (self.rect.x, self.rect.y))
        if self.direction == 1:
            screen.blit(self.right_attack, (self.rect.x, self.rect.y))
        if self.handler.getPlayer1().name == self.name:
            if pygame.sprite.collide_rect(self.handler.getPlayer2(), self):
                self.handler.getPlayer2().takeDamage(self.damage)
                self.handler.getAttackList().remove(self)
        if self.handler.getPlayer2().name == self.name:
            if pygame.sprite.collide_rect(self.handler.getPlayer1(), self):
                self.handler.getAttackList().remove(self)
                self.handler.getPlayer1().takeDamage(self.damage)
