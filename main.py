import pygame
from player import Player
from testLevel import TestLevel
from healthbar import HealthBar
from timer import Timer
from handler import Handler
from attack import Attack

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (1100, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")

level = TestLevel(screen)

background_image = pygame.image.load(level.getBackImg()).convert()
testSprite = pygame.image.load("media/BaseSprite.png").convert()
testProjectile = pygame.image.load("media/projectileTest.png").convert()

platformArray = pygame.sprite.Group()

platformArray.add(level.ground)

pygame.display.set_caption("Lil' Shed's Get Good In™")

clock = pygame.time.Clock()

p1HitList = []
p2HitList = []

attackUpdateList = pygame.sprite.Group()

handler = Handler(attackUpdateList)

player1 = Player(testSprite, 100, 20, "Yes", "No", "Will", 200, 100, platformArray, handler)
player2 = Player(testSprite, 100, 20, "Yes", "No", "Jaccob Bonkley", 850, 100, platformArray, handler)

handler.setPlayer1(player1)
handler.setPlayer2(player2)

attack = Attack(player1.x, player1.y, "melee", 5, 2, 2, screen, testProjectile, 10, handler)

p1hpbar = HealthBar(screen, "topleft", player1.health)
p2hpbar = HealthBar(screen, "topright", player2.health)
timer = Timer(30, screen)

done = False
while not done:
    screen.blit(background_image, [0, 0])  # Jakob's mistake

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.jump()
            elif event.key == pygame.K_a:
                player1.xchange = -5
            elif event.key == pygame.K_d:
                player1.xchange = 5
            elif event.key == pygame.K_s:
                player1.health -= 10
                pass  # player1.duck()
            elif event.key == pygame.K_r:
                attack.melee_attack()
            elif event.key == pygame.K_e:
                player1.attack(testProjectile, screen)
            elif event.key == pygame.K_UP:
                player2.jump()
            elif event.key == pygame.K_LEFT:
                player2.xchange = -5
            elif event.key == pygame.K_RIGHT:
                player2.xchange = 5
            elif event.key == pygame.K_DOWN:
                player2.health -= 10
            elif event.key == pygame.K_KP0:
                player2.attack(testProjectile, screen)
                pass  # player2.duck()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player1.xchange = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player2.xchange = 0
            elif event.key == pygame.K_s:
                pass  # player1.unduck()
            elif event.key == pygame.K_DOWN:
                pass  # player2.unduck()

    if player2.health <= 0:
        player2.goToSleepForAnExtendedPeriodOfTime()
    if player1.health <= 0:
        player1.goToSleepForAnExtendedPeriodOfTime()
    player1.update(screen)
    player2.update(screen)
    timer.update(screen)
    p1hpbar.update(player1.health)
    p2hpbar.update(player2.health)
    level.ground.update()

    for e in attackUpdateList:
        e.render(screen)
        e.move()

    pygame.sprite.spritecollide(player1, attackUpdateList, True)
    pygame.sprite.spritecollide(player2, attackUpdateList, True)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
