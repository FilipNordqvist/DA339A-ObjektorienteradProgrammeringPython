import random


def main():
    difficulty = user__difficulty()
    game(difficulty)


def user__difficulty():
    difficulty = int(input("What level do you want to play? "))
    return difficulty * 10


def game(difficulty):
    winning_number = random.randrange(0,difficulty)
    number_of_guesses = 0
    
    while True:
        try:
            guess = int(input(f"Try to guess a number between 0-{difficulty}: "))
        
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess < winning_number:
            print(f"You guessed to low, guess again {guess}")
            number_of_guesses += 1
        elif guess > winning_number:
            print(f"You guessed to high, guess again {guess}")
            number_of_guesses += 1
        else:
            print(f"It took you {number_of_guesses} moves to guess {winning_number}")
            break


if __name__ == "__main__":
    main()
