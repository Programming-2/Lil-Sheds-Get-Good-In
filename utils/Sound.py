import pygame


class Sound:
    def __init__ (self,name):
        self.name = name
        try:
            self.sound = pygame.mixer.Sound("media/Audio/" + self.name + ".ogg")
            self.useSound = True
        except pygame.error:
            self.useSound = False

    def playSound(self):
        #print(useSound)
        if self.useSound:
            self.sound.play()
