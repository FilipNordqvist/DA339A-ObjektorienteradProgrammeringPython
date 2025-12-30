class lab8():



    def showMenu(self):
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

            self.makeChoice()  

    
    def makeChoice(self):
        choice = int(input("Make a choice:"))
        
        match choice:
            case 1:
                self.countdown()
            case _:
                print("Ogiltigt val, testa igen")

    def countdown(self):
        for i in range(10):
            print(i-1, end=" ")
        print()
    
           

lab = lab8()    
lab.showMenu()