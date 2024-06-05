"""Account class definition"""
from decimal import Decimal

class Account:
    """Account class for maintaing a bank account balance"""
    def __init__ (self, name, balance):
        """Initialize an account object"""
        # if balance is < 0 raise error
        if balance < Decimal('0.00'):
            raise ValueError('initial balance must be >= to 0.00.')
        self.name  = name
        self.balance = balance

    def deposit(self,amount):
        """Deposit money to the account"""
        if amount < Decimal('0.00'):
            raise ValueError('ammount must be positive')
        
        self.balance += amount    

    def withdraw(self,amount):
        """withdraw money from the account"""
        if amount > self.balance:
            raise ValueError('amount must be <= to balance')
        elif amount < Decimal('0.00'):
            raise ValueError('amount must be positive')
        
        self.balance -= amount        