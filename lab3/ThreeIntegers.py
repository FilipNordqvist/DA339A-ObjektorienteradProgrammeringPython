class Integers():
    def app():
        tal1 = int(input("Ange tal 1: "))
        tal2 = int(input("Ange tal 2: "))
        tal3 = int(input("Ange tal 3: "))

        sum = tal1 + tal2 + tal3
        average = (tal1 + tal2 + tal3)/3
        product = tal1 * tal2 * tal3
        
        if tal1 < tal2 and tal1 < tal3:
            smallest = tal1
        elif tal2 < tal1 and tal2 < tal3:
            smallest =tal2
        else:
            smallest= tal3
        
        if tal1 > tal2 and tal1 > tal3:
            largest = tal1
        elif tal2 > tal1 and tal2 > tal3:
            largest = tal2
        else:
            largest = tal3
        
        print(f"Summan av talen är {sum} medel av är {average}, produkten av talen är {product}.")
        print(f"Det minsta talen är {smallest} och det största talet är {largest}")

    app()