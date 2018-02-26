import pygame
from states.State import State
from colors import colors
from healthbar import HealthBar
from timer import Timer
from players.Player import Player
from players.Will import Will

font = pygame.font.SysFont("Comic Sans MS", 36)
DeadText = font.render("KO", True, colors.get("RED"))


class GameState(State):

    def __init__(self, name, level, screen, handler, attackUpdateList):
        super().__init__(name)
        self.platformArray = level.platformGroup
        self.attackUpdateList = attackUpdateList

        self.timer = Timer(300, screen)
        self.testProjectile = pygame.image.load("media/projectileTest.png").convert()
        self.background_image = pygame.image.load(level.getBackImg()).convert()
        self.handler = handler

        self.player2 = Player(100, 20, "Yes", "No", "JaccobBonkley", 850, 100, self.platformArray, handler, .6, 0)
        self.player1 = Will(200, 100, self.platformArray, handler, 1, self.player2)

        self.p1hpbar = HealthBar(screen, "topleft", self.player1.health)
        self.p2hpbar = HealthBar(screen, "topright", self.player2.health)

        handler.setPlayer1(self.player1)
        handler.setPlayer2(self.player2)

        # Timer utils
        self.count = 0
        self.end_time = 0

    def update(self, screen):
        print("time: " + str(self.timer.current_time))
        screen.blit(self.background_image, [0, 0])  # Jakob's mistake
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and not (self.player1.dead or self.player1.stunned):
            self.player1.xchange = -5
        if keys[pygame.K_d] and not (self.player1.dead or self.player1.stunned):
            self.player1.xchange = 5
        if keys[pygame.K_LEFT] and not (self.player2.dead or self.player2.stunned):
            self.player2.xchange = -5
        if keys[pygame.K_RIGHT] and not (self.player2.dead or self.player2.stunned):
            self.player2.xchange = 5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    self.player1.attack(self.testProjectile, screen, "1")
                elif event.key == pygame.K_f:
                    self.player1.special()
                elif event.key == pygame.K_RSHIFT:
                    self.player2.attack(self.testProjectile, screen, "2")
                elif event.key == pygame.K_r:
                    pass
                    # attack.p1_melee_attack()
                elif event.key == pygame.K_RCTRL and not self.player2.dead:
                    pass
                    # attack.p2_melee_attack()
                elif event.key == pygame.K_w and not (self.player1.dead or self.player1.stunned):
                    self.player1.jump()
                elif event.key == pygame.K_s and not (self.player1.dead or self.player1.stunned):
                    self.player1.duck()
                elif event.key == pygame.K_UP and not (self.player2.dead or self.player2.stunned):
                    self.player2.jump()
                elif event.key == pygame.K_DOWN and not (self.player2.dead or self.player2.stunned):
                    self.player2.duck()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    self.player1.unduck()
                elif event.key == pygame.K_DOWN:
                    self.player2.unduck()

        if self.player1.y > screen.get_size()[1]:
            self.player1.health = 0
        if self.player2.y > screen.get_size()[1]:
            self.player2.health = 0

        if self.player2.health <= 0:
            self.player2.goToSleepForAnExtendedPeriodOfTime()
            screen.blit(DeadText, [self.player2.x, self.player1.y - 1])
        if self.player1.health <= 0:
            self.player1.goToSleepForAnExtendedPeriodOfTime()
            screen.blit(DeadText, [self.player1.x, self.player2.y])
        if self.timer.current_time < 1:
            self.platformArray.remove(self.platformArray)
        self.player1.update(screen)
        self.player2.update(screen)
        self.timer.update(screen)
        self.p1hpbar.update(self.player1.health)
        self.p2hpbar.update(self.player2.health)
        self.platformArray.update()
        self.handler.setPlayer1(self.player1)
        self.handler.setPlayer2(self.player2)

        for e in self.attackUpdateList:
            if e.x < 0 or e.x > screen.get_size()[0]:
                self.attackUpdateList.remove(e)
            if e.y < 0 or e.y > screen.get_size()[1]:
                self.attackUpdateList.remove(e)
            e.render(screen)
            e.move()
            if pygame.sprite.spritecollide(self.player1, self.attackUpdateList, False) and e.player == "2":
                pygame.sprite.spritecollide(self.player1, self.attackUpdateList, True)
                self.player1.takeDamage(self.player2.damage)
            if pygame.sprite.spritecollide(self.player2, self.attackUpdateList, False) and e.player == "1":
                pygame.sprite.spritecollide(self.player2, self.attackUpdateList, True)
                self.player2.takeDamage(self.player1.damage)

        pygame.sprite.groupcollide(self.platformArray, self.attackUpdateList, False, True)
        print(self.attackUpdateList)

        self.player1.xchange = 0
        self.player2.xchange = 0

        if self.player1.dead:
            # player2.dead = True
            text = font.render("Player 2 Wins!", False, colors.get("BLACK"))
            screen.blit(text, ((screen.get_size()[0] / 2 - 125), (screen.get_size()[1] / 2 - 200)))
            if self.count == 0:
                self.end_time = self.timer.current_time
                self.count += 1
                print(self.end_time)
            if self.timer.current_time <= self.end_time - 5:
                self.handler.setDone(True)
            print("end time: " + str(self.end_time))
            '''if self.timer.current_time <= self.end_time - 5:
                # TODO find a new way to break
                # Maybe just change state
                self.handler.setDone(True)'''
        elif self.player2.dead:
            # player1.dead = True
            text = font.render("Player 1 Wins!", False, colors.get("BLACK"))
            screen.blit(text, ((screen.get_size()[0] / 2 - 125), (screen.get_size()[1] / 2 - 200)))
            if self.count == 0:
                self.end_time = self.timer.current_time
                self.count += 1
            print("end time: " + str(self.end_time))
            if self.timer.current_time <= self.end_time - 5:
                self.handler.setDone(True)
