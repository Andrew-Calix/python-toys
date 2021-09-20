"""
My understanding of functions is still premature
I don't know why guess = 0 in the function
"""

import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry guess again. Too low.")
        elif guess > random_number:
            print("Sorry guess again. Too high")

    print("Yay, congrats. You have guessed the number.")


guess(100)

E: str = input("press ENTER to exit")
