class Cooldown():
    def __init__(self, cooldownduration):
        self.total_cooldown = cooldownduration
        self.current_cooldown = cooldownduration
        self.current_tick = 0
        self.done = True

        self.count = 0

    def getTotalCooldown(self):
        return self.total_cooldown

    def getCurrentCooldown(self):
        return self.current_cooldown

    def isDone(self):
        return self.done

    def changeDuration(self, newDuration):
        self.total_cooldown = newDuration

    def changeCurrentCooldown(self, change):
        self.current_cooldown += change

    def update(self):
        if self.count == 0:
            self.done = False
            self.current_cooldown = 0
            self.count += 1
        self.current_tick += 1
        self.current_cooldown = self.current_tick / 60
        if self.current_cooldown >= self.total_cooldown:
            self.current_tick = 0
            self.count = 0
            self.done = True
