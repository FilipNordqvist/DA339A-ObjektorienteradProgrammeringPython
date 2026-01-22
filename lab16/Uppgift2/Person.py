from Telefon import Telefon
from TelefonTyp import TelefonTyp

class Person:
    def __init__(self, namn, nummer, tel_typ):
        #Skapar ett Telefon-objekt
        ny_telefon = Telefon(nummer, tel_typ)

        self.namn = namn
        self.telefon = ny_telefon

    #Getters och setters
    def get_namn(self):
        return self.namn

    def get_telefon(self):
        return self.telefon

    def set_namn(self, namn):
        self.namn = namn

    def set_telefon(self, telefon):
        self.telefon = telefon

    def __str__(self):
        return f"{self.namn} har numret {self.telefon}"