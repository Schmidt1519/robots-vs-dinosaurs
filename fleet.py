from robot import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()


    # def create_fleet(self, robo):
    #     self.robots.append(robo)


    def create_fleet(self):
        weapon1 = Weapon("Axe", 10)
        weapon2 = Weapon("Sword", 15)
        weapon3 = Weapon("Grenade", 50)

        robot1 = Robot("Megatron", weapon1)
        robot2 = Robot("Buzz", weapon2)
        robot3 = Robot("Tank", weapon3)

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)