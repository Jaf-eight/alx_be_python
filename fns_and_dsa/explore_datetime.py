
# explore_datetime.py
from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format as YYYY-MM-DD HH:MM:SS
    print(f"Current date and time: {formatted_date}")
    return formatted_date  # Return formatted date for checks

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)  # Add days
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format as YYYY-MM-DD
        print(f"Future date: {formatted_future_date}")
        return formatted_future_date
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Run the functions
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
