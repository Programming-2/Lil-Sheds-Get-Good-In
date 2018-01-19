import pygame
from player import Player

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (1100, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")

background_image = pygame.image.load("media/field_map.png").convert()
testSprite = pygame.image.load("media/BaseSprite.png").convert()

player1 = Player(testSprite, 100, 20, "Yes", "No", "Will", 100, 100)
player2 = Player(testSprite, 100, 20, "Yes", "No", "Jaccob Bonkley", 500, 100)

pygame.display.set_caption("Game")

clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pass  # player1.jump()
            elif event.key == pygame.K_a:
                player1.xchange = -5
            elif event.key == pygame.K_d:
                player1.xchange = 5
            elif event.key == pygame.K_s:
                pass  # player1.duck()
            elif event.key == pygame.K_UP:
                pass  # player2.jump()
            elif event.key == pygame.K_LEFT:
                player2.xchange = -5
            elif event.key == pygame.K_RIGHT:
                player2.xchange = 5
            elif event.key == pygame.K_DOWN:
                pass  # player2.duck()
        elif pygame.event == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player1.xchange = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player2.xchange = 0
            elif event.key == pygame.K_s:
                pass  # player1.unduck()
            elif event.key == pygame.K_DOWN:
                pass  # player2.unduck()

    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])  # Jakob's mistake

    player1.update(screen)
    player2.update(screen)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
