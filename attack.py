class Attack():

    def __init__(self, attack_name, damage, cooldown, range, sound):
        self.attack_name = attack_name
        self.damage = damage
        self.cooldown = cooldown
        self.range = range
        self.sound = sound

    def attack(self):
        if self.cooldown == 0:
            self.sound.play()
            return self.damage

    def update(self):
        self.cooldown - 1