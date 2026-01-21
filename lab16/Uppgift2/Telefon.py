from TelefonTyp import TelefonTyp

class Telefon:
    def __init__(self, nummer, telefon_typ):
        self.nummer = nummer
        self.telefon_typ = telefon_typ

    def get_nummer(self):
        return self.nummer

    def get_telefon_typ(self):
        return self.telefon_typ

    def set_nummer(self, nummer):
        self.nummer = nummer

    def set_telefon_typ(self, telefon_typ):
        self.telefon_typ = telefon_typ

    def __str__(self):
        return self.nummer + " (" + self.telefon_typ.value + ")"
