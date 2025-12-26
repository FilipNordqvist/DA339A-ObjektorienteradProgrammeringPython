class Calculator():
    def app():
        print("Välkommmen till världens bästa kalkylator!")

        #celsius = 25

        celsius = int(input("Tempratur i C? "))

        farenheit = (celsius * 1.8) + 32

        print(f"{celsius}C grader i Sverige motsvarar {farenheit}F grader i USA!")
      
    app()
