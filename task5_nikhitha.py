n = int(input("Enter number of rows: "))

print("\n1. Right Triangle Pattern")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n2. Inverted Triangle Pattern")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n3. Pascal Triangle")

for i in range(n):
    num = 1
    for j in range(n - i):
        print(" ", end="")

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()

print("\n4. Prime Numbers")

for num in range(2, n + 1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")
