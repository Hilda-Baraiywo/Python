print("=== Basic Calculator ===")
print("Welcome to the Python Calculator!")


# Input first number
num1 = float(input("Enter the first number: "))
    
# Input second number
num2 = float(input("Enter the second number: "))
    
# Input operation
print("\nAvailable operations:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
    
operation = input("\nEnter the operation (+, -, *, /): ").strip()
    
# Perform calculation based on operation
if operation == '+':
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"\n{num1} / {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed!")
else:
    print(f"\nError: '{operation}' is not a valid operation!")
    print("Please use +, -, *, or /")

