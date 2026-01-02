class makeChoice:
    
    @staticmethod
    def choice():
        while True:
            choice = input("Make a choice:")
            try:
                return int(choice)
            except ValueError:
                print("fel inmatning, ange ett nummer mellan 1 - 6 eller 0 för att avsluta")
     
        