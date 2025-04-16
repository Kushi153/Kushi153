# number_guess_game.py
import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    name = "Ravi Teja"
    print(f"Hello, {name}! Let's play.")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low, try again.")
            elif guess > number_to_guess:
                print("Too high, try again.")
            else:
                print(f"Congratulations {name}! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
