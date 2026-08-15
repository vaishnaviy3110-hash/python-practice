import random
choices=["rock","paper","scissors"]
print("--Welcome to the Rock, Paper, Scissors game!--")
user_choice=input("Enter your choice {rock,paper,scissors}:").lower()
if user_choice not in choices:
    print("Invalid choice! Please choice from the given choices/options only!")
else:
    computerChoice=random.choice(choices)
    print(f"Computer chose: {computerChoice}")
    print(f"You chose:{user_choice}")
    if user_choice==computerChoice:
         print("It's a tie!")
    elif ((user_choice=="rock" and computerChoice=="scissors") or
         (user_choice=="paper" and computerChoice=="rock") or 
         (user_choice=="scissors" and computerChoice=="paper")):
        print("You win!")
    else:
        print("Computer wins!")
