from TelefonTyp import TelefonTyp


class Telefon:
    def __init__(self, nummer, telefon_typ):
        self._nummer = nummer
        self._telefon_typ = telefon_typ

    def get_nummer(self):
        return self._nummer

    def get_telefon_typ(self):
        return self._telefon_typ

    def set_nummer(self, nummer):
        self._nummer = nummer

    def set_telefon_typ(self, telefon_typ):
        self._telefon_typ = telefon_typ

    def __str__(self):
        return f"Telefonnummer: {self._nummer}, Typ: {self._telefon_typ}"
