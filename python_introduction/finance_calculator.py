# Prompt for user input
monthly_income = float(input("Enter your monthly income: "))
total_expenses = float(input("Enter your total monthly expenses: "))
# Calculate monthly savings
monthly_savings = monthly_income - total_expenses
# Define annual interest rate
annual_interest_rate = 0.05

# Calculate projected annual savings
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)
# Print results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
