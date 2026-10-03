# 1. Create a dictionary mapping months to days
month_days = {
    "January": 31, "February": 28, "March": 31, "April": 30,
    "May": 31, "June": 30, "July": 31, "August": 31,
    "September": 30, "October": 31, "November": 30, "December": 31
}

# 2. Get the month from the user (and fix spelling/casing automatically)
month = input("Enter the name of a month: ").strip().capitalize()

# 3. Check if the month exists in our dictionary
if month not in month_days:
    print("Error: Invalid month name entered!")
else:
    # 4. If February, ask for the year and calculate leap year days
    if month == "February":
        year = int(input("Enter a year: "))
        
        # Leap year logic: divisible by 4 and not 100, OR divisible by 400
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days = 29
        else:
            days = 28
            
        print(f"{month} {year} has {days} days.")
    else:
        # 5. For all other months, look up the days directly
        days = month_days[month]
        print(f"{month} has {days} days.")

