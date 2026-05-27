bill_amount = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))

tip_amount = (bill_amount * tip_percent) / 100
total_with_tip = bill_amount + tip_amount
amount_per_person = total_with_tip / people

tip_amount = round(tip_amount, 2)
total_with_tip = round(total_with_tip, 2)
amount_per_person = round(amount_per_person, 2)

print("\n===== BILL SUMMARY =====")
print(f"Original Bill      : ₹{bill_amount}")
print(f"Tip Amount         : ₹{tip_amount}")
print(f"Total With Tip     : ₹{total_with_tip}")
print(f"Amount Per Person  : ₹{amount_per_person}")
print("========================")