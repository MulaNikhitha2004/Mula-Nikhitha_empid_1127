# Fibonacci Series Generator

n = int(input("Enter number of terms: "))

a = 0
b = 1

print("\nFibonacci Series")

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c