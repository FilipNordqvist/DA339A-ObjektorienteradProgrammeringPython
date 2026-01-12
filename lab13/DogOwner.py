from Dog import Dog

class DogOwner:

    def __init__(self, name, address, number_of_dogs):
        self.name = name
        self.address = address
        self.number_of_dogs = number_of_dogs
        self.dog = None
        
    def get_dog(self):
        age = int(input("Hur gammal är din hund? "))
        gender = input("Är din hund Hona eller Hane? ")
        name = input("Vad heter din hund? ") 
        self.dog = Dog(age,gender, name)  # Skapar Dog objektet, self betyder att du pratar med samma instans av objektet
        return self.dog
    

    def set_adress(self,address):
        if not address.strip():
             raise ValueError("Vänligen ange en adress")
        self.address = address

    def get_adress(self):
        return self.address


    def get_name(self):
        return self.name

    def get_number_of_dogs(self):
        return self.number_of_dogs
