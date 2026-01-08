from DogOwner import DogOwner

class DogDayCare:

    def __init__(self,cost_for_one_dog,dog_owner):
        self.cost_for_dog = cost_for_one_dog
        self.dog_owner = None
        
    def add_dog(self,dog,number):
        None
        
    def calculate_cost(self,dog_owner):
        None

    def member_registration(self):
        owner_name = input("Vad heter du? ")
        address = input("Vad är din adress? ")
        nr_dogs = input("Hur många hundar har du? ")# Hur lägger jag till dessa i add_dog?
        owner = DogOwner(owner_name,address,nr_dogs)
        owner.set_adress(address)

    def print_dog_owner_stats(self):
        print("Du är en medlem nu!")
        print(f"Name: {DogOwner.get_name}")
        print(f"Adress: {DogOwner.get_adress}")
        print(f"Antal hundar: {DogOwner.get_number_of_dogs}")
        print("Hund info: (Namn, Kön och ålder)")
        print(f"{DogOwner.get_dog}")
        
