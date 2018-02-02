import pygame
from player import Player
from testLevel import TestLevel
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

player1 = Player(testSprite, 100, 20, "Yes", "No", "Will", 200, 100)
player2 = Player(testSprite, 100, 20, "Yes", "No", "Jaccob Bonkley", 850, 100)

ranged_attack = Attack("ranged", 1, 5)

platformArray = pygame.sprite.Group()

platformArray.add(level.ground)

pygame.display.set_caption("Lil' Shed's Get Good In™")

clock = pygame.time.Clock()

p1HitList = []
p2HitList = []

done = False
while not done:
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

    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])  # Jakob's mistake

    y = 0
    pygame.draw.rect(screen,[player1.x + y, player1.y], [5, 5], 0)
    y += 1

    p1HitList = pygame.sprite.spritecollide(player1, platformArray, False)
    p2HitList = pygame.sprite.spritecollide(player2, platformArray, False)

    for platform in p1HitList:
        player1.resetJump()
        player1.y = platform.y - player1.height
        player1.ychange = 0

    for platform in p2HitList:
        player2.resetJump()
        player2.y = platform.y - player2.height
        player2.ychange = 0

    player1.update(screen)
    player2.update(screen)
    level.ground.update()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
