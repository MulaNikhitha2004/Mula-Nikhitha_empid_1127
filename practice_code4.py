# Voting Eligibility Checker

def check_eligibility(age):
    if age >= 18:
        return "Eligible to Vote"
    else:
        return "Not Eligible to Vote"

age = int(input("Enter your age: "))

result = check_eligibility(age)

print(result)
