# project: name simple calculator
# developer: Tilak Kumar
#projectnumber:1 from level 1 beginner
# ======================features========================#
# Separate Functions: "separate function for every operation"
# User Input: "Two numbers and operation choice."
# Error Handling: "specific check for division by zero"
# Looping: "Runs until user types 'exit' or selects option 5"

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
        print("Exiting calculator.goodbye!;)")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")

        except ValueError:
            print("Invalid input! Please enter numeric values only.")

    else:
        print("Invalid Input. Please choose between 1-5.")
