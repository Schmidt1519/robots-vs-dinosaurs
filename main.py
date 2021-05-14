from weapon import Weapon
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
# from battlefield import Battlefield

if __name__ == '__main__':

    weapon1 = Weapon("Axe", 10)
    weapon2 = Weapon("Sword", 15)
    weapon3 = Weapon("Grenade", 50)

    dino1 = Dinosaur("Stegosaurus", 8)
    dino2 = Dinosaur("Raptor", 15)
    dino3 = Dinosaur("T-Rex", 40)

    robot1 = Robot("Megatron", weapon1)
    robot2 = Robot("Buzz", weapon2)
    robot3 = Robot("Tank", weapon3)

    fleet = Fleet()
    fleet.create_fleet(robot1)
    fleet.create_fleet(robot2)
    fleet.create_fleet(robot3)

    herd = Herd()
    herd.create_herd(dino1)
    herd.create_herd(dino2)
    herd.create_herd(dino3)

    robot1.attack_dinosaur(dino1)
    dino2.attack_robot(robot2)
    robot3.attack_dinosaur(dino3)