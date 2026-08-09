# Number Guessing Game

import random

secret_number = random.randint(1, 100)

print("===== Number Guessing Game =====")
print("I have chosen a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print(f"Congratulations! You guessed the number {secret_number}.")
        break
