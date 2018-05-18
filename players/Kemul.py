import pygame
from src.Attack import Attack
from src.CustomAttack import CustomAttack
from players.Player import Player
from src.Cooldown import Cooldown
from utils.Sound import Sound
from datastructures.CircularQueue import CircularQueue


class Kemul(Player):

    def __init__(self, x, y, handler):
        health = 110
        damage = 55
        winQuote = "Chewbacca"
        loseQuote = "Chewbacca"
        name = "Kemul"
        defense = .5
        movespeed = 5

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.special_active = False
        self.count = 0
        self.start_time = 0
        self.startgravity = self.gravity
        self.startdefense = defense
        self.specialsprite = pygame.image.load("media/Players/Will/WillSpecial.png").convert()
        self.attacksprite = pygame.image.load("media/Players/Will/Attack3.png").convert_alpha()
        self.rangedsprite1 = pygame.image.load("media/Players/Will/WillRanged1.png").convert_alpha()
        self.rangedsprite2 = pygame.image.load("media/Players/Will/WillRanged2.png").convert_alpha()
        self.attack1 = pygame.image.load("media/Players/Will/Attack1.png").convert_alpha()
        self.attack2 = pygame.image.load("media/Players/Will/Attack2.png").convert_alpha()
        self.attack_animation = CircularQueue()
        self.attack_animation.addData(self.attack1)
        self.attack_animation.addData(self.attack2)
        self.powerattack_animation_right = CircularQueue()
        self.powerattack_animation_right.addData(pygame.image.load("media/Players/Will/PowerAttack1.png").convert_alpha())
        self.powerattack_animation_right.addData(pygame.image.load("media/Players/Will/PowerAttack2.png").convert_alpha())
        self.powerattack_animation_left = CircularQueue()
        self.powerattack_animation_left.addData(pygame.transform.flip(pygame.image.load("media/Players/Will/PowerAttack1.png").convert_alpha(), True, False))
        self.powerattack_animation_left.addData(pygame.transform.flip(pygame.image.load("media/Players/Will/PowerAttack2.png").convert_alpha(), True, False))
        self.BIGGnoise = Sound("BIGGDeathSound")
        self.rangedcount = 0
        self.rangedavailable = False
        self.ranged_cooldown = Cooldown(5)
        self.attackavailable = False
        self.damage_special = 1.5 * damage
        self.special_available = True
        self.special_cooldown = Cooldown(5)
        self.special_duration = Cooldown(1)
        self.special_count = 0
        self.special_start_time = 0
        self.released = False
        self.damage = damage
        self.tickcounter = 0
        self.right_ranged_animation = CircularQueue()
        self.right_ranged_animation.addData(self.rangedsprite1)
        self.right_ranged_animation.addData(self.rangedsprite2)
        self.left_ranged_animation = CircularQueue()
        self.left_ranged_animation.addData(pygame.transform.flip(self.rangedsprite1, True, False))
        self.left_ranged_animation.addData(pygame.transform.flip(self.rangedsprite2, True, False))
        self.ranged_used = False
        self.tick = 0

        # attacks
        self.basic = Attack(self, self.damage, self.handler)
        self.basic.attacksprite = self.attacksprite
        self.special1 = CustomAttack(self, self.damage_special, self.handler, 15, 0)
        self.special2 = CustomAttack(self, self.damage_special, self.handler, 15, 15)
        self.special3 = CustomAttack(self, self.damage_special, self.handler, 0, 15)
        self.special4 = CustomAttack(self, self.damage_special, self.handler, -15, 15)
        self.special5 = CustomAttack(self, self.damage_special, self.handler, -15, 0)
        self.special6 = CustomAttack(self, self.damage_special, self.handler, -15, -15)
        self.special7 = CustomAttack(self, self.damage_special, self.handler, 0, -15)
        self.special8 = CustomAttack(self, self.damage_special, self.handler, 15, -15)
        self.special_list = [self.special1, self.special2, self.special3, self.special4, self.special5, self.special6, self.special7, self.special8]

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True

    def attack(self, screen):
        self.rangedavailable = True

    def update(self, screen):
        self.tick += 1
        if not self.special_active:
            super().update(screen)

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()

        if self.special_active and not self.sleeping:
            self.sprite = self.specialsprite
            self.special_duration.update()
            if not self.special_duration.isDone():
                self.rangedavailable = False
                screen.blit(self.sprite, [self.rect.x, self.rect.y])
            else:
                for attack in self.special_list:
                    attack.updateAttack()
                    attack.rect.x += ((.5 * self.width) - (.5 * attack.left_attack.get_width()))
                    attack.rect.y += ((.5 * self.height) - (.5 * attack.left_attack.get_height()))
                    self.handler.getAttackList().add(attack)
                self.special_active = False
                self.gravity = self.startgravity
                self.defense = self.startdefense
                self.sprite = self.stansprite
                self.count = 0
                self.special_cooldown.update()
