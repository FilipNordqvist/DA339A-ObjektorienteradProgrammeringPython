from Telefon import Telefon
from TelefonTyp import TelefonTyp
from Person import Person
from Kontaktbok import Kontaktbok

def main():
    """telefon = Telefon("+46 70 71234", TelefonTyp.ARBETE)
    print(telefon)

    person = Person("Homer Simpson", telefon)
    print(person)"""
    
    kontakt = Kontaktbok()
    kontakt.add_to_phonebook()
    
    kontakt.return_persons()

if __name__ == "__main__":
    main()
