import pygame
from inputmanager.KeyboardManager import KeyboardManager

keyboardManager = KeyboardManager()

while True:
    keyboardManager.update()
    print(keyboardManager.keysDown[pygame.K_a])
