import pygame
from src.Attack import Attack


class CustomAttack(Attack):
    def __init__(self, player, damage, handler, x_speed, y_speed, image=None, ychange=0, animationQueue=None):
        self.player = player
        self.damage = damage
        self.handler = handler
        self.animationQueue = animationQueue
        super().__init__(self.player, self.damage, self.handler)
        self.attacksprite = pygame.image.load("media/Misc/Projectile.png")
        if image is not None:
            self.attacksprite = image
        self.left_attack = pygame.transform.flip(self.attacksprite, False, True)
        self.right_attack = self.attacksprite
        self.changex = x_speed
        self.changey = y_speed
        self.cust_y_change = ychange
        self.rect = pygame.Rect(self.player_x, self.player_y, self.attacksprite.get_width(), self.attacksprite.get_height())
        self.rect.x = self.player.rect.x + (self.player.width * .5) - (self.attacksprite.get_width() * .5)
        self.rect.y = self.player.rect.y + (self.player.height * .5) - (self.attacksprite.get_height() * .5)

    def update(self, screen):
        self.rect.x += self.changex
        self.changey += self.cust_y_change
        self.rect.y += self.changey
        self.checkPlat()
        if self.animationQueue is not None:
            screen.blit(self.animationQueue.get(), (self.rect.x, self.rect.y))
        else:
            if self.direction == -1:
                screen.blit(self.left_attack, (self.rect.x, self.rect.y))
            if self.direction == 1:
                screen.blit(self.right_attack, (self.rect.x, self.rect.y))
        if pygame.sprite.collide_rect(self.handler.getOtherPlayer(self.player), self):
            self.handler.getOtherPlayer(self.player).takeDamage(self.damage)
            self.handler.getAttackList().remove(self)
