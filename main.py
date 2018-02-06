import pygame
from player import Player
from testLevel import TestLevel
from attack import Attack
from healthbar import HealthBar
from platform import Platform

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

platformArray = pygame.sprite.Group()

platformArray.add(level.ground)

platformArray.add(Platform(screen, 300, 300, 500, 100))

player1 = Player(testSprite, 100, 20, "Yes", "No", "Will", 200, 100, platformArray)
player2 = Player(testSprite, 100, 20, "Yes", "No", "Jaccob Bonkley", 850, 100, platformArray)

p1hpbar = HealthBar(screen, "topleft", player1.health)
p2hpbar = HealthBar(screen, "topright", player2.health)

ranged_attack = Attack(player1.x, player1.y, "ranged", 1, 0, 0, screen)

pygame.display.set_caption("Lil' Shed's Get Good In™")

clock = pygame.time.Clock()

p1HitList = []
p2HitList = []

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
                pass  # player1.duck()
            elif event.key == pygame.K_e:
                ranged_attack.ranged_attack()
            elif event.key == pygame.K_UP:
                player2.jump()
            elif event.key == pygame.K_LEFT:
                player2.xchange = -5
            elif event.key == pygame.K_RIGHT:
                player2.xchange = 5
            elif event.key == pygame.K_DOWN:
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

    player1.ychange += player1.gravity
    player2.ychange += player2.gravity

    player1.update(screen)
    player2.update(screen)
    p1hpbar.update(50)
    p2hpbar.update(100)
    ranged_attack.update()
    level.ground.update()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
