from DogDayCare import DogDayCare


"""Skapar en instans av DogDayCare och skickar in 100 (pris per hund) 
till konstruktorn, och anropar sedan member_registration().
"""
def main():
    dog_day_care = DogDayCare(100)
    dog_day_care.member_registration()

"""Ser till att main() bara körs när filen startas direkt, inte när den importeras."""
if __name__ == "__main__":
    main()
