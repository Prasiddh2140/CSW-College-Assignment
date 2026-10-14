# List of student scores
scores = [78, 92, 45, 88, 63, 54, 99, 81, 70]
print("Original scores:", scores)

# --------------------------------------------------
# i. Find and display the average score
# --------------------------------------------------
total = sum(scores)
count = len(scores)
average = total / count
print("Average score:", round(average, 2))

# --------------------------------------------------
# ii. Determine the minimum and maximum scores
# --------------------------------------------------
lowest_score = min(scores)
highest_score = max(scores)
print("Minimum score:", lowest_score)
print("Maximum score:", highest_score)

# --------------------------------------------------
# iii. Display all scores above the average
# --------------------------------------------------
above_average = []
for s in scores:
    if s > average:
        above_average.append(s)

print("Scores above average:", above_average)

# --------------------------------------------------
# iv. Sort the list in descending order (highest to lowest)
# --------------------------------------------------
scores.sort(reverse=True)
print("Scores in descending order:", scores)

# --------------------------------------------------
# v. Replace the three lowest scores with 0
# --------------------------------------------------
# Because the list is sorted highest to lowest,
# the three lowest numbers are at the very end of the list.
scores[-1] = 0
scores[-2] = 0
scores[-3] = 0

print("Final scores with 3 lowest set to 0:", scores)