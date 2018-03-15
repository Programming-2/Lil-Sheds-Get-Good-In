import pygame
from states.State import State
from utils.Colors import colors
from src.HealthBar import HealthBar
from src.CoolDownBars import CooldownBar
from utils.Timer import Timer
from src.MeleeAttack import Attack

font = pygame.font.SysFont("Comic Sans MS", 36)


class GameState(State):

    # TODO Organize Game State
    # TODO Create a better way to order when things are rendered

    def __init__(self, name, screen, handler, attackUpdateList):
        super().__init__(name)
        self.platformArray = handler.getLevel().platformGroup
        self.attackUpdateList = attackUpdateList

        self.timer = Timer(300, screen)
        self.testProjectile = pygame.image.load("media/projectileTest.png").convert()
        self.background_image = pygame.image.load(handler.getLevel().getBackImg()).convert()
        self.kosprite = pygame.image.load("media/KO.png")
        self.handler = handler

        handler.setPlatformArray(self.platformArray)

        self.player1 = self.handler.player1
        self.player2 = self.handler.player2
        self.player1MeleeAttack = Attack(self.player1.x, self.player1.y, "melee attack", 5, 2, 2, screen, 120, handler, self.player1)
        self.player2MeleeAttack = Attack(self.player2.x, self.player2.x, "melee attack", 5, 2, 2, screen, 120, handler, self.player2)

        self.screen = screen

        self.handler.setPlayer1(self.player1)
        self.handler.setPlayer2(self.player2)

        # Timer utils
        self.count = 0
        self.end_time = 0

    def resetState(self):
        self.platformArray = self.handler.getLevel().platformGroup
        self.background_image = pygame.image.load(self.handler.getLevel().getBackImg()).convert()
        self.timer = Timer(300, self.screen)
        self.handler.setPlatformArray(self.platformArray)

        self.player1 = self.handler.player1
        self.player2 = self.handler.player2
        self.player1MeleeAttack = Attack(self.player1.x, self.player1.y, "melee attack", 5, 2, 2, self.screen, 120, self.handler, self.player1)
        self.player2MeleeAttack = Attack(self.player2.x, self.player2.x, "melee attack", 5, 2, 2, self.screen, 120, self.handler, self.player2)

        self.handler.setPlayer1(self.player1)
        self.handler.setPlayer2(self.player2)

        # Timer utils
        self.count = 0
        self.end_time = 0


    def reloadLevel(self):
        self.platformArray = self.handler.getLevel().platformGroup

        self.testProjectile = pygame.image.load("media/projectileTest.png").convert()
        self.background_image = pygame.image.load(self.handler.getLevel().getBackImg()).convert()
        self.kosprite = pygame.image.load("media/KO.png")

        self.handler.setPlatformArray(self.platformArray)

        self.player1.setPlatArray(self.handler.getPlatformArray())
        self.player2.setPlatArray(self.handler.getPlatformArray())

    def setPlayers(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.handler.setPlayer1(self.player1)
        self.handler.setPlayer2(self.player2)
        self.player2.facing = -1
        self.p1hpbar = HealthBar(self.screen, "topleft", self.player1.health)
        self.p2hpbar = HealthBar(self.screen, "topright", self.player2.health)
        self.p1cdbar = CooldownBar(self.screen, self.player1)
        self.p2cdbar = CooldownBar(self.screen, self.player2)

    def update(self, screen):
        screen.blit(self.background_image, [0, 0])  # Jakob's mistake
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and not (self.player1.sleeping or self.player1.stunned):
            self.player1.xchange = -1 * self.player1.movespeed
        if keys[pygame.K_d] and not (self.player1.sleeping or self.player1.stunned):
            self.player1.xchange = self.player1.movespeed
        if keys[pygame.K_LEFT] and not (self.player2.sleeping or self.player2.stunned):
            self.player2.xchange = -1 * self.player2.movespeed
        if keys[pygame.K_RIGHT] and not (self.player2.sleeping or self.player2.stunned):
            self.player2.xchange = self.player2.movespeed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g and not self.player1.sleeping:
                    self.player1.attack(screen)
                    self.player1.rangedstarttime = pygame.time.get_ticks()
                    self.player1.released = False
                elif event.key == pygame.K_f and not self.player1.sleeping:
                    self.player1.special()
                elif event.key == pygame.K_RSHIFT and not self.player2.sleeping:
                    self.player2.attack(screen)
                    self.player2.rangedstarttime = pygame.time.get_ticks()
                    self.player2.released = False
                elif event.key == pygame.K_RETURN and not self.player2.sleeping:
                    self.player2.special()
                elif event.key == pygame.K_r and not self.player1.sleeping:
                    self.player1MeleeAttack.p1_melee_attack()
                elif event.key == pygame.K_RCTRL and not self.player2.sleeping:
                    pass
                    self.player2MeleeAttack.p2_melee_attack()
                elif event.key == pygame.K_w and not (self.player1.sleeping or self.player1.stunned):
                    self.player1.jump()
                elif event.key == pygame.K_s and not (self.player1.sleeping or self.player1.stunned):
                    self.player1.duck()
                    self.player1.gravity *= 4
                elif event.key == pygame.K_UP and not (self.player2.sleeping or self.player2.stunned):
                    self.player2.jump()
                elif event.key == pygame.K_DOWN and not (self.player2.sleeping or self.player2.stunned):
                    self.player2.duck()
                    self.player2.gravity *= 4
                elif event.key == pygame.K_RETURN:
                    self.player2.special()
                elif event.key == pygame.K_ESCAPE:
                    self.handler.getStateManager().setCurrentState("PausedState")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    self.player1.unduck()
                    self.player1.gravity /= 4
                elif event.key == pygame.K_DOWN:
                    self.player2.unduck()
                    self.player2.gravity /= 4
                elif event.key == pygame.K_g:
                    self.player1.rangedendtime = pygame.time.get_ticks()
                    self.player1.released = True
                    print("END")
                elif event.key == pygame.K_RSHIFT:
                    self.player2.rangedendtime = pygame.time.get_ticks()
                    self.player2.released = True
                    print("END")

        if self.player1.y > screen.get_size()[1]:
            self.player1.health = 0
        if self.player2.y > screen.get_size()[1]:
            self.player2.health = 0

        if self.player2.health <= 0:
            self.player2.goToSleepForAnExtendedPeriodOfTime()
            screen.blit(self.kosprite, [self.player2.x - 15, self.player2.y - 80])
        if self.player1.health <= 0:
            self.player1.goToSleepForAnExtendedPeriodOfTime()
            screen.blit(self.kosprite, [self.player1.x - 15, self.player1.y - 80])
        if self.timer.current_time < 1:
            self.platformArray.remove(self.platformArray)
        self.player1.update(screen)
        self.player2.update(screen)
        self.timer.update(screen)
        self.p1hpbar.update(self.player1.health)
        self.p2hpbar.update(self.player2.health)
        self.p1cdbar.update(self.player1.special_cooldown)
        self.p2cdbar.update(self.player2.special_cooldown)
        self.platformArray.update()
        self.handler.setPlayer1(self.player1)
        self.handler.setPlayer2(self.player2)

        # print(self.attackUpdateList)
        pygame.sprite.groupcollide(self.platformArray, self.attackUpdateList, False, True)

        self.player1.xchange = 0
        self.player2.xchange = 0

        if self.player1.sleeping:
            # player2.dead = True
            text = font.render("Player 2 Wins!", False, colors.get("BLACK"))
            screen.blit(text, ((screen.get_size()[0] / 2 - 125), (screen.get_size()[1] / 2 - 200)))
            if self.count == 0:
                self.end_time = self.timer.current_time
                self.count += 1
            if self.timer.current_time <= self.end_time - 5:
                self.handler.setDone(True)
            '''if self.timer.current_time <= self.end_time - 5:
                # TODO find a new way to break
                # Maybe just change state
                self.handler.setDone(True)'''
        elif self.player2.sleeping:
            # player1.dead = True
            text = font.render("Player 1 Wins!", False, colors.get("BLACK"))
            screen.blit(text, ((screen.get_size()[0] / 2 - 125), (screen.get_size()[1] / 2 - 200)))
            if self.count == 0:
                self.end_time = self.timer.current_time
                self.count += 1
            if self.timer.current_time <= self.end_time - 5:
                self.handler.setDone(True)
