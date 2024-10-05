# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Encapsulated account balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:  # Ensure the deposit amount is positive
            self.__account_balance += amount

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if sufficient funds exist."""
        if 0 < amount <= self.__account_balance:  # Check if enough funds are available
            self.__account_balance -= amount
            return True
        return False  # Not enough funds

    def display_balance(self):
        """Print the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")  # Format to 2 decimal places
