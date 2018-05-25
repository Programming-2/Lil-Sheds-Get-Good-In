import pygame
from src.Attack import Attack
from src.CustomAttack import CustomAttack
from players.Player import Player
from src.Cooldown import Cooldown
from utils.Sound import Sound
from datastructures.CircularQueue import CircularQueue
from animation.Animation import Animation
from animation.AnimationManager import AnimationManager


class Will(Player):

    def __init__(self, x, y, handler):
        health = 110
        damage = 55
        win_quote = "yikes"
        lose_quote = "yikes"
        name = "Will"
        defense = .5
        movespeed = 5

        super().__init__(health, damage, win_quote, lose_quote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.special_active = False
        self.count = 0
        self.start_time = 0
        self.startgravity = self.gravity
        self.startdefense = defense
        self.jumpsprite = pygame.image.load("media/Players/Will/WillJump.png").convert_alpha()
        self.specialsprite = pygame.image.load("media/Players/Will/WillSpecial.png").convert()
        self.attacksprite = pygame.image.load("media/Players/Will/Attack2.png").convert_alpha()
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
        
        self.walkSpriteList = [
            pygame.image.load("media/Players/Will/Will.png").convert_alpha(),
            pygame.image.load("media/Players/Will/Will1.png").convert_alpha(),
            pygame.image.load("media/Players/Will/Will2.png").convert_alpha(),
            pygame.image.load("media/Players/Will/Will3.png").convert_alpha()
        ]
        self.walkAnimation = Animation(self.handler, self, self.walkSpriteList)
        self.walk_animation_delay = 8

        self.specialSpriteList = [
            pygame.image.load("media/Players/Will/WillSpecial1.png").convert_alpha(),
            pygame.image.load("media/Players/Will/WillSpecial.png").convert()
        ]

        self.specialAnimation = Animation(self.handler, self, self.specialSpriteList)

        self.crouchSpriteList = [
            pygame.image.load("media/Players/Will/WillCrouch.png").convert_alpha(),
            pygame.image.load("media/Players/Will/WillCrouch1.png").convert_alpha(),
            pygame.image.load("media/Players/Will/WillCrouch2.png").convert_alpha(),
            pygame.image.load("media/Players/Will/WillCrouch3.png").convert_alpha()
        ]

        self.crouchAnimation = Animation(self.handler, self, self.crouchSpriteList)
        self.crouch_animation_delay = 8

        self.attackSpriteList = [
            pygame.image.load("media/Players/Will/WillRanged1.png").convert_alpha(),
            pygame.image.load("media/Players/Will/WillRanged2.png").convert_alpha()
        ]

        self.attackAnimation = Animation(self.handler, self, self.attackSpriteList)

        self.animation_manager = AnimationManager(self, self.walkAnimation, self.specialAnimation, self.crouchAnimation, self.attackAnimation)

        self.BIGGnoise = Sound("BIGGDeathSound")
        self.rangedcount = 0
        self.rangedavailable = False
        self.ranged_cooldown = Cooldown(5)
        self.attackavailable = False

        # Special
        self.special_available = True
        self.special_cooldown = Cooldown(5)
        self.special_duration = Cooldown(.25)
        self.special_count = 0
        self.special_start_time = 0
        self.roll_speed = 10

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

    def moveX(self):
        self.rect.x += self.xchange
        platList = pygame.sprite.spritecollide(self, self.platArray, False)
        for platform in platList:
            if self.xchange > 0 and self.rect.right < platform.rect.right:  # Moving right and left of platform
                self.rect.right = platform.rect.left
            elif self.xchange < 0 and self.rect.left > platform.rect.left:  # Moving left and right of platform
                self.rect.left = platform.rect.right
            self.xchange = 0

    def special(self):
        if self.special_cooldown.isDone():
            self.special_active = True
            self.in_special = True

    def attack(self, screen):
        self.rangedavailable = True

    def update(self, screen):
        self.animation_manager.update()
        self.tick += 1

        if not self.special_active:
            super().update(screen)

        if not self.special_cooldown.isDone():
            self.special_cooldown.update()

        if self.special_active and not self.sleeping:
            self.special_duration.update()
            if not self.special_duration.isDone():
                self.stunned = True
                self.defense = 0
                self.rect.x += self.roll_speed * self.facing
            else:
                self.special_cooldown.update()
                self.defense = self.startdefense
                self.stunned = False
                self.special_active = False
                self.in_special = False

        if self.rangedavailable:
            self.tickcounter += 1
            self.ranged_cooldown.current_cooldown = self.tickcounter / 60
            if self.ranged_cooldown.current_cooldown <= 1 and self.released:
                attack = Attack(self, self.damage, self.handler)
                attack.damage = 10
                attack.travel_speed = 10
                attack.left_animation = self.attack_animation
                attack.right_animation = self.attack_animation
                self.handler.getAttackList().add(attack)
                self.rangedavailable = False
                self.ranged_used = True
                self.tickcounter = 0
            elif self.ranged_cooldown.current_cooldown <= 2 and self.released:
                attack = Attack(self, self.damage, self.handler)
                attack.damage = 25
                attack.travel_speed = 15
                attack.left_animation = self.attack_animation
                attack.right_animation = self.attack_animation
                self.handler.getAttackList().add(attack)
                self.rangedavailable = False
                self.ranged_used = True
                self.tickcounter = 0
            elif self.ranged_cooldown.current_cooldown <= 3 and self.released:
                attack = Attack(self, self.damage, self.handler)
                attack.damage = 60
                attack.travel_speed = 20
                attack.left_animation = self.attack_animation
                attack.right_animation = self.attack_animation
                self.handler.getAttackList().add(attack)
                self.rangedavailable = False
                self.ranged_used = True
                self.tickcounter = 0
            elif self.ranged_cooldown.current_cooldown <= 4 and self.released:
                attack = Attack(self, self.damage, self.handler)
                attack.damage = 120
                attack.travel_speed = 25
                attack.left_animation = self.attack_animation
                attack.right_animation = self.attack_animation
                self.handler.getAttackList().add(attack)
                self.rangedavailable = False
                self.ranged_used = True
                self.tickcounter = 0
            elif self.ranged_cooldown.current_cooldown > 4 and self.released:
                attack = Attack(self, self.damage, self.handler)
                attack.damage = self.ranged_cooldown.current_cooldown * 40
                attack.travel_speed = self.ranged_cooldown.current_cooldown * 7
                attack.left_animation = self.powerattack_animation_left
                attack.right_animation = self.powerattack_animation_right
                self.handler.getAttackList().add(attack)
                self.rangedavailable = False
                self.ranged_used = True
                self.tickcounter = 0
                self.BIGGnoise.playSound()
            self.rangedcount = 0
        try:
            screen.blit(self.sprite, [self.rect.x, self.rect.y])
        except TypeError:
            print(self.sprite)
