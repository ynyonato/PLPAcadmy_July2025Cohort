# Basic Calculator Program

# Prompt the user to enter the first number (accepts decimals)
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number (accepts decimals)
num2 = float(input("Enter the second number: "))

# Ask the user to choose a mathematical operation (+, -, *, /)
operation = input("Enter an operation (+, -, *, /): ")

# Initialize a dictionary to map operation to descriptive text
operation_names = {
    '+': "addition",
    '-': "subtraction",
    '*': "multiplication",
    '/': "division"
}

# Perform the operation based on user input and display the result along with the chosen operation message
if operation in operation_names:
    print(f"You chose to make {operation_names[operation]}.")
    
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        # Check to avoid division by zero
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is undefined.")
else:
    # Handle invalid operation inputs
    print("Error: Invalid operation. Please enter one of +, -, *, /.")
