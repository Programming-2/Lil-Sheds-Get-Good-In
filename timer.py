import pygame
import colors


class Timer:
    def __init__(self, time, screen):
        self.screen = screen
        self.total_time = time
        self.current_time = time
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Comic Sans MS', 16)
        self.screensize = screen.get_size()

    def update(self, screen):
        #if self.clock.tick_busy_loop() == 1000:
            #self.current_time -= 1

        text = self.font.render(self.current_time, False, colors.colors.get("BLACK"))
        screen.blit(text, (self.screensize[0] / 2, 100))
