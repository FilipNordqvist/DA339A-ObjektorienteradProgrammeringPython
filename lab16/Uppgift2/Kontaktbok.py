from Telefon import Telefon
from TelefonTyp import TelefonTyp
from Person import Person


class Kontaktbok():
    
    def main():
        telefon1 = Telefon("+46 70 71234", TelefonTyp.arbete)

        person1 = Person("Homer simpson", telefon1)
        
        print(telefon1.__str__)
        
        
        
     
        
    if __name__ == "__main__":
        main()