from Person import Person


def main():
    person = Person("Kalle",12)
    
    print(person.name)
    person.name = "Filip"
    print(person.name)
    
if __name__ == "__main__":
    main()
    