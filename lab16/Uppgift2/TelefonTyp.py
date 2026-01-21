from enum import Enum

class TelefonTyp(Enum):
    ARBETE = "arbete"
    HEM = "hem"
    
    def __str__(self):
        return f"Telefon typ: {self.name}"
