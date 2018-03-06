import pygame
import os
from levels.IceLevel import IceLevel
from utils.Handler import Handler
from states.GameState import GameState
from states.ControlState import ControlState
from states.EndGameState import EndGameState
from states.MainMenuState import MainMenuState
from states.MapSelectionState import MapSelectionState
from states.PlayerSelectionState import PlayerSelectionState
from utils.StateManager import StateManager
from states.PausedState import PausedState

pygame.init()

# TODO Centralize image loading
# TODO Standardize naming conventions and casing
# TODO Determine better keybinds

# Screen init
size = (1100, 800)
screen = pygame.display.set_mode(size)
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Loading level
level = IceLevel(screen)

# Loading Images
background_image = pygame.image.load(level.getBackImg()).convert()
mainMenu = pygame.image.load("media/LilShedTitleScreen.png").convert()
testProjectile = pygame.image.load("media/projectileTest.png").convert()
testControlScreen = pygame.image.load("media/ControlScreen.png").convert()
playerSelectScreen = pygame.image.load("media/LilShedCharacterSelect.png")
mapSelectionScreen = pygame.image.load("media/MapSelection.png")
pauseScreen = pygame.image.load("media/PauseScreen.png").convert()

# Setting up screen stuff
pygame.display.set_caption("Lil' Shed's Get Good In™")

clock = pygame.time.Clock()

# Init player hit lists
p1HitList = []
p2HitList = []

# Init attack list
attackUpdateList = pygame.sprite.Group()

# Init state manager
stateManager = StateManager(None)

# Init handler
handler = Handler(attackUpdateList, stateManager, None, level)

# State Declaration
stateDict = {
    "GameState": GameState("GameState", screen, handler, attackUpdateList),
    "ControlState": ControlState("ControlState", handler, testControlScreen),
    "EndGameState": EndGameState("EndGameState"),
    "MainMenuState": MainMenuState("MainMenuState", mainMenu, handler),
    "MapSelectionState": MapSelectionState("MapSelectionState", handler, screen, mapSelectionScreen),
    "PlayerSelectionState": PlayerSelectionState("PlayerSelectionState", handler, playerSelectScreen),
    "PausedState": PausedState("PausedState", handler, pauseScreen)
}
stateManager.setStateDict(stateDict)
# End State Declaration

# Vars
done = False
game_won = False
stateManager.setCurrentState("MainMenuState")

# Game loop
while not handler.getDone():
    stateManager.update(screen)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
