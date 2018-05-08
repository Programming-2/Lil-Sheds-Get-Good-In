import pygame
from datastructures.CircularQueue import CircularQueue


class Attack(pygame.sprite.Sprite):

    def __init__(self, player, damage, handler, travel_speed = 15, changey = 0):
        super().__init__()
        self.player = player
        self.player_x = player.rect.x
        self.player_y = player.rect.y
        self.direction = player.facing
        self.travel_speed = travel_speed
        self.changex = self.travel_speed * self.direction
        self.changey = changey
        self.attacksprite = player.attacksprite
        self.left_attack = pygame.transform.rotate(self.attacksprite, 180)
        self.right_attack = player.attacksprite
        self.left_animation = CircularQueue()
        self.left_animation.addData(self.left_attack)
        self.right_animation = CircularQueue()
        self.right_animation.addData(self.right_attack)
        self.damage = damage
        self.handler = handler
        # self.sound = sound
        self.rect = pygame.Rect(self.player_x, self.player_y, self.left_attack.get_width(), self.left_attack.get_height())
        if self.direction == 1:
            self.rect.x += player.width
        self.name = player.name
        self.spawned = True

    def updateAttack(self):
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y
        self.direction = self.player.facing

    def checkPlat(self):
        if self.name != "Lil' Shed":
            pygame.sprite.groupcollide(self.handler.getPlatformArray(), self, False, True)
        else:
            if 0 > self.rect.x > 1100 or 0 > self.rect.y > 800:
                pygame.sprite.groupcollide(self.handler.getPlatformArray(), self, False, True)

    def update(self, screen):
        self.checkPlat()
        if self.spawned:
            self.player.attacksound.playSound()
            self.spawned = False
        # self.changex = self.travel_speed * self.direction
        self.rect.x += self.travel_speed * self.direction
        self.rect.y += self.changey
        if self.direction == -1:
            screen.blit(self.left_animation.get(), (self.rect.x, self.rect.y))
        if self.direction == 1:
            screen.blit(self.right_animation.get(), (self.rect.x, self.rect.y))
        if self.handler.getPlayer1().name == self.name:
            if pygame.sprite.collide_rect(self.handler.getPlayer2(), self):
                self.handler.getPlayer2().takeDamage(self.damage)
                self.handler.getAttackList().remove(self)
        if self.handler.getPlayer2().name == self.name:
            if pygame.sprite.collide_rect(self.handler.getPlayer1(), self):
                self.handler.getAttackList().remove(self)
                self.handler.getPlayer1().takeDamage(self.damage)
