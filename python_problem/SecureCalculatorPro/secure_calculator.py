import logging
from datetime import datetime
from collections import Counter

# Configure Logging
logging.basicConfig(
    filename='error_log.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Custom Exceptions
class InvalidNumberError(Exception):
    pass

class DivisionByZeroError(Exception):
    pass


# Calculator Class
class SecureCalculator:

    def __init__(self):
        self.history_file = "calculation_history.txt"

    def validate_number(self, value):
        try:
            return float(value)
        except ValueError:
            raise InvalidNumberError("Only numeric values are allowed.")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero.")
        return a / b

    def save_history(self, expression):
        with open(self.history_file, "a") as file:
            file.write(expression + "\n")

    def view_history(self):
        try:
            with open(self.history_file, "r") as file:
                data = file.read()

                if data.strip():
                    print("\n===== Calculation History =====")
                    print(data)
                else:
                    print("\nNo calculations found.")

        except FileNotFoundError:
            print("\nHistory file not found.")

    def view_errors(self):
        try:
            with open("error_log.log", "r") as file:
                data = file.read()

                if data.strip():
                    print("\n===== Error Report =====")
                    print(data)
                else:
                    print("\nNo errors logged.")

        except FileNotFoundError:
            print("\nNo error log file found.")

    def analytics_report(self):

        total_calculations = 0
        total_errors = 0
        error_types = []

        # Count Calculations
        try:
            with open(self.history_file, "r") as file:
                total_calculations = len(file.readlines())
        except FileNotFoundError:
            pass

        # Count Errors
        try:
            with open("error_log.log", "r") as file:
                lines = file.readlines()

                total_errors = len(lines)

                for line in lines:
                    if "InvalidNumberError" in line:
                        error_types.append("InvalidNumberError")
                    elif "DivisionByZeroError" in line:
                        error_types.append("DivisionByZeroError")
                    else:
                        error_types.append("OtherError")

        except FileNotFoundError:
            pass

        print("\n===== Analytics Report =====")
        print("Total Calculations :", total_calculations)
        print("Total Errors       :", total_errors)

        if error_types:
            common_error = Counter(error_types).most_common(1)[0][0]
            print("Most Common Error  :", common_error)
        else:
            print("Most Common Error  : No Errors")


# Menu Driven Program
def main():

    calculator = SecureCalculator()

    while True:

        print("\n===== Secure Calculator Pro =====")
        print("1. Perform Calculation")
        print("2. View Calculation History")
        print("3. View Error Report")
        print("4. Analytics Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            try:

                num1 = calculator.validate_number(
                    input("Enter First Number: ")
                )

                num2 = calculator.validate_number(
                    input("Enter Second Number: ")
                )

                print("\nOperations")
                print("+  Addition")
                print("-  Subtraction")
                print("*  Multiplication")
                print("/  Division")

                operator = input("Choose Operator: ")

                if operator == "+":
                    result = calculator.add(num1, num2)

                elif operator == "-":
                    result = calculator.subtract(num1, num2)

                elif operator == "*":
                    result = calculator.multiply(num1, num2)

                elif operator == "/":
                    result = calculator.divide(num1, num2)

                else:
                    raise Exception("Invalid Operator")

            except InvalidNumberError as e:
                print("Error:", e)
                logging.error(
                    f"InvalidNumberError: {e}"
                )

            except DivisionByZeroError as e:
                print("Error:", e)
                logging.error(
                    f"DivisionByZeroError: {e}"
                )

            except Exception as e:
                print("Error:", e)
                logging.error(
                    f"OtherError: {e}"
                )

            else:
                print("Result =", result)

                expression = (
                    f"{num1} {operator} {num2} = {result}"
                )

                calculator.save_history(expression)

            finally:
                print("Operation Completed.")

        elif choice == "2":
            calculator.view_history()

        elif choice == "3":
            calculator.view_errors()

        elif choice == "4":
            calculator.analytics_report()

        elif choice == "5":
            print("Thank You for Using Secure Calculator Pro")
            break

        else:
            print("Invalid Menu Choice")


if __name__ == "__main__":
    main()