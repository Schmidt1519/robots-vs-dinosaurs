import dinosaur


class Robot:
    def __init__(self, name, Weapon):
        self.name = name
        self.health = 100
        self.power_level = 150
        self.weapon = Weapon


    def attack_dinosaur(self, dino_to_attack):
        pass