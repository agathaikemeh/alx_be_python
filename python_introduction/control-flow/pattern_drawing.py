# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a variable to track the rows
row = 0

# Use a while loop to iterate through the rows
while row < size:
    # Use a for loop to print asterisks for each row
    for col in range(size):
        print("*", end="")  # Print asterisk without moving to the next line
    print()  # Move to the next line after printing the row
    row += 1  # Increment the row counter
