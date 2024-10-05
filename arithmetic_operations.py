def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations based on the given operation.
    
    Parameters:
    - num1 (float): First number.
    - num2 (float): Second number.
    - operation (str): The operation to perform (add, subtract, multiply, divide).
    
    Returns:
    - Result of the operation or an error message for invalid operations or division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation"

