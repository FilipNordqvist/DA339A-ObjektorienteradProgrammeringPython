import random


def main():
    difficulty = user__difficulty()
    game(difficulty)


def user__difficulty():
    difficulty = int(input("What level do you want to play? "))
    return difficulty * 10


def game(difficulty):
    print(f"Skriver ut i game --> {difficulty}")


if __name__ == "__main__":
    main()
