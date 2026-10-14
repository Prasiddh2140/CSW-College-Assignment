# List of numbers to classify
numbers = [2, 4, 8, 9, 27, 28]

# Create a dictionary with empty lists for each category
classified = {
    "Prime": [],
    "Composite": [],
    "Perfect Squares": [],
    "Perfect Cubes": [],
}

# Check each number in the list
for num in numbers:

    # 1. Check if Prime or Composite
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            classified["Prime"].append(num)
        else:
            classified["Composite"].append(num)

    # 2. Check if Perfect Square
    # Check if any integer multiplied by itself equals num
    for i in range(num + 1):
        if i * i == num:
            classified["Perfect Squares"].append(num)
            break
        elif i * i > num:
            break

    # 3. Check if Perfect Cube
    # Check if any integer cubed equals num
    for i in range(num + 1):
        if i * i * i == num:
            classified["Perfect Cubes"].append(num)
            break
        elif i * i * i > num:
            break

# Display the output
print("Input =", numbers)
print("Output = {")
for category, values in classified.items():
    print(f'  "{category}": {values},')
print("}")