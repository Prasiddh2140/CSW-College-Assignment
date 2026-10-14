# Function to find student with highest average score
def highest_average(students):
    highest = 0
    top_student = ""
    for name in students:
        total = 0
        # Calculate total marks
        for marks in students[name]:
            total = total + marks
        # Calculate average
        average = total / len(students[name])
        print(name, "Average =", average)
        # Check highest average
        if average > highest:
            highest = average
            top_student = name
    return top_student
# Student dictionary
students_scores = {
    "Ram": [85, 90, 92],
    "Laxman": [70, 80, 88],
    "Janaki": [95, 100, 90]
}
# Calling function
result = highest_average(students_scores)
print("\nStudent with highest average score is:", result)