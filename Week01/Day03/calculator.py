def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def show_menu():
    print("===== Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

operations = {
                '1' : ('+' , add),
                '2' : ('-' , subtract),
                '3' : ('*' , multiply),
                '4' : ('/' , divide)
            }

EXIT_OPTION = '5'

def calculate():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == EXIT_OPTION:
            print("Exiting the calculator. \nGoodBye!")
            break
        elif choice in ['1', '2', '3', '4']:
            try:
                 number1  = float(input("Enter first number:"))
                 number2 = float(input("Enter second number:"))
            except ValueError:
                print("Invalid input. Please enter numberic values.")
                continue

            symbol , operation = operations[choice]
            try: 
                result = operation(number1, number2)
                print(f"{number1} {symbol} {number2} = {result}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid choice. Please select between 1 and 5.")

calculate()