"""Module contains a solution to the task: eight."""


class Bank:
    """Class Bank."""
    def __init__(self, amount):
        """Function initialize."""
        self.amount = amount

    def deposit(self, money):
        """Function deposit."""
        self.amount += money
        return self.amount

    def withdraw_money(self, money):
        """Function withdraw money."""
        if self.amount - money < 0:
            print(f'Insufficient sum, available amount is {self.amount}')
            return False
        self.amount -= money
        return self.amount

    def check_balance(self):
        """Function check balance."""
        print(f'current balance is {self.amount}')
        return self.amount


user = Bank(amount=1000)
assert user.check_balance() == 1000
assert user.deposit(1111) == 2111
assert user.withdraw_money(1111) == 1000
assert user.withdraw_money(1000000) is False
