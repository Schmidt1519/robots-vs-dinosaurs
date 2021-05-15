class Robot:
    def __init__(self, name, Weapon):
        self.name = name
        self.health = 100
        self.power_level = 150
        self.weapon = Weapon
        self.weapon_choice = ('axe', 'sword', 'grenade', 'machete', 'rifle')


    def attack_dinosaur(self, dinosaur_to_attack):
        print(f'{self.name} attacked {dinosaur_to_attack.type}')
        self.power_level -= 10
        dinosaur_to_attack.health -= self.weapon.attack_power
        print(f'{self.name} power level is now {self.power_level}')
        print(f'{dinosaur_to_attack.type} health is now {dinosaur_to_attack.health}')
