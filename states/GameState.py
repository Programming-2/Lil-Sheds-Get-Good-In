import pygame
from State import State
from colors import colors

font = pygame.font.SysFont("Comic Sans MS", 36)
DeadText = font.render("KO", True, colors.get("RED"))

class GameState(State):

    def __init(self, name, level, player1, player2, handler, timer, platformArray, attackUpdateList, p1hpbar, p2hpbar):
        super().__init__(name)
        # TODO Move all instantiation to this state
        self.player1 = player1
        self.player2 = player2
        self.platformArray = platformArray
        self.attackUpdateList = attackUpdateList
        self.p1hpbar = p1hpbar
        self.p2hpbar = p2hpbar
        self.timer = timer
        self.testProjectile = pygame.image.load("media/projectileTest.png").convert()
        self.background_image = pygame.image.load(level.getBackImg()).convert()
        self.handler = handler

        # Timer utils
        count = 0

    def update(self, screen):
        screen.blit(self.background_image, [0, 0])  # Jakob's mistake
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.player1.attack(self.testProjectile, screen, "1")
                elif event.key == pygame.K_KP0:
                    self.player2.attack(self.testProjectile, screen, "2")
                elif event.key == pygame.K_r:
                    pass
                    # attack.p1_melee_attack()
                elif event.key == pygame.K_RCTRL and not self.player2.dead:
                    pass
                    # attack.p2_melee_attack()
                elif event.key == pygame.K_w and not self.player1.dead:
                    self.player1.jump()
                elif event.key == pygame.K_s and not self.player1.dead:
                    self.player1.duck()
                elif event.key == pygame.K_UP and not self.player2.dead:
                    self.player2.jump()
                elif event.key == pygame.K_DOWN and not self.player2.dead:
                    self.player2.duck()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    self.player1.unduck()
                elif event.key == pygame.K_DOWN:
                    self.player2.unduck()

        if keys[pygame.K_a] and not self.player1.dead:
            self.player1.xchange = -5
        if keys[pygame.K_d] and not self.player1.dead:
            self.player1.xchange = 5
        if keys[pygame.K_LEFT] and not self.player2.dead:
            self.player2.xchange = -5
        if keys[pygame.K_RIGHT] and not self.player2.dead:
            self.player2.xchange = 5

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

        self.player1.xchange = 0
        self.player2.xchange = 0

        if self.player1.dead:
            # player2.dead = True
            text = font.render("Player 2 Wins!", False, colors.get("BLACK"))
            screen.blit(text, ((screen.get_size()[0] / 2 - 125), (screen.get_size()[1] / 2 - 200)))
            game_won = True
            if self.count == 0:
                end_time = self.timer.current_time
                self.count += 1
            print(end_time)
            if self.timer.current_time <= end_time - 5:
                # TODO find a new way to break
                # Maybe just change state
                self.handler.getStateManager().setState("EndGame")
        elif self.player2.dead:
            # player1.dead = True
            text = font.render("Player 1 Wins!", False, colors.get("BLACK"))
            screen.blit(text, ((screen.get_size()[0] / 2 - 125), (screen.get_size()[1] / 2 - 200)))
            game_won = True
            if self.count == 0:
                end_time = self.timer.current_time
                self.count += 1
            print(end_time)
            if self.timer.current_time <= end_time - 5:
                # TODO find a new way to break
                # Maybe just change state
                self.handler.getStateManager().setState("EndGame")
