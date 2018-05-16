import json


class Settings():
    def __init__(self):
        with open("user/preferences.json", 'r') as outfile:
            self.json = json.load(outfile)

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

    def write(self):
        with open("user/preferences.json", 'w') as outfile:
            json.dump(self.json, outfile)
