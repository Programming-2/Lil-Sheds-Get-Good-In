import json


class Settings():
    def __init__(self):
        with open("user/preferences.json") as preferences:
            self.json = json.load(preferences)

    def setMusic(self):
        if self.json["music"]:
            self.json["music"] = False
        else:
            self.json["music"] = True

    def setSFX(self):
        if self.json["sfx"]:
            self.json["sfx"] = False
        else:
            self.json["sfx"] = True

    def useMusic(self):
        return self.json["music"]

    def useSFX(self):
        return self.json["sfx"]
