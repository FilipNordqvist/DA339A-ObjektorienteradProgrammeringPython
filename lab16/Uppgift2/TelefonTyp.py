from enum import Enum

class TelefonTyp(Enum):
    privat = 0
    arbete = 1
    
    def __str__(self):
        return f"Telefon typ: {self.name}"