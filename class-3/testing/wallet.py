class Wallet:

    def __init__(self, balance):
        self.balance = balance
        self.max_balance = 0

    def withdraw(self, amount):
        self.balance -= amount

    def add_founds(self, amount):
        if amount < 0:
            raise Exception("amount must be a positive number")
        self.balance += amount

    def is_empty(self):
        if self.balance == 0:
            return True
        return False

    def has_debt(self):
        pass
