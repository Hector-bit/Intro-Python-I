class Animals:
    def __init__(self, skin_type, species, weight, color, name, enviroment):
        self.skin_type = skin_type
        self.species = species
        self.weight = weight
        self.color = color
        self.name = name
        self.enviroment = enviroment
    def move(self):
        if self.enviroment == "WATER":
            movement = "swims"
        elif self.enviroment == "AIR":
            movement = "flys"
        else:
            movement = "walks"
        print(f"{self.name} {movement}")


class Dog(Animals):
    def __init__(self, name, weight, color):
        super().__init__("fur", "DOG", weight, color, name, "LAND")
    def speak(self):
        print("WOOF!")
    def move(self):
        print(f"{self.name} walks.")