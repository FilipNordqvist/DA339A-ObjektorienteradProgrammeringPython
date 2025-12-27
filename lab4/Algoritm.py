class Algoritm:
    def app():
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
    
    app()


