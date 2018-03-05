import pygame
from states.State import State


class PausedState(State):

    def __init__(self, name):
        super().__init__(name)

    def update(self, screen):
        pass
