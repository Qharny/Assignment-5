# Polymorphism Challenge

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Mammal(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def move(self):
        return f"{self.name} moves by running."
    
    

class Bird(Animal):
    def __init__(self, name, age, beak_type):
        super().__init__(name, age)
        self.beak_type = beak_type
        

    def move(self):
        return f"{self.name} moves by flying."
        

class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type
        

    def move(self):
        return f"{self.name} moves by swimming."    
    

lion = Mammal("Lion", 5, "Golden")
eagle = Bird("Eagle", 3, "Hooked")
salmon = Fish("Salmon", 2, "Freshwater")

animals = [lion, eagle, salmon]


for animal in animals:
    print(animal.move())