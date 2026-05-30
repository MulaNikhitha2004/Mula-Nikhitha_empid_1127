print("===== Attendance Calculator =====")

total_classes = int(input("Enter total classes held: "))
attended_classes = int(input("Enter attended classes: "))

attendance = (attended_classes / total_classes) * 100

print("\nAttendance Percentage :", round(attendance, 2), "%")

if attendance >= 75:
    print("Eligible for exams")

else:
    required = int((0.75 * total_classes) - attended_classes)

    print("Not eligible for exams")
    print("Attend at least", required, "more classes")