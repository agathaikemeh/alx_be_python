# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Try to perform division
        if denom == 0:
            return "Error: Cannot divide by zero."
        else:
            return f"The result of the division is {num / denom}"
    except ValueError:
        return "Error: Please enter numeric values only."
