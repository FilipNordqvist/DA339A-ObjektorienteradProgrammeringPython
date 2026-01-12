from DogOwner import DogOwner
from Dog import Dog


class DogDayCare:
    def __init__(self, cost_for_one_dog):
        self.cost_for_dog = cost_for_one_dog
        self.dog_owner = None

    def member_registration(self):
        owner_name = input("Vad heter du? ")
        address = input("Vad är din adress? ")
        nr_dogs = input("Hur många hundar har du? ")

        self.dog_owner = DogOwner(
            owner_name, address, nr_dogs
        )  # Skapar dogowner objektet, self betyder att du pratar med samma instans av objektet

        dog = self.dog_owner.get_dog()

        self.add_dog(dog)

        self.print_dog_owner_stats()

    def add_dog(self, dog):
        self.dog_owner.dog = dog

    def print_dog_owner_stats(self):
        print("Du är en medlem nu!")

        print(f"Name: {self.dog_owner.get_name()}")
        print(f"Adress: {self.dog_owner.get_adress()}")
        print(f"Antal hundar: {self.dog_owner.get_number_of_dogs()}")

        print("Hund info: (Namn, Kön och ålder)")
        dog = self.dog_owner.dog
        print(dog.get_name(), dog.get_gender(), dog.get_age())

    def calculate_cost(self, dog_owner):
        None
