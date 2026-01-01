from makeChoice import makeChoice
from countdown import countdown


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
                case _:
                    print("Ogiltigt val, testa igen")
                    active = False