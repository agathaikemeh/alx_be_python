from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time in a readable format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date
    future_date = current_date + timedelta(days=days)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    # Display the current date and time
    display_current_datetime()

    # Prompt user for number of days
    days = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate and display the future date
    calculate_future_date(days)

if __name__ == "__main__":
    main()

