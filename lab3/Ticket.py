class Ticket():
    def app():
        print("-----Välkkommen-----")
        print("Filmen kostar 100kr/per")
        print("Barn får 25% rabatt")

        price = 100
        discount = 0.25

        name = (input("Ange ditt namn: "))
        adult = int(input("Antal vuxna: "))
        child = int(input("Antal barn: "))

        adult_price = price * adult
        child_price = price * (1 - discount) * child
        total = adult_price + child_price

        print("\nDitt kvitto:")
        print(f"Namn: {name}")
        print(f"Totalt att betala: {total} kr")
        

    
    app()