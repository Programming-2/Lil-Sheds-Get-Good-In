import pygame


class AnimationManager:
    def __init__(self, player, walkAnimation, specialAnimation=None, crouchAnimation=None, attackAnimation=None, idleAnimation=None):
        self.walk_animation = walkAnimation
        self.crouch_animation = crouchAnimation
        self.attack_animation = attackAnimation
        self.idle_animation = idleAnimation
        self.special_animation = specialAnimation
        self.jumpsprite = player.jumpsprite

        self.player = player
    
    def update(self):
        if self.player.in_special and self.special_animation is not None:
            self.special_animation.loopFromStart(self.player.special_animation_delay)
        elif self.player.jumping:
            if self.player.facing == 1:
                self.player.sprite = self.jumpsprite
            elif self.player.facing == -1:
                self.player.sprite = pygame.transform.flip(self.jumpsprite, True, False)
        elif self.player.crouching and self.crouch_animation is not None:
            if self.player.walking:
                self.crouch_animation.loop(self.player.crouch_animation_delay)
            else:
                self.crouch_animation.displayFirst()
        elif self.player.walking:
            self.walk_animation.loop(self.player.walk_animation_delay)
        elif not self.player.walking and not self.player.attacking and not self.player.crouching:
            self.walk_animation.displayFirst()
            self.walk_animation.reset()
        else:
            self.player.sprite = self.player.stansprite
        
        if not self.player.in_special and self.special_animation is not None:
            self.special_animation.reset()
