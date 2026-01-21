from Telefon import Telefon

class Person:
    def __init__(self, namn, telefon):
        self.namn = namn
        self.telefon = telefon

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
