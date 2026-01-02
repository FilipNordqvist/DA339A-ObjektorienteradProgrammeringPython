class lab10:
    testArray = [32, 27, 64, 18, 95, 14, 90, 70, 60, 37,95]

    def uppgift1(self):
        number_to_find = 10
        for i in self.testArray:
            if i == number_to_find:
                print(f"{number_to_find} hittades i arrayen")
                return

        print(f"Talet {number_to_find} fanns inte i arrayen")

    def uppgift2a(self):
        biggest_number = max(self.testArray)
        result = []

        #För att få värde och index behövs enumerate, self.testArray.index(value) ger bara första träffen
        for index, value in enumerate(self.testArray):
            if value == biggest_number:
                result.append([value, index])
        
        print("Tal -> Index")
        for value, index in result:
            print(value," -> ", index)
    print()

    def uppgift2b(self):
        smallest_number = min(self.testArray)
        result = []

        for index, value in enumerate(self.testArray):
            if value == smallest_number:
                result.append([value,index])
        print("Tal -> Index")
        for value, index in result:
            print(value," -> ", index)


    
lab = lab10()
lab.uppgift2b()