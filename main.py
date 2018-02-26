import pygame
import os
from testLevel import TestLevel
from handler import Handler
from states.GameState import GameState
from states.ControlState import ControlState
from states.EndGameState import EndGameState
from states.MainMenuState import MainMenuState
from states.MapSelectionState import MapSelectionState
from states.PlayerSelectionState import PlayerSelectionState
from states.StateManager import StateManager

pygame.init()

# TODO Centralize image loading
# TODO Standardize naming conventions and casing
# TODO Determine better keybinds

size = (1100, 800)
screen = pygame.display.set_mode(size)
os.environ['SDL_VIDEO_CENTERED'] = '1'

level = TestLevel(screen)

background_image = pygame.image.load(level.getBackImg()).convert()
mainMenu = pygame.image.load("media/LilShedTitleScreen.png").convert()
testProjectile = pygame.image.load("media/projectileTest.png").convert()
testControlScreen = pygame.image.load("media/ControlScreen.png").convert()

pygame.display.set_caption("Lil' Shed's Get Good In™")

clock = pygame.time.Clock()

p1HitList = []
p2HitList = []

attackUpdateList = pygame.sprite.Group()

stateManager = StateManager(None)

handler = Handler(attackUpdateList, stateManager)

# State Declaration
stateDict = {
    "GameState": GameState("GameState", level, screen, handler, attackUpdateList),
    "ControlState": ControlState("ControlState", handler, testControlScreen),
    "EndGameState": EndGameState("EndGameState"),
    "MainMenuState": MainMenuState("MainMenuState", mainMenu, handler),
    "MapSelectionState": MapSelectionState("MapSelectionState"),
    "PlayerSelectionState": PlayerSelectionState("PlayerSelectionState")
}
stateManager.setStateDict(stateDict)
# End State Declaration

done = False
game_won = False
# stateManager.setCurrentState("GameState")
stateManager.setCurrentState("MainMenuState")
# stateManager.setCurrentState("ControlState")
# stateManager.setCurrentState("EndGameState")
# stateManager.setCurrentState("MapSelectionState")
# stateManager.setCurrentState("PlayerSelectionState")

while not handler.getDone():
    stateManager.update(screen)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
