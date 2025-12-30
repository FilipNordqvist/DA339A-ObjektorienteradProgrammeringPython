class lab8():



    def showMenu(self): 
        while True:
            print("Select one:")
            print("1. Countdown")
            print("2. Add numbers")
            print("3. Compare numbers")
            print("4. Factorial")
            print("5. Randomize")
            print("6. Temperature")
            print("0. Exit")

            choice = self.makeChoice()
            print("Du valde: ", choice)
            
            if choice == 0:
                break

    
    def makeChoice(self):
        choice = int(input("Make a choice:"))
        return choice
        

lab = lab8()    
lab.showMenu()