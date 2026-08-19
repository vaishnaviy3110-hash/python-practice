# Simple ATM

balance = 10000

print("===== Welcome to Simple ATM =====")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Your current balance is ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))

        if amount > 0:
            balance = balance + amount
            print(f"₹{amount} deposited successfully.")
            print(f"Your new balance is ₹{balance}")
        else:
            print("Please enter a valid amount.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Please enter a valid amount.")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance = balance - amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Your remaining balance is ₹{balance}")

    elif choice == "4":
        print("Thank you for using Simple ATM!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
