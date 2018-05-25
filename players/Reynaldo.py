import pygame, math
from players.Player import Player
from src.Cooldown import Cooldown
from src.Attack import Attack


class Reynaldo(Player):

    def __init__(self, x, y, handler):
        health = 100
        damage = 20
        win_quote = "Pog Champerino!!!!"
        lose_quote = "I was lagging!"
        name = "Reynaldo"
        movespeed = 6
        defense = .5
        self.handler = handler

        super().__init__(health, damage, win_quote, lose_quote, name, x, y, movespeed, handler.getPlatformArray(),
                         handler.getAttackList(), handler, defense)

        self.ranged_cooldown = Cooldown(1.5)
        self.ranged_count = 0
        self.ranged_active = False
        self.start_tick = 0

        self.special_sprite = pygame.image.load("media/Players/Reynaldo/ReynaldoSpecial.png").convert_alpha()
        self.special_sprite_rect = self.special_sprite.get_rect()
        self.special_active = False
        self.start_pos = []
        self.special_count = 0
        self.special_travel_speed = 20
        self.special_range = 800
        self.special_stage = 1
        self.special_cooldown = Cooldown(5)
        self.special_hit = False
        self.start_direction = 0

    def attack(self, screen):
        if self.ranged_cooldown.isDone():
            self.ranged_active = True

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True  # A BIG OLD BOOMERANG AHRI Q THAT DOESNT DO DAMAGE ON THE WAY OUT BUT A LOTTA DAMAGE ON THE WAY BACK

    def update(self, screen):
        self.moveX()
        self.moveY()
        self.gravityUpdate()

        if self.xchange > 0:
            self.facing = 1
        elif self.xchange < 0:
            self.facing = -1

        screen.blit(self.sprite, [self.rect.x, self.rect.y])

        if self.ranged_cooldown.isDone() and self.ranged_active:
            if self.ranged_count == 0:
                self.start_tick = self.handler.getTick()
                self.ranged_count += 1
            if (self.handler.getTick() - self.start_tick) % 5 == 0:
                self.handler.getAttackList().add(Attack(self, self.damage, self.handler))
            if (self.handler.getTick() - self.start_tick) == 10:
                self.ranged_cooldown.update()

        if not self.ranged_cooldown.isDone():
            self.ranged_cooldown.update()
            self.ranged_count = 0
            self.ranged_active = False

        if self.special_active:
            if self.special_count == 0:
                self.start_pos = [self.rect.x, self.rect.y]
                self.special_sprite_rect.x = self.rect.x
                self.special_sprite_rect.y = self.rect.y - 30
                self.special_count += 1
                self.start_direction = self.facing
            screen.blit(self.special_sprite, [self.special_sprite_rect.x, self.special_sprite_rect.y])

            if abs(self.start_pos[0] - self.special_sprite_rect.x) >= self.special_range:
                self.special_stage = 2

            if self.special_stage is 1:
                self.movespeed = 10
                if self.start_direction == 1:
                    self.special_sprite_rect.x += self.special_travel_speed
                if self.start_direction == -1:
                    self.special_sprite_rect.x -= self.special_travel_speed
            if self.special_stage is 2:
                pygame.transform.rotate(self.special_sprite, 10)
                x_dist = self.special_sprite_rect.x - self.rect.x
                y_dist = self.special_sprite_rect.y - self.rect.y + 30
                xy_dist = math.sqrt((x_dist * x_dist) + (y_dist * y_dist))
                y_angle = math.asin(x_dist / xy_dist)
                x_angle = math.acos(y_dist / xy_dist)
                x_speed = self.special_travel_speed * math.sin(y_angle)
                y_speed = self.special_travel_speed * math.cos(x_angle)
                if pygame.Rect.colliderect(self.special_sprite_rect, self.rect):
                    self.special_stage = 3
                if pygame.Rect.colliderect(self.handler.getOtherPlayer(self).rect, self.special_sprite_rect) and not self.special_hit:
                    self.handler.getOtherPlayer(self).takeTrueDamage(40)
                    self.special_hit = True
                self.special_sprite_rect.x -= x_speed
                self.special_sprite_rect.y -= y_speed
            if self.special_stage is 3:
                self.special_count = 0
                self.special_stage = 1
                self.special_active = False
                self.special_hit = False
                self.movespeed = 6
                self.special_cooldown.update()

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()
