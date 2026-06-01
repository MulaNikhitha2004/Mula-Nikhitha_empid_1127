expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        expenses.append(amount)
        print("Expense Added!")

    elif choice == "2":
        print("Expenses:", expenses)

    elif choice == "3":
        amount = float(input("Enter amount to delete: "))
        if amount in expenses:
            expenses.remove(amount)
            print("Expense Deleted!")
        else:
            print("Not Found!")

    elif choice == "4":
        print("Total Spending:", sum(expenses))

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")