import robot


class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.health = 100
        self.energy = 150
        self.attack_power = attack_power
        self.attack_type = ('claw', 'bite', 'slash')


    def attack_robot(self, robot_to_attack):
        print(f'{self.type} attacked {robot_to_attack.name}')
        self.energy -= 10
        robot_to_attack.health -= self.attack_power
        print(f'{self.type} energy is now {self.energy}')
        print(f'{robot_to_attack.name} health is now {robot_to_attack.health}')
