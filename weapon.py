class Weapon:
    def __init__(self, type, attack_power):
        self.type = type
        self.attack_power = attack_power


    def weapon_punch(self):
        self.attack_power = 3

    def weapon_bat(self):
        self.attack_power = 4

    def weapon_claws(self):
        self.attack_power = 5

    def weapon_axe(self):
        self.attack_power = 7

    def weapon_sword(self):
        self.attack_power = 8

    def weapon_missile(self):
        self.attack_power = 12

    def weapon_grenade(self):
        self.attack_power = 15

