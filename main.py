import pygame
import os
from player import Player
from testLevel import TestLevel
from healthbar import HealthBar
from timer import Timer
from handler import Handler
from attack import Attack
from platform import Platform

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (1100, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")
os.environ['SDL_VIDEO_CENTERED'] = '1'

level = TestLevel(screen)

background_image = pygame.image.load(level.getBackImg()).convert()
testProjectile = pygame.image.load("media/projectileTest.png").convert()

platformArray = level.platformGroup

pygame.display.set_caption("Lil' Shed's Get Good In™")

clock = pygame.time.Clock()

p1HitList = []
p2HitList = []

attackUpdateList = pygame.sprite.Group()

handler = Handler(attackUpdateList)

player1 = Player(100, 20, "Yes", "No", "Will", 200, 100, platformArray, handler, .3, 1)
player2 = Player(100, 20, "Yes", "No", "Jaccob Bonkley", 850, 100, platformArray, handler, .3, 2)

handler.setPlayer1(player1)
handler.setPlayer2(player2)

# attack = Attack(player1.x, player1.y, 10, "melee", 5, 2, 2, screen, testProjectile, 100, handler)

p1hpbar = HealthBar(screen, "topleft", player1.health)
p2hpbar = HealthBar(screen, "topright", player2.health)
timer = Timer(300, screen)

done = False
while not done:
    screen.blit(background_image, [0, 0])  # Jakob's mistake
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                player1.attack(testProjectile, screen, "1")
            elif event.key == pygame.K_KP0:
                player2.attack(testProjectile, screen, "2")
            elif event.key == pygame.K_r:
                pass
                # attack.p1_melee_attack()
            elif event.key == pygame.K_RCTRL and not player2.dead:
                pass
                # attack.p2_melee_attack()
            elif event.key == pygame.K_w and not player1.dead:
                player1.jump()
            elif event.key == pygame.K_s and not player1.dead:
                player1.duck()
            elif event.key == pygame.K_UP and not player2.dead:
                player2.jump()
            elif event.key == pygame.K_DOWN and not player2.dead:
                player2.duck()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player1.unduck()
            elif event.key == pygame.K_DOWN:
                player2.unduck()

    if keys[pygame.K_a] and not player1.dead:
        player1.xchange = -5
    if keys[pygame.K_d] and not player1.dead:
        player1.xchange = 5
    if keys[pygame.K_LEFT] and not player2.dead:
        player2.xchange = -5
    if keys[pygame.K_RIGHT] and not player2.dead:
        player2.xchange = 5

    if player1.y > screen.get_size()[1]:
        player1.health = 0
    if player2.y > screen.get_size()[1]:
        player2.health = 0

    if player2.health <= 0:
        player2.goToSleepForAnExtendedPeriodOfTime()
    if player1.health <= 0:
        player1.goToSleepForAnExtendedPeriodOfTime()
    if timer.current_time < 1:
        platformArray.remove(platformArray)
    player1.update(screen)
    player2.update(screen)
    timer.update(screen)
    p1hpbar.update(player1.health)
    p2hpbar.update(player2.health)
    platformArray.update()
    handler.setPlayer1(player1)
    handler.setPlayer2(player2)

    for e in attackUpdateList:
        e.render(screen)
        e.move()
        if pygame.sprite.spritecollide(player1, attackUpdateList, False) and e.player == "2":
            pygame.sprite.spritecollide(player1, attackUpdateList, True)
            player1.takeDamage(player2.damage)
        if pygame.sprite.spritecollide(player2, attackUpdateList, False) and e.player == "1":
            pygame.sprite.spritecollide(player2, attackUpdateList, True)
            player2.takeDamage(player1.damage)

    pygame.sprite.groupcollide(platformArray, attackUpdateList, False, True)

    player1.xchange = 0
    player2.xchange = 0

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
