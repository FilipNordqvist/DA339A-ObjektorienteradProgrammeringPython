from Person import Person
from TelefonTyp import TelefonTyp

"""
Klass som håller kontakter i en lista och returnerar vid anrop
"""
class Kontaktbok():
    def __init__(self):
        self.persons = []
        
    #Lägger ett person objekt i listan
    def add_to_phonebook(self,person):
        self.persons.append(person)
        
    #returnar en lista med personer    
    def return_persons(self):
        for person in self.persons:
            print(person)
            
        
    