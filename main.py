#Main Class
import pygame

##Insert any functions


pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Game")

clock = pygame.time.Clock()

done = False
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here


    # --- Screen-clearing code goes here


    # --- Turn screen to white
    screen.fill(WHITE)

    # --- Drawing code should go here


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()