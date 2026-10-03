# Simple Calculator Program using if-elif statements

# Step 1: Get the operation choice from the user
operation = input("Enter operation (add/sub/mul/div/mod): ").strip().lower()

# Step 2: Input two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 3: Perform the operation based on user's choice using if-elif
if operation == "add":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operation == "sub":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operation == "mul":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operation == "div":
    # Safe check for division by zero
    if num2 == 0:
        print("Error: Division by zero not allowed.")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

elif operation == "mod":
    # Safe check for modulus by zero
    if num2 == 0:
        print("Error: Modulus by zero not allowed.")
    else:
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")

else:
    print("Invalid Operation! Please choose from add, sub, mul, div, or mod.")
