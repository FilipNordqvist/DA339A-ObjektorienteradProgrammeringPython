class Calculator():
    def app():
        print("Välkommmen till världens bästa kalkylator!")
        #farenheit = 32

        farenheit = int(input("Tempratur i F? "))

        celsius = 5/9 * (farenheit - 32)

        print(f"{farenheit}F grader i USA är {celsius:.0f} C grader i Sverige")
    app()
