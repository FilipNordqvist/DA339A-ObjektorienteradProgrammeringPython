class LocalVariable():
    def example(self):
        number = 100000
        real = 13.25
        bigNr = 37222654987

        print(f"int: {number}, type: {type(number)}")
        print(f"double: {real}, type: {type(real)}")
        print(f"long: {bigNr}, type: {type(bigNr)}")

numbers = LocalVariable()
numbers.example() 
