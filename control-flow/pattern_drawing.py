# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate input
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize row counter
    row = 0

    # Use a while loop for rows
    while row < size:
        # Use a for loop for columns
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1