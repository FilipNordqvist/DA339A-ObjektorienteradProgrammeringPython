from Telefon import Telefon
from TelefonTyp import TelefonTyp
from Person import Person

def main():
    telefon = Telefon("+46 70 71234", TelefonTyp.ARBETE)
    print(telefon)

    person = Person("Homer Simpson", telefon)
    print(person)

if __name__ == "__main__":
    main()
