import pygame
from players.Player import Player
from src.Cooldown import Cooldown
from src.Attack import Attack
from src.CustomAttack import CustomAttack


class Shed(Player):

    def __init__(self, x, y, handler):
        health = 200
        damage = 20
        winQuote = "Robotics taught me that"
        loseQuote = "I could've been watching Robotics competitions"
        name = "Lil' Shed"
        movespeed = 5
        defense = .7

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        # Misc
        self.tick = 0
        self.special_tick = 1
        self.jump_pressed = False
        self.duck_pressed = False

        # Ranged
        self.ranged_cooldown = Cooldown(0.5)

        # Special
        self.special_cooldown = Cooldown(8)
        self.special_active = False
        self.special_duration = Cooldown(3)
        self.specialx = 5
        self.specialy = 15

        self.movingLeft = False
        self.movingRight = False

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True

    def jump(self):
        self.jump_pressed = True
        self.jumpreleased = False

    def duck(self):
        self.duck_pressed = True
        self.duckreleased = False

    def unduck(self):
        self.duckreleased = True
        self.duck_pressed = False

    def moveLeft(self):
        if self.xchange > self.movespeed * -1:
            self.xchange -= .2
        self.movingLeft = True

    def moveRight(self):
        if self.xchange < self.movespeed:
            self.xchange += .2
        self.movingRight = True

    def update(self, screen):
        self.tick += 1
        self.screen = screen
        self.moveX()
        self.moveY()
        screen.blit(self.sprite, [self.rect.x, self.rect.y])

        if self.xchange > 0:
            self.facing = 1
        elif self.xchange < 0:
            self.facing = -1

        if self.jump_pressed and not self.jumpreleased:
            self.ychange -= 0.2
        if self.duck_pressed and not self.duckreleased:
            self.ychange += 0.2
        if self.jumpreleased and round(self.ychange, 1) < 0:
            self.ychange += 0.1
        if self.duckreleased and round(self.ychange, 1) > 0:
            self.ychange -= 0.1

        if self.special_active and not self.sleeping:
            if self.tick % 5 == 0:
                self.special_tick += 1
            print(self.special_tick)
            self.movespeed = 0
            self.ychange = 0
            self.special_duration.update()
            if not self.special_duration.isDone():
                for x in range(1, 17):
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, self.specialx, self.specialy))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -self.specialx, self.specialy))
                    self.specialx += 2
                    self.specialy -= 2

                '''if self.special_tick == 1:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 5, 15))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -5, 15))
                elif self.special_tick == 2:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 7, 13))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -7, 13))
                elif self.special_tick == 3:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 9, 11))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -9, 11))
                elif self.special_tick == 4:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 11, 9))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -11, 9))
                elif self.special_tick == 5:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 13, 7))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -13, 7))
                elif self.special_tick == 6:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 15, 5))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -15, 5))
                elif self.special_tick == 7:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 17, 3))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -17, 3))
                elif self.special_tick == 8:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 19, 1))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -19, 1))
                elif self.special_tick == 9:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 19, -1))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -19, -1))
                elif self.special_tick == 10:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 17, -3))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -17, -3))
                elif self.special_tick == 11:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 15, -5))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -15, -5))
                elif self.special_tick == 12:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 13, -7))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -13, -7))
                elif self.special_tick == 13:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 11, -9))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -11, -9))
                elif self.special_tick == 14:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 9, -11))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -9, -11))
                elif self.special_tick == 15:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 7, -13))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -7, -13))
                elif self.special_tick == 16:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 5, -15))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, 5, -15))
                else:
                    self.special_tick = 1'''
            else:
                self.special_cooldown.update()
                self.movespeed = 5
                self.special_active = False

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()
