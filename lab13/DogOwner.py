from Dog import Dog

class DogOwner:

    def __init__(self, name, address, number_of_dogs):
        self.name = name
        self.address = address
        self.number_of_dogs = number_of_dogs
    

    def set_adress(self,address):
        self.address = address

    def get_adress(self):
        return self.address

    def get_dog(self):
        return self.dog

    def get_name(self):
        return self.name

    def get_number_of_dogs(self):
        return self.number_of_dogs
