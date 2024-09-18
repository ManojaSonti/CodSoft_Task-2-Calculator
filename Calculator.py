# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Display the operation choices
def display_menu():
    print("\nSimple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

def main():
    while True:
        display_menu()

        # Take input from the user for the operation
        choice = input("Enter choice (1/2/3/4): ")

        # Check if the choice is valid
        if choice in ['1', '2', '3', '4']:
            try:
                # Input two numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                # Perform the chosen operation
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")

            except ValueError:
                print("Invalid input. Please enter numeric values.")

        else:
            print("Invalid choice. Please select a valid operation.")

        # Ask the user if they want to perform another calculation
        next_calculation = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if next_calculation != 'yes':
            print("Exiting the calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
