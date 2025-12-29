class lab6:
    def uppgift1a():
        a = [1,2,3,4,5,6,7,8,9,10]

        for x in a:
            print(x, end=" ")
        print()

        for x in a[::-1]:
            print(x, end=" ")
        print()

        for x in a[1::2]:
            print(x, end=" ")
        print()

        for x in a[8::-2]:
            print(x, end=" ")
        print()

        for x in range(10,110,10):
            print(x, end=" ")
        print()

    def uppgift1b():
        a = [1,2,3,4,5,6,7,8,9,10]
        i = 0 
        
        while i < len(a):
            print(a[i], end=" ")
            i += 1

        print()
        
        while i > 0:
            print(a[i-1], end=" ")
            i -= 1

        print()

        i = 1

        while i < len(a):
            print(a[i], end=" ")
            i += 2

        print()

        i = len(a) - 1

        while i > 0:
            print(a[i-1], end=" ")
            i -= 2
        
        print()

        i = 0

        while i <= 100:
            print(i, end=" ")
            i += 10
        
        print()

    def uppgift2():
        min = 10
        max = 25
        increase = 3

        for i in range(min,max + 1,increase):
            print(i, end=" ")
        print()

        while min <= max:
            print(min, end=" ")
            min += increase
            
        print()
    
    def uppgift3():
        i = 1

        number = int(input("Vilket nummers multipliaktionstabell vill du ha? "))

        for i in range(1,11):
            print(i*number, end=" ")
        
        print()

    def uppgift4():
        #a
        for i in range(1,10):
            print("*"*i)

        print()

        #b
        for i in reversed(range(1,10)):
            print("*"*i)

        print()

        #c
        for i in range(1,5):
            print("*"*i)
        
        for i in reversed(range(1,5)):
            print("*"*i)

    #d Julgrannen
            
    uppgift4()

