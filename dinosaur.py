import robot


class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.health = 100
        self.energy = 150
        self.attack_power = attack_power


    def attack_robot(self, robot_to_attack):
        pass
