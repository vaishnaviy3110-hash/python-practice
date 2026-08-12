import random
secret_num=random.randint(1,100)
attempts=7
print("welcome to the guessing game!")
print(f"you have {attempts} attempts to guess the secret num between 1-100.")
print("good luck!")
for i in range(1,attempts+1):
    guess=int(input(f"attempt {i} of {attempts}:"))
    if guess < secret_num:
        print("Try again!, Your guess is too low.")
    elif guess > secret_num:
        print("Try again!, Your guess is too high.")
    else:
        print(f"Congratulations! You guessed the secret number {secret_num} correctly in {i} attempts.")
        break
else:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_num}.")            
