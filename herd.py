from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()


    # def create_herd(self, dino):
    #     self.dinosaurs.append(dino)


    def create_herd(self):
        dino1 = Dinosaur("Stegosaurus", 50)
        dino2 = Dinosaur("Raptor", 65)
        dino3 = Dinosaur("T-Rex", 80)

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)