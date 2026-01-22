from Telefon import Telefon
from TelefonTyp import TelefonTyp
from Person import Person
from Kontaktbok import Kontaktbok

def main():
    
    #Iniitirerar ett Telefon-objekt
    telefon = Telefon("+46 70 71234", TelefonTyp.ARBETE)
    print(telefon)

    #Initierar ett Person-objekt
    person = Person("Homer Simpson", "0701234567", TelefonTyp.HEM)
    print(person)
    
    #Initierar ett kontakt objekt
    kontakt = Kontaktbok()
    
    #Lägger till Person-objekt i kontaktbokens lista
    kontakt.add_to_phonebook(Person("Namn1", "telnr 1", TelefonTyp.HEM))
    kontakt.add_to_phonebook(Person("Namn2", "telnr 2", TelefonTyp.ARBETE))
    kontakt.add_to_phonebook(Person("Namn3", "telnr 3", TelefonTyp.HEM))
    kontakt.add_to_phonebook(Person("Namn4", "telnr 4", TelefonTyp.ARBETE))
    kontakt.add_to_phonebook(person)
    kontakt.return_persons()

if __name__ == "__main__":
    main()
