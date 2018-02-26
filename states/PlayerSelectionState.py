import pygame
from states.State import State


class PlayerSelectionState(State):

    # TODO Implement player selection

    def __init__(self, name, handler, img):
        super().__init__(name)
        self.handler = handler
        self.img = img

    def update(self, screen):
        pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        screen.blit(self.img, [0, 0])

        if (14 < pygame.mouse.get_pos()[0] < 323 and pressed) and (590 < pygame.mouse.get_pos()[1] < 740 and pressed):
            self.handler.getStateManager().setCurrentState("GameState")
