print("===== EMI Calculator =====")

principal = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate: "))
time = int(input("Enter loan tenure in months: "))

monthly_rate = rate / (12 * 100)

emi = (principal * monthly_rate * (1 + monthly_rate) ** time) / ((1 + monthly_rate) ** time - 1)

print("\n===== EMI DETAILS =====")
print("Loan Amount :", principal)
print("Interest Rate :", rate, "%")
print("Loan Tenure :", time, "months")
print("Monthly EMI :", round(emi, 2))
print("========================")
