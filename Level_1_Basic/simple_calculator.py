# Project: Simple Calculator
# Developer: Tilak Kumar
# Project Number: 1 (Level 1 Beginner)
# Features:
# - Separate Functions for every operation
# - User Input: Two numbers and operation choice
# - Error Handling: Specific check for division by zero
# - Looping: Runs until user types '5' to exit

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def format_result(value):
    """Formats result to remove unnecessary .0 from whole numbers"""
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

print("--- Codveda Level 1: Simple Calculator ---")

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {format_result(result)}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {format_result(result)}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {format_result(result)}")
            elif choice == '4':
                result = divide(num1, num2)
                # Check if result is a string (error message) or a number
                if isinstance(result, str):
                    print(f"Result: {num1} / {num2} = {result}")
                else:
                    print(f"Result: {num1} / {num2} = {format_result(result)}")

        except ValueError:
            print("Invalid input! Please enter numeric values only.")

    else:
        print("Invalid Input. Please choose between 1-5.")
