total_target = 100
total_produced = 0
defective_items = 0

print("===== Production Counter System =====")

for shift in range(1, 4):

    print(f"\nShift {shift}")

    for cycle in range(1, 21):

        item = int(input(f"Enter items produced in cycle {cycle}: "))

        if item < 0:
            print("Defective item detected")
            defective_items += 1
            continue

        total_produced += item

        if total_produced >= total_target:
            print("\nProduction target reached!")
            break

    if total_produced >= total_target:
        break

worker_efficiency = (total_produced / total_target) * 100

print("\n===== Production Report =====")
print("Total Produced :", total_produced)
print("Defective Items :", defective_items)
print("Worker Efficiency :", round(worker_efficiency, 2), "%")
print("================================")