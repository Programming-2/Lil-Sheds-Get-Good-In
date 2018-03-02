import pygame
import Colors


class Timer:
    def __init__(self, time, screen):
        self.screen = screen
        self.total_time = time
        self.current_time = time
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Comic Sans MS', 24)
        self.screensize = screen.get_size()
        self.frame_count = 0

    def update(self, screen):
        self.frame_count += 1
        if self.frame_count % 60 == 0 and self.current_time >= 1:
            self.current_time -= 1

        if self.current_time > 10:
            text = self.font.render(str(self.current_time), False, Colors.colors.get("BLACK"))
            screen.blit(text, (self.screensize[0] / 2 - 20, 10))
        if self.current_time <= 10:
            text = self.font.render(str(self.current_time), False, Colors.colors.get("RED"))
            screen.blit(text, (self.screensize[0] / 2 - 20, 10))
