from makeChoice import makeChoice
from countdown import countdown
from number import number


class showMenu:
    
    @staticmethod
    def theMenu():
        active = True

        while active:
            print("Select one:")
            print("1. Countdown")
            print("2. Add numbers")
            print("3. Compare numbers")
            print("4. Factorial")
            print("5. Randomize")
            print("6. Temperature")
            print("0. Exit")

            choice = makeChoice.choice()

            match choice:
                case 0:
                    active = False
                case 1:
                    countdown.count()
                case 2:
                    tal1 = int(input("Ange första numret: "))
                    tal2 = int(input("Ange andra numret: "))
                    result = number.addNumber(tal1,tal2)
                    print(f"Resultater är: {result}")
                case 3:
                    tal1 = int(input("Ange första numret: "))
                    tal2 = int(input("Ange andra numret: "))
                    number.compare(tal1, tal2)
                case 4:
                    print("Oj detta funkade?")
                case _:
                    print("Ogiltigt val, testa igen")
                    #active = False

                