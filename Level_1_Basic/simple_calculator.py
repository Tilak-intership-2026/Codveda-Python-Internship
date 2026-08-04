# Project: Simple Calculator
# Developer: Tilak Kumar
# Project Number: 1 (Level 1 Beginner)

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

def smart_format(value, original_input_str):
    """
    Checks if the original input had a decimal point.
    If yes, returns float. If no, returns int (if whole number).
    """
    if '.' in original_input_str:
        return f"{value:.2f}" # Shows 2 decimal places for floats
    else:
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
            # We take input as string first to check for '.'
            str_num1 = input("Enter first number: ")
            str_num2 = input("Enter second number: ")
            
            num1 = float(str_num1)
            num2 = float(str_num2)

            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {smart_format(num1, str_num1)} + {smart_format(num2, str_num2)} = {smart_format(result, str_num1)}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {smart_format(num1, str_num1)} - {smart_format(num2, str_num2)} = {smart_format(result, str_num1)}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {smart_format(num1, str_num1)} * {smart_format(num2, str_num2)} = {smart_format(result, str_num1)}")
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(f"Result: {smart_format(num1, str_num1)} / {smart_format(num2, str_num2)} = {result}")
                else:
                    print(f"Result: {smart_format(num1, str_num1)} / {smart_format(num2, str_num2)} = {smart_format(result, str_num1)}")

        except ValueError:
            print("Invalid input! Please enter numeric values only.")

    else:
        print("Invalid Input. Please choose between 1-5.")
