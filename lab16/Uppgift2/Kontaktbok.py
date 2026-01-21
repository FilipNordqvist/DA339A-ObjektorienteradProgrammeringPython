from Telefon import Telefon
from TelefonTyp import TelefonTyp
from Person import Person


class Kontaktbok():
    
    def main():
        telefon = Telefon("+46 70 71234", TelefonTyp.ARBETE)
        print(telefon)

        person = Person("Homer simpson", telefon)
        print(person)
        
        
    if __name__ == "__main__":
        main()
