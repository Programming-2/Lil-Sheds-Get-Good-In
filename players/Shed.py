from players.Player import Player
from src.Cooldown import Cooldown
from src.CustomAttack import CustomAttack
from src.Attack import Attack


class Shed(Player):

    def __init__(self, x, y, handler):
        health = 200
        damage = 5
        win_quote = "OH YEAHHHH!"
        lose_quote = "IMPOSSIBLE!"
        name = "Lil' Shed"
        movespeed = 5
        defense = .7

        super().__init__(health, damage, win_quote, lose_quote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        # Misc
        self.tick = 0
        self.jump_pressed = False
        self.duck_pressed = False

        # Ranged
        self.ranged_cooldown = Cooldown(0.5)

        # Special
        self.special_cooldown = Cooldown(3)
        self.special_active = False
        self.specialx = 5
        self.specialy = 15
        self.special_phase = 1
        self.special_x_change = 1
        self.special_y_change = 1

        self.movingLeft = False
        self.movingRight = False
        self.gravity = 0

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True

    def jump(self):
        self.jump_pressed = True
        self.jumpreleased = False

    def unjump(self):
        self.jumpreleased = True
        self.jump_pressed = False

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

    def attack(self, screen):
        self.handler.getAttackList().add(Attack(self, self.damage * 4, self.handler))

    def update(self, screen):
        self.tick += 1

        if self.jump_pressed and not self.jumpreleased:
            self.ychange -= 0.2
        if self.duck_pressed and not self.duckreleased:
            self.ychange += 0.2
        if self.jumpreleased and round(self.ychange, 1) < 0:
            self.ychange += 0.1
        if self.duckreleased and round(self.ychange, 1) > 0:
            self.ychange -= 0.1
        if not self.movingLeft and round(self.xchange, 1) < 0:
            self.xchange += 0.1
        if not self.movingRight and round(self.xchange, 1) > 0:
            self.xchange -= 0.1
        if self.rect.y <= 0 and self.ychange < 0:
            self.ychange = 0

        if self.special_active and not self.sleeping:
            self.rapidFire.playSound()
            self.movespeed = 0
            self.ychange = 0
            self.xchange = 0
            if self.special_phase != 7:
                if self.tick % 2 == 0:
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, self.specialx, self.specialy))
                    self.handler.getAttackList().add(CustomAttack(self, self.damage, self.handler, -self.specialx, self.specialy))
                    if self.special_phase == 1:
                        self.special_x_change = 1
                        self.special_y_change = 1
                        if self.specialx >= 19:
                            self.special_phase = 2
                    elif self.special_phase == 2:
                        self.special_x_change = -1
                        self.special_y_change = 1
                        if self.specialx <= 3:
                            self.special_phase = 3
                    elif self.special_phase == 3:
                        self.special_x_change = 1
                        self.special_y_change = -1
                        if self.specialx >= 19:
                            self.special_phase = 4
                    elif self.special_phase == 4:
                        self.special_x_change = -1
                        self.special_y_change = -1
                        if self.specialx <= 5:
                            self.special_phase = 5
                    elif self.special_phase == 5:
                        self.special_x_change = 1
                        self.special_y_change = 1
                        if self.specialx >= 19:
                            self.special_phase = 6
                    elif self.special_phase == 6:
                        self.special_x_change = -1
                        self.special_y_change = 1
                        if self.specialx <= 3:
                            self.special_phase = 7

                    self.specialx += self.special_x_change
                    self.specialy -= self.special_y_change

            else:
                self.special_cooldown.update()
                self.movespeed = 5
                self.special_active = False
                self.specialx = 5
                self.specialy = 15
                self.special_phase = 1

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()

        super().update(screen)

        self.movingLeft = False
        self.movingRight = False
