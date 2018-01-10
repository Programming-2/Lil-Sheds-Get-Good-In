#Parent Level Class
import pygame
pygame.init()

class Level():
    def __init__(self, screen, back_img):
        self.__screen = screen
        self.__back_img = back_img

size = (1100, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")

background_image = pygame.image.load("Test.png").convert()

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True

    pygame.display.flip()
    clock.tick(60)
    screen.blit(background_image, [0, 0])
pygame.quit()
