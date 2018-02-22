import pygame
import os
from player import Player
from testLevel import TestLevel
from healthbar import HealthBar
from timer import Timer
from handler import Handler
from colors import colors

pygame.init()

font = pygame.font.SysFont("Comic Sans MS", 36)
DeadText = font.render("KO", True, colors.get("RED"))

size = (1100, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")
os.environ['SDL_VIDEO_CENTERED'] = '1'

level = TestLevel(screen)

background_image = pygame.image.load(level.getBackImg()).convert()
testProjectile = pygame.image.load("media/projectileTest.png").convert()

platformArray = level.platformGroup

pygame.display.set_caption("Lil' Shed's Get Good In™")

clock = pygame.time.Clock()

p1HitList = []
p2HitList = []

attackUpdateList = pygame.sprite.Group()

handler = Handler(attackUpdateList, None)

player1 = Player(100, 20, "Yes", "No", "Will", 200, 100, platformArray, handler, .3, 1)
player2 = Player(100, 20, "Yes", "No", "Jaccob Bonkley", 850, 100, platformArray, handler, .3, 2)

handler.setPlayer1(player1)
handler.setPlayer2(player2)

# attack = Attack(player1.x, player1.y, 10, "melee", 5, 2, 2, screen, testProjectile, 100, handler)

p1hpbar = HealthBar(screen, "topleft", player1.health)
p2hpbar = HealthBar(screen, "topright", player2.health)
timer = Timer(300, screen)
count = 0

done = False
game_won = False
while not done:

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
