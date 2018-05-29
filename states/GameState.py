import pygame
from states.State import State
from utils.Colors import colors
from src.HealthBar import HealthBar
from src.InfoBars import InfoBar
from utils.Timer import Timer
from utils.Constants import *

font = pygame.font.SysFont("Comic Sans MS", 36)


class GameState(State):

    # TODO Organize Game State
    # TODO Create a better way to order when things are rendered

    def __init__(self, name, screen, handler, attackUpdateList):
        super().__init__(name)
        self.platformArray = handler.getLevel().platformGroup
        self.attackUpdateList = attackUpdateList

        self.timer = Timer(300, screen)
        self.testProjectile = pygame.image.load("media/Misc/projectileTest.png").convert()
        self.background_image = pygame.image.load(handler.getLevel().getBackImg()).convert()
        self.kosprite = pygame.image.load("media/Misc/KO.png").convert()
        self.handler = handler

        handler.setPlatformArray(self.platformArray)

        self.player1 = self.handler.player1
        self.player2 = self.handler.player2

        self.screen = screen

        self.handler.setPlayer1(self.player1)
        self.handler.setPlayer2(self.player2)

        if pygame.joystick.get_count() == 2:
            self.joystick1 = pygame.joystick.Joystick(0)
            self.joystick1.init()
            self.joystick2 = pygame.joystick.Joystick(1)
            self.joystick2.init()
            self.useJoysticksP1 = True
            self.useJoysticksP2 = True
        elif pygame.joystick.get_count() == 1:
            self.joystick1 = pygame.joystick.Joystick(0)
            self.joystick1.init()
            self.useJoysticksP1 = True
            self.useJoysticksP2 = False
        else:
            self.useJoysticksP1 = False
            self.useJoysticksP2 = False

        # Timer utils
        self.count = 0
        self.end_time = 0

    def resetState(self):
        self.player1.sleeping = False

        self.player2.sleeping = False

        self.platformArray = self.handler.getLevel().platformGroup

        self.background_image = pygame.image.load(self.handler.getLevel().getBackImg()).convert()

        self.timer = Timer(300, self.screen)

        self.handler.setPlatformArray(self.platformArray)

        self.player1 = self.handler.player1
        self.player2 = self.handler.player2

        self.handler.setPlayer1(self.player1)
        self.handler.setPlayer2(self.player2)

        self.player2.facing = -1

        self.player1.health = self.player1.maxHP
        self.player2.health = self.player2.maxHP

        self.p1hpbar = HealthBar(self.screen, "topleft", self.player1.health, self.handler)
        self.p2hpbar = HealthBar(self.screen, "topright", self.player2.health, self.handler)

        self.p1infobar = InfoBar(self.screen, self.player1, self.handler)
        self.p2infobar = InfoBar(self.screen, self.player2, self.handler)

        self.player1.rect.x = 150
        self.player1.rect.y = 100

        self.player2.rect.x = 950
        self.player2.rect.y = 100

        self.player1.xchange = 0
        self.player1.ychange = 0

        self.player2.xchange = 0
        self.player2.ychange = 0

        self.player1.unduck()
        self.player2.unduck()

        # Timer utils
        self.count = 0
        self.end_time = 0

    def reloadLevel(self):
        if len(self.handler.getLevel().platformGroup) == 0:
            self.handler.getLevel().__init__(self.screen)

        self.platformArray = self.handler.getLevel().platformGroup

        self.testProjectile = pygame.image.load("media/Misc/projectileTest.png").convert()
        self.background_image = pygame.image.load(self.handler.getLevel().getBackImg()).convert()
        self.kosprite = pygame.image.load("media/Misc/KO.png")

        self.handler.setPlatformArray(self.platformArray)
        self.handler.getAttackList().empty()

        self.player1.setPlatArray(self.handler.getPlatformArray())
        self.player2.setPlatArray(self.handler.getPlatformArray())

    def setPlayers(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.handler.setPlayer1(self.player1)
        self.handler.setPlayer2(self.player2)

        self.player2.facing = -1

        self.p1hpbar = HealthBar(self.screen, "topleft", self.player1.health, self.handler)
        self.p2hpbar = HealthBar(self.screen, "topright", self.player2.health, self.handler)

        self.p1infobar = InfoBar(self.screen, self.player1, self.handler)
        self.p2infobar = InfoBar(self.screen, self.player2, self.handler)

    def update(self, screen):
        screen.blit(self.background_image, [0, 0])  # Jakob's mistake
        keys = pygame.key.get_pressed()

        self.handler.level.update(screen)

        if keys[pygame.K_a] and not (self.player1.sleeping or self.player1.stunned):
            self.player1.moveLeft()
        if keys[pygame.K_d] and not (self.player1.sleeping or self.player1.stunned):
            self.player1.moveRight()
        if keys[pygame.K_LEFT] and not (self.player2.sleeping or self.player2.stunned):
            self.player2.moveLeft()
        if keys[pygame.K_RIGHT] and not (self.player2.sleeping or self.player2.stunned):
            self.player2.moveRight()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g and not (self.player1.sleeping or self.player1.stunned):
                    self.player1.attack(screen)
                    self.player1.rangedstarttime = pygame.time.get_ticks()
                    self.player1.released = False
                elif event.key == pygame.K_f and not (self.player1.sleeping or self.player1.stunned):
                    self.player1.special()
                elif event.key == pygame.K_r and not (self.player1.sleeping or self.player1.stunned):
                    self.player1.meleeAttack(screen)
                elif event.key == pygame.K_w and not (self.player1.sleeping or self.player1.stunned):
                    self.player1.jump()
                elif event.key == pygame.K_s and not (self.player1.sleeping or self.player1.stunned):
                    self.player1.duck()
                elif event.key == pygame.K_RSHIFT and not (self.player2.sleeping or self.player2.stunned):
                    self.player2.attack(screen)
                    self.player2.rangedstarttime = pygame.time.get_ticks()
                    self.player2.released = False
                elif event.key == pygame.K_RETURN and not (self.player2.sleeping or self.player2.stunned):
                    self.player2.special()
                elif event.key == pygame.K_RCTRL and not (self.player2.sleeping or self.player2.stunned):
                    self.player2.meleeAttack(screen)
                elif event.key == pygame.K_UP and not (self.player2.sleeping or self.player2.stunned):
                    self.player2.jump()
                elif event.key == pygame.K_DOWN and not (self.player2.sleeping or self.player2.stunned):
                    self.player2.duck()
                elif event.key == pygame.K_ESCAPE:
                    self.handler.getStateManager().setCurrentState("PausedState")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player1.unjump()
                elif event.key == pygame.K_UP:
                    self.player2.unjump()
                if event.key == pygame.K_s:
                    self.player1.unduck()
                elif event.key == pygame.K_DOWN:
                    self.player2.unduck()
                elif event.key == pygame.K_g:
                    self.player1.rangedendtime = pygame.time.get_ticks()
                    self.player1.released = True
                elif event.key == pygame.K_RSHIFT:
                    self.player2.rangedendtime = pygame.time.get_ticks()
                    self.player2.released = True
            if self.useJoysticksP1 and event.type == pygame.JOYBUTTONDOWN:
                if event.button == CONTROLLER_RANGED and not (self.player1.sleeping or self.player1.stunned) and event.joy == 0:
                    self.player1.attack(screen)
                    self.player1.rangedstarttime = pygame.time.get_ticks()
                    self.player1.released = False
                if event.button == CONTROLLER_SPECIAL and not (self.player1.sleeping or self.player1.stunned) and event.joy == 0:
                    self.player1.special()
                if event.button == CONTROLLER_MELEE and not (self.player1.sleeping or self.player1.stunned) and event.joy == 0:
                    self.player1.meleeAttack(screen)
                if event.button == CONTROLLER_JUMP and not (self.player1.sleeping or self.player1.stunned) and event.joy == 0 and self.player1.name != "Lil' Shed":
                    self.player1.jump()
                if event.button == CONTROLLER_CROUCH and not (self.player1.sleeping or self.player1.stunned) and event.joy == 0 and self.player1.name != "Lil' Shed":
                    self.player1.duck()
            if self.useJoysticksP2 and event.type == pygame.JOYBUTTONDOWN:
                if event.button == CONTROLLER_JUMP and not (self.player2.sleeping or self.player2.stunned) and event.joy == 1 and self.player2.name != "Lil' Shed":
                    self.player2.jump()
                if event.button == CONTROLLER_MELEE and not (self.player2.sleeping or self.player2.stunned) and event.joy == 1:
                    self.player2.meleeAttack(screen)
                if event.button == CONTROLLER_CROUCH and not (self.player2.sleeping or self.player2.stunned) and event.joy == 1 and self.player2.name != "Lil' Shed":
                    self.player2.duck()
                if event.button == CONTROLLER_RANGED and not (self.player2.sleeping or self.player2.stunned) and event.joy == 1:
                    self.player2.attack(screen)
                    self.player2.rangedstarttime = pygame.time.get_ticks()
                    self.player2.released = False
                if event.button == CONTROLLER_SPECIAL and not (self.player2.sleeping or self.player2.stunned) and event.joy == 1:
                    self.player2.special()
                if event.button == CONTROLLER_PAUSE:
                    self.handler.getStateManager().setCurrentState("PausedState")
            if self.useJoysticksP1 and event.type == pygame.JOYBUTTONUP:
                if event.button == CONTROLLER_JUMP and not (self.player1.sleeping or self.player1.stunned) and event.joy == 0 and self.player1.name != "Lil' Shed":
                    self.player1.unjump()
                if event.button == CONTROLLER_RANGED and event.joy == 0:
                    self.player1.rangedendtime = pygame.time.get_ticks()
                    self.player1.released = True
                if event.button == CONTROLLER_CROUCH and event.joy == 0 and self.player1.name != "Lil' Shed":
                    self.player1.unduck()
            if self.useJoysticksP2 and event.type == pygame.JOYBUTTONUP:
                if event.button == CONTROLLER_JUMP and not (self.player2.sleeping or self.player2.stunned) and event.joy == 1 and self.player2.name != "Lil' Shed":
                    self.player2.unjump()
                if event.button == CONTROLLER_RANGED and event.joy == 1:
                    self.player2.rangedendtime = pygame.time.get_ticks()
                    self.player2.released = True
                if event.button == CONTROLLER_CROUCH and event.joy == 1 and self.player2.name != "Lil' Shed":
                    self.player2.unduck()

        if self.player1.rect.y > screen.get_size()[1]:
            self.player1.health = 0
        if self.player2.rect.y > screen.get_size()[1]:
            self.player2.health = 0

        if self.player2.health <= 0:
            self.player2.goToSleepForAnExtendedPeriodOfTime()
            screen.blit(self.kosprite, [self.player2.rect.x - 15, self.player2.rect.y - 80])
        if self.player1.health <= 0:
            self.player1.goToSleepForAnExtendedPeriodOfTime()
            screen.blit(self.kosprite, [self.player1.rect.x - 15, self.player1.rect.y - 80])

        if self.timer.current_time < 1:
            self.platformArray.remove(self.platformArray)

        self.player1.update(screen)
        self.player2.update(screen)
        self.player1.attackUpdate(screen)

        self.timer.update(screen)

        self.p1infobar.update(self.player1.ranged_cooldown.getCurrentCooldown(), self.player1.special_cooldown.getCurrentCooldown(), self.player1.health)
        self.p2infobar.update(self.player2.ranged_cooldown.getCurrentCooldown(), self.player2.special_cooldown.getCurrentCooldown(), self.player2.health)

        self.p1hpbar.update(self.player1.health)
        self.p2hpbar.update(self.player2.health)

        self.platformArray.update()

        for p in self.platformArray:
            if p.platform_cooldown.isDone() and p.duration != -1:
                self.platformArray.remove(p)

        self.handler.setPlayer1(self.player1)
        self.handler.setPlayer2(self.player2)

        if self.player1.name != "Lil' Shed":
            self.player1.xchange = 0
        if self.player2.name != "Lil' Shed":
            self.player2.xchange = 0

        if self.useJoysticksP1:
            if (self.joystick1.get_axis(0) > 0.01) and not (self.player1.sleeping or self.player1.stunned):
                self.player1.moveRight()

            if (self.joystick1.get_axis(0) < -0.01) and not (self.player1.sleeping or self.player1.stunned):
                self.player1.moveLeft()

            if (self.joystick1.get_axis(1) > 0.01) and not (self.player1.sleeping or self.player1.stunned) and self.player1.name == "Lil' Shed":
                self.player1.duck()
            elif self.player1.name == "Lil' Shed":
                self.player1.unduck()

            if (self.joystick1.get_axis(1) < -0.01) and not (self.player1.sleeping or self.player1.stunned) and self.player1.name == "Lil' Shed":
                self.player1.jump()
            elif self.player1.name == "Lil' Shed":
                self.player1.unjump()

        if self.useJoysticksP2:
            if (self.joystick2.get_axis(0) > 0.01) and not (self.player2.sleeping or self.player2.stunned):
                self.player2.moveRight()

            if (self.joystick2.get_axis(0) < -0.01) and not (self.player2.sleeping or self.player2.stunned):
                self.player2.moveLeft()

            if (self.joystick2.get_axis(1) > 0.01) and not (self.player2.sleeping or self.player2.stunned) and self.player2.name == "Lil' Shed":
                self.player2.duck()
            elif self.player2.name == "Lil' Shed":
                self.player2.unduck()

            if (self.joystick2.get_axis(1) < -0.01) and not (self.player2.sleeping or self.player2.stunned) and self.player2.name == "Lil' Shed":
                self.player2.jump()
            elif self.player2.name == "Lil' Shed":
                self.player2.unjump()

        if self.player1.sleeping:
            text = font.render("Player 2 Wins!", False, colors.get("BLACK"))
            screen.blit(text, ((screen.get_size()[0] / 2 - 125), (screen.get_size()[1] / 2 - 200)))
            text = font.render(self.handler.getPlayer1().loseQuote, False, colors.get("BLACK"))
            screen.blit(text, (self.handler.getPlayer1().rect.x, self.handler.getPlayer1().rect.y - 100))
            text = font.render(self.handler.getPlayer2().winQuote, False, colors.get("BLACK"))
            screen.blit(text, (self.handler.getPlayer2().rect.x, self.handler.getPlayer2().rect.y - 100))
            if self.count == 0:
                self.end_time = self.timer.current_time
                self.count += 1
            if self.timer.current_time <= self.end_time - 5:
                self.handler.setDone(True)
                self.handler.getStateManager().setCurrentState("EndGameState")
        elif self.player2.sleeping:
            text = font.render("Player 1 Wins!", False, colors.get("BLACK"))
            screen.blit(text, ((screen.get_size()[0] / 2 - 125), (screen.get_size()[1] / 2 - 200)))
            text = font.render(self.handler.getPlayer2().loseQuote, False, colors.get("BLACK"))
            screen.blit(text, (self.handler.getPlayer2().rect.x, self.handler.getPlayer2().rect.y - 100))
            text = font.render(self.handler.getPlayer1().winQuote, False, colors.get("BLACK"))
            screen.blit(text, (self.handler.getPlayer1().rect.x, self.handler.getPlayer1().rect.y - 100))
            if self.count == 0:
                self.end_time = self.timer.current_time
                self.count += 1
            if self.timer.current_time <= self.end_time - 5:
                self.handler.setDone(True)
                self.handler.getStateManager().setCurrentState("EndGameState")
