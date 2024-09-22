# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a variable to track rows
row = 0

# While loop to handle the rows
while row < size:
    # For loop to print asterisks (*) for each row
    for _ in range(size):
        print("*", end="")  # print asterisks side by side without a newline
    print()  # print a newline after the row is complete
    row += 1  # move to the next row
