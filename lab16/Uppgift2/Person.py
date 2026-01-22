from Telefon import Telefon
from TelefonTyp import TelefonTyp

class Person:
    def __init__(self, namn,nummer, telefon):
        self.namn = namn
        self.telefon = telefon
        
        ny_telefon = Telefon(nummer,telefon)
        self.namn = namn
        self.telefon = ny_telefon

    def get_namn(self):
        return self.namn

    def get_telefon(self):
        return self.telefon

    def set_namn(self, namn):
        self.namn = namn

    def set_telefon(self, telefon):
        self.telefon = telefon

    def __str__(self):
        return self.namn + " har numret " + str(self.telefon)
