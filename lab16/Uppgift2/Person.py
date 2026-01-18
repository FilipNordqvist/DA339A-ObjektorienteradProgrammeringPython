from Telefon import Telefon

class Person():
    
    def __init__(self,nummer):
        self.nummer = nummer
        
    def get_nummer(self):
        return self.nummer
    
    def set_nummer(self, nummer):
        self.nummer = nummer