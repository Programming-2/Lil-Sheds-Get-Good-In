import pygame
import os
from levels.IceLevel import IceLevel
from utils.Colors import colors
from utils.Handler import Handler
from states.GameState import GameState
from states.ControlState import ControlState
from states.EndGameState import EndGameState
from states.MainMenuState import MainMenuState
from states.MapSelectionState import MapSelectionState
from states.PlayerSelectionState import PlayerSelectionState
from states.HiddenPlayerState import HiddenPlayerState
from states.SettingsState import SettingsState
from utils.StateManager import StateManager
from states.PausedState import PausedState
from inputmanager.KeyboardManager import KeyboardManager


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
mainMenu = pygame.image.load("media/Screens/NewtitleScreen2.png").convert()
testProjectile = pygame.image.load("media/Misc/projectileTest.png").convert()
testControlScreen = pygame.image.load("media/Screens/ControlScreen.png").convert()
playerSelectScreen = pygame.image.load("media/Screens/LilShedCharacterSelect.png").convert_alpha()
mapSelectionScreen = pygame.image.load("media/Screens/MapSelection.png").convert()
pauseScreen = pygame.image.load("media/Screens/PauseScreen2.png").convert_alpha()
hiddenPlayerScreen = pygame.image.load("media/Screens/HiddenCharacterMenu.png").convert_alpha()
settingsState = pygame.image.load("media/Screens/SettingsState.png").convert_alpha()

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

# Key Manager
keyManager = KeyboardManager()

# Init handler
handler = Handler(screen, attackUpdateList, stateManager, None, level, keyManager)

# State Declaration
stateDict = {
    "GameState": GameState("GameState", screen, handler, attackUpdateList),
    "ControlState": ControlState("ControlState", handler, testControlScreen),
    "EndGameState": EndGameState("EndGameState", handler),
    "MainMenuState": MainMenuState("MainMenuState", mainMenu, handler),
    "MapSelectionState": MapSelectionState("MapSelectionState", handler, screen, mapSelectionScreen),
    "PlayerSelectionState": PlayerSelectionState("PlayerSelectionState", handler, playerSelectScreen),
    "PausedState": PausedState("PausedState", handler, pauseScreen),
    "HiddenPlayerState": HiddenPlayerState("HiddenPlayerState", handler, hiddenPlayerScreen),
    "SettingsState": SettingsState("SettingsState", handler, settingsState)
}
stateManager.setStateDict(stateDict)
# End State Declaration

# Vars
done = False
game_won = False
stateManager.setCurrentState("MainMenuState")

font = pygame.font.SysFont("Comic Sans MS", 16)

# Game loop
while not handler.getDone():
    handler.updateTick()
    stateManager.update(screen)
    text = font.render(str(int(clock.get_fps())), False, colors.get("BLACK"))
    screen.blit(text, (0, 780))

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
