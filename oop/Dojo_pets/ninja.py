import pets


class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet =  pet
        self. treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()

    def bathe(self):
        print(f"Giving {self.pet} a bath!")
        self.pet.noise()


rocco = pets.Dog("Rocco", "dog", ["fetch", "shake", "come", "lay_down"], "bark")
me = Ninja("ryan", "beitler", rocco , ["pupperoni", "crazins", "peanutbutter", "bacon"], "dry food")
xena = pets.Cat("xena", "cat", "too cool for tricks", "meow")

me.feed()
print(rocco)