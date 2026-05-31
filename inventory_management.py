inventory = {}

while True:
    print("\n===== INVENTORY MENU =====")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Delete Product")
    print("6. Inventory Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Product
    if choice == "1":
        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))

        inventory[pid] = {
            "name": name,
            "category": category,
            "quantity": quantity,
            "price": price
        }

        print("Product Added Successfully")

    # Display Products
    elif choice == "2":
        if len(inventory) == 0:
            print("No Products Available")
        else:
            print("\n--- Product List ---")
            for pid, details in inventory.items():
                print(pid, details)

    # Search Product
    elif choice == "3":
        search_name = input("Enter Product Name: ")

        found = False
        for pid, details in inventory.items():
            if details["name"].lower() == search_name.lower():
                print("\nProduct Found")
                print(pid, details)
                found = True

        if not found:
            print("Product Not Found")

    # Update Quantity
    elif choice == "4":
        pid = input("Enter Product ID: ")

        if pid in inventory:
            new_qty = int(input("Enter New Quantity: "))
            inventory[pid]["quantity"] = new_qty
            print("Quantity Updated Successfully")
        else:
            print("Product ID Not Found")

    # Delete Product
    elif choice == "5":
        pid = input("Enter Product ID: ")

        if pid in inventory:
            del inventory[pid]
            print("Product Deleted Successfully")
        else:
            print("Product ID Not Found")

    # Inventory Report
    elif choice == "6":
        total_products = len(inventory)

        total_value = 0
        categories = set()

        for details in inventory.values():
            total_value += details["quantity"] * details["price"]
            categories.add(details["category"])

        print("\n===== INVENTORY REPORT =====")
        print("Total Products :", total_products)
        print("Total Value :", total_value)
        print("Categories :", categories)

    # Exit
    elif choice == "7":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")