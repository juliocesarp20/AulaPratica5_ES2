class BudgetException(Exception):
    pass


class Deposit:
    def __init__(self, initial_budget=0):
        self.budget = initial_budget

    def deposit(self, amount):
        if amount <= 0:
            raise BudgetException("Invalid deposit amount."
                                  " Amount must be greater than zero.")
        self.budget += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise BudgetException("Invalid withdrawal amount. "
                                  "Amount must be greater than zero.")
        if amount > self.budget:
            raise BudgetException("Insufficient funds. "
                                  "Cannot withdraw more than available budget.")
        self.budget -= amount
