# Fibonacci Series

n = int(input("Enter the number of terms: "))

a = 0
b = 1

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci Series:")
    print(a)
else:
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
