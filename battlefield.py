import robot
import dinosaur
from herd import Herd
from fleet import Fleet
import random


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    def run_game(self):  # master function to call all methods
        self.display_welcome()
        self.chose_team()
        self.first_turn()


    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs!')

        print('Each Robot and Dinosaur begin with 100 health.')
        print('Each character begins with 150 energy/power level points')
        print('and attacking requires 10 energy/power level points.')

        print('Robots belong to a Fleet and Dinosaurs belong to a Herd.')
        print('A winner is declared once all Robots in a fleet or ')
        print('all Dinosaurs in a Herd have 0 health.')


    def chose_team(self):
        choose_team = int(input('Choose your team: (1) Robots; (2) Dinosaurs')
            if choose_team == 1:
                print ('You chose the fleet of Robots')
            elif choose_team == 2:
                print('You chose the herd of Dinosaurs')


    def first_turn(self):
        turn = random.randint(1, 2)
        if turn == 1:
            self.robo_turn()
            print('Robots are up first')
        else:
            self.dino_turn()
            print('Dinosaurs are up first')


    def battle(self):  # boolean for dino/robot turn to determine
        self.display_winners()  # check for winner


    def dino_turn(self):
        self.show_robo_opponent_options()

        # self.herd.dinosaurs[0].attack_robot(self.fleet.robots[0])

        i = 0
        for i in self.fleet.robots:
            print(self.fleet.robots[i].health)
            i += 1

    #     dino_selection = input(f'Choose your dinosaur: {')
    #     robot_attack_selection = input(f'Choose your robot to attack: {Fleet.robots}')
    #     if dino_selection == {Herd.dinosaurs}:
    #         robot.attack_dinosaur(robot_attack_selection)


    def robo_turn(self, robot):
        self.show_dino_opponent_options()



    # def show_dino_opponent_options(self):
    #     i = 0
    #     for element in self.fleet.robots[i]:
    #       print(f' {element.name} health is {element.health}')
    #       i += 1


    def show_dino_opponent_options(self):
       if self.fleet.robots[0].health >= 0:
           print(f' {self.fleet.robots[0].name} health is {self.fleet.robots[0].health}')
       if self.fleet.robots[1].health >= 0:
           print(f' {self.fleet.robots[1].name} health is {self.fleet.robots[1].health}')
       if self.fleet.robots[2].health >= 0:
           print(f' {self.fleet.robots[2].name} health is {self.fleet.robots[2].health}')


    def show_robo_opponent_options(self):
       if self.herd.dinosaurs[0].health >= 0:
           print(f' {self.herd.dinosaurs[0].type} health is {self.herd.dinosaurs[0].health}')
       if self.herd.dinosaurs[1].health >= 0:
           print(f' {self.herd.dinosaurs[1].type} health is {self.herd.dinosaurs[1].health}')
       if self.herd.dinosaurs[2].health >= 0:
           print(f' {self.herd.dinosaurs[2].type} health is {self.herd.dinosaurs[2].health}')


    def display_winners(self):
        if self.fleet.robots == 0:
            print("Dinosaurs win!")
        elif self.herd.dinosaurs == 0:
            print("Robots win!")