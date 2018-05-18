

class AnimationManager():
    def __init__(self, player, walkAnimation, crouchAnimation=None, attackAnimation=None, idleAnimation=None):
        self.walk_animation = walkAnimation
        self.crouch_animation = crouchAnimation
        self.attack_animation = attackAnimation
        self.idle_animation = idleAnimation

        self.player = player
    
    def update(self):
        if self.player.crouching:
            if self.player.walking:
                self.crouch_animation.loop(10)
            else:
                self.crouch_animation.displayFirst()
        elif self.player.walking:
            self.walk_animation.loop(10)
        elif not self.player.walking and not self.player.attacking and not self.player.crouching:
            self.walk_animation.displayFirst()
