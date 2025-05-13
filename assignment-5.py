# Base class
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe
        self.__identity = "Secret"  # Encapsulation: private attribute

    def reveal_identity(self):
        return f"{self.name}'s identity is {self.__identity}."

    def set_identity(self, real_name):
        self.__identity = real_name

    def display_power(self):
        return f"{self.name} uses {self.power}!"

# Subclass
class FlyingHero(Superhero):
    def __init__(self, name, power, universe, flight_speed):
        super().__init__(name, power, universe)
        self.flight_speed = flight_speed

    def display_power(self):
        return f"{self.name} flies at {self.flight_speed} km/h using {self.power}!"

# Create objects
hero1 = Superhero("ShadowStrike", "Invisibility", "DarkVerse")
hero1.set_identity("Liam Fox")

hero2 = FlyingHero("SkyBlaze", "Fire Wings", "AeroVerse", 900)

print(hero1.display_power())
print(hero1.reveal_identity())
print(hero2.display_power())
