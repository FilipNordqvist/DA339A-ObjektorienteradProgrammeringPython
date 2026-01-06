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
        
        biggest_number = max(testArray)
        smallest_number = min (testArray)
        average_number = 0

        for value in testArray:
            average_number += value
             
        average_number = average_number / len(testArray)
        print(f"Medelvärde: {average_number:.1f}, Största tal: {biggest_number} och minsta tal: {smallest_number}")

    def uppgift5(self):
        testArray1 = [3.3, 2.7, 6.4, 1.8, 9.5, 1.4, 9.0, 7.0, 6.5, 3.7]
        testArray2 = [5.6, 4.7, 2.8, 3.7, 5.8, 2.7, 6.4, 1.8, 9.5, 10.2]

        differences = []

        for x,y in zip(testArray1,testArray2):
            if x != y:
                differences.append(abs(x - y)) #Lägger in skillanderna i en egen array
            
        if not differences:
            print("De är lika")
        else:
            print(f"De är inte lika, Skillnader: {len(differences)}, Största skillanden: {max(differences):.1f} ") #max  blir det största talet i arrayen som också är den största skillanden mellan talen jämfört.
    
    def uppgift6(self):
        b = [0,12,13,14,13,0,0,15,15,0,13,0,0,15,34,2,3,4,5,6,1,2,3,4,5,6,0,0,0,0,0]

        # Går igenom varje element x(value) i listan b och lägger till det i new
        # endast om värdet inte är 0
        new = [x for x in b if x != 0] 
        
        print(f"Gamla arrayen {b}")
        print(f"Utan 0 {new}")

    def uppgift7(self):
        #ta det största av talen på varje position och lagra i en ny tredje array 
        array1 = [[1,2,3],[11,12,13],[6,3,23]]
        array2 = [[1,1,4],[1,2,3],[21,7,23]]
    
    #repitera senare
       

lab = lab10()
lab.uppgift7()