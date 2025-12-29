class AskName:
    def uppgift3():
        name = input("Vad heter du? ")
        nameLength = len(name)
        if nameLength < 5:
            print(f"{name} är ett kort namn med {nameLength} st bokstäver")
        else:
            print(f"{name} är ett långt namn med {nameLength} st bokstäver")
    
    uppgift3()
