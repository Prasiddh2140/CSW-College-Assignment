def sum_and_average(*args):
    total_sum = sum(args) 
    average = total_sum / len(args)
    return total_sum, average

total, avg = sum_and_average(10, 20, 30)
print("Sum: ", total)
print("Average:", avg)
            