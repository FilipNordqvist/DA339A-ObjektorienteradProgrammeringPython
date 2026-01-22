from Person import Person
from TelefonTyp import TelefonTyp

class Kontaktbok():
    def __init__(self):
        self.persons = []
        
    def add_to_phonebook(self,person):
        self.persons.append(person)
        
        
    def return_persons(self):
        for person in self.persons:
            print(person)
            
    def test_value(self):
        self.addNew(Person("Namn1", "telnr 1", TelefonTyp.privat))
        self.addNew(Person("Namn2", "telnr 2", TelefonTyp.arbete))
        self.addNew(Person("Namn3", "telnr 3", TelefonTyp.privat))
        self.addNew(Person("Namn4", "telnr 4", TelefonTyp.arbete))
        
    