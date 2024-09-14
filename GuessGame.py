import random


def generate_number(difficulty):
    difficulty = int(difficulty)
    return random.randint(1, difficulty)

def get_guess_from_user():
    return int(input("Input your guess: "))

def compare_results(guess,secret_number):
    if guess == secret_number:
        print("Correct!")
        return True
    else:
        print("Wrong!")
        return False

def play(difficulty):
    secretNumber = generate_number(difficulty)
    guess = get_guess_from_user()
    return compare_results(guess,secretNumber)