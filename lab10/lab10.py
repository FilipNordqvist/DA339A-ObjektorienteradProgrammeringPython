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
    
    def uppgift3a(self):
        students = [
    ["Adam", "Ason", "661122", "35", "U"],
    ["Beata", "Bson", "770111", "38", "G"],
    ["Calle", "Ceson", "880222", "23", "U"],
    ["Dorotea", "Deson", "990311", "44", "VG"],
    ["Eivar", "Eson", "550423", "40", "G"],]
        
        for student in students: 
            if student[4] == "G" or student[4] == "VG":
                print(student[1],student[4])
            else:
                continue

        print("\nEfter omvandling:\n")

        #3b
        for student in students:
            if student[4] == "G":
                student[4] = 25
            elif student[4] == "VG":
                student[4] = 40
        #Nya betyg
        for student in students:
            if student[4] == 25 or student[4] == 40:
                print(student[0],student[1],student[4])
        
        def uppgift4(self):
            testArray = [3.3, 2.7, 6.4, 1.8, 9.5, 1.4, 9.0, 7.0, 6.5, 3.7]
        
        
    





    
lab = lab10()
lab.uppgift3a()