class lab10:
    def __init__(self,number_to_find):
        self.number_to_find = number_to_find
        self.testArray = [32, 27, 64, 18, 95, 14, 90, 70, 60, 37]

    def uppgift1(self):
        for i in self.testArray:
            if i == self.number_to_find:
                print(f"{self.number_to_find} hittades i arrayen")
                return
        else:
            print(f"Talet {self.number_to_find} fanns inte i arrayen")
    
number = int(input("Vilket nummer vill du hitta i arrayen?"))
lab = lab10(number)
lab.uppgift1()