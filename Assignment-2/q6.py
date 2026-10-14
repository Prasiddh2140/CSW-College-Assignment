# Function to process dictionary
def process_data(data):
    result = {}
    for key in data:
        value = data[key]
        # If value is a list
        if type(value) == list:
            total = 0
            for num in value:
                # Check prime number
                count = 0
                for i in range(1, num + 1):
                    if num % i == 0:
                        count = count + 1
                if count == 2:
                    total = total + num
            result[key] = total
        # If value is a tuple
        elif type(value) == tuple:
            product = 1
            for num in value:
                # Check odd number
                if num % 2 != 0:
                    product = product * num
            result[key] = product
    return result
# Input dictionary
data = {
    "A": [2, 3, 4, 5, 10],
    "B": (1, 2, 3, 4, 5),
    "C": [7, 8, 9],
    "D": (6, 7, 8)
}
# Calling function
new_dictionary = process_data(data)
print("New Dictionary:")
print(new_dictionary)