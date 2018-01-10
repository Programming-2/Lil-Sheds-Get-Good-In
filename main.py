import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (1100, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")

background_image = pygame.image.load("Test.png").convert()

pygame.display.set_caption("Game")

clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    pygame.display.flip()
    clock.tick(60)
    screen.blit(background_image, [0, 0])

pygame.quit()
