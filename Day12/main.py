import random
import art

EASY = 10
HARD = 5
MIN_NUMBER = 1
MAX_NUMBER = 100

def instruction():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {random.randint(MIN_NUMBER, MAX_NUMBER)}")

def set_difficulty():
    level = input("Choose a difficult. Type 'easy' or 'hard': ").lower()
    return EASY if level == 'easy' else HARD

def check_answer(guess, secret_number, number_guess):
    if guess == secret_number:
        print(f"You got it! The answer was {secret_number}.")
    elif guess < secret_number:
        number_guess -= 1
        print("Too low.")
    elif guess > secret_number:
        number_guess -= 1
        print("Too high.")
    return number_guess

def start():
    instruction()    
    number_guess = set_difficulty()
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    guess = 0

    while guess != secret_number:
        print(f"You have {number_guess} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        number_guess = check_answer(guess, secret_number, number_guess)
        
        if number_guess == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer was {secret_number}.")
            return
        if guess != secret_number:
            print("Guess again.")

def main():
    start()

if __name__ == "__main__":
    main()