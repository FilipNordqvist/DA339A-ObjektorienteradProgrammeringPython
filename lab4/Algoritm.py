import random


class Algoritm:

    def uppgift1():
        while True:
            tal1 = input("Ange första talet: ")
            try:
                tal1 = int(tal1) 
                break
            except ValueError:
                print("Fel inmatning")

        while True:
            tal2 = input("Ange andra talet: ")
            try:
                tal2 = int(tal2) 
                break
            except ValueError:
                print("Fel inmatning")

        if tal1 > tal2 and tal1 != tal2:
           print(f"Tal 1: {tal1} är störst")
        elif tal1 < tal2 and tal1 != tal2:
           print(f"Tal 2: {tal2} är störst")
        else:
            print(f"Första talet: {tal1} och andra talet: {tal2} är lika stora")
    
    #Starta uppgift 2 s4 lab4
    def uppgift2():
        while True:
            tal1 = input("Ange första talet: ")
            try:
                tal1 = int(tal1) 
                break
            except ValueError:
                print("Fel inmatning")

        while True:
            tal2 = input("Ange andra talet: ")
            try:
                tal2 = int(tal2) 
                break
            except ValueError:
                print("Fel inmatning")

        while True:
            tal3 = input("Ange andra talet: ")
            try:
                tal3 = int(tal3) 
                break
            except ValueError:
                print("Fel inmatning")

        if tal1 == tal2 == tal3:
            print("Talen är lika stora")

        elif tal1 > tal3 and tal2 > tal3:
            print(f"Tal 1: {tal1} och Tal 2: {tal2} är störst")

        elif tal1 > tal2 and tal3 > tal2:
            print(f"Tal 1: {tal1} och Tal 3: {tal3} är störst")

        elif tal2 > tal1 and tal3 > tal1:
            print(f"Tal 2: {tal2} och Tal 3: {tal3} är störst")

    def uppgift3():

        number = int(input("Vilken multiplakationstabell vill du ha?"))
        for x in range(1,11):
            print(x*number)
    
    def uppgift4():
        for x in range(1,11):
            for y in range(1,11):
                print(f"{x*y:4}", end="")
            print()
    
    def uppgift5():

        total = 0

        numbers = []
        while True:
            tal1 = input("Ange dina tal (-1 för att avsluta): ")
            try:
                tal1 = int(tal1)
                if tal1 == -1:
                    break
                numbers.append(tal1)
            except ValueError:
                print("Fel inmatning")

        for x in numbers:
            total += x
            medel = total/len(numbers)
        print(f"{medel:.0f}")

    def uppgift6():
        hemligtTal = random.randint(1,10)

        while True:
            try:
                tal1 = int(input("Gissa talet 1-10: "))
            except ValueError:
                    print("Ange ett heltal!")
                    continue
            
            if tal1 > hemligtTal:
                print("Talet är för stort")
            if tal1 < hemligtTal:
                print("Talet är för litet")
            elif tal1==hemligtTal:
                print("Du vann!")
                break
            else:
                print("Du gissade fel, testa igen!")
    
    def uppgift7():
        kostnad = 0
        kvitto = []

        while True:
            val = int(input("Välj\n1.Kontroll\n2.Rengöring\n3.Laga ett hål\n-1 för Klar "))
            if val == 1:
                kostnad += 600
                kvitto.append("Kontroll av tänder 600kr")
            elif val == 2:
                kostnad += 300
                kvitto.append("Rengöring av tänder 300kr")
            elif val == 3:
                kvitto.append("Lagning av tänder 1500kr")
                kostnad += 1500
            elif val == -1:
                if kostnad >= 3000:
                    kostnad *= 0.9
                break
            else:
                 print("Fel val, försök igen")         

        print("\nKvitto:")    
        for x in kvitto:
            print(x)
        print(f"Total kostnad för behanlingar: {kostnad:.2f} kr")

    def uppgift8():
        räknare = 0
        antalRättAnv1 = 0
        antalRättAnv2 = 0
        antalRundor = 10

        while räknare < antalRundor:
                talAnv1 = int(input("användare1 ange ett tal"))
                talAnv2 = int(input("användare2 ange ett tal"))
                if talAnv1 == talAnv2:
                    print("Rundan blev oavgjord")
                elif talAnv1 > talAnv2:
                    print("Användare 1 vann rundan")
                    antalRättAnv1 += 1
                elif talAnv2 > talAnv1:
                    print("Användare 2 vann rundan")
                    antalRättAnv2 += 1
                räknare += 1
        if antalRättAnv1==antalRättAnv2:
                print("Matchen blev oavgjord")
        elif antalRättAnv1 > antalRättAnv2:
                print("Användare 1 vann matchen")
        elif antalRättAnv2 > antalRättAnv1:
                print("Användare 2 vann matchen")

    def uppgift9():

        

                

    uppgift9()
      



