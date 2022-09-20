
class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        self.noise = noise

    def sleep(self):
        self.energy +=25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self
    
    def make_noise(self):
        print(f"{self.noise}")
        return self

    def __repr__(self):
        return f"Name:{self.name}, Type: {self.type}, Tricks: {self.tricks}, Health: {self.health}, Energy: {self.energy}, Noise: {self.noise} "


class Dog(Pet):
    def __init__(self, name, type, tricks, noise):
        super().__init__(name, type, tricks, noise)

    def play(self):
        self.health += 10
        self.energy -= 5
        return self


class Cat(Pet):
    def __init__(self, name, type, tricks, noise):
        super().__init__(name, type, tricks, noise)

    def play(self):
        if self.energy < 100:
            print(f"{self.name} ignores you")
        else:
            self.health += 10
            self.energy -= 5