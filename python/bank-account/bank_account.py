class BankAccount(object):
    def __init__(self):
        self.is_open = None
        self._balance = 0

    def get_balance(self):
        return self._balance

    def open(self):
        if self.is_open != None:
            raise ValueError("Cannot open account with status", self.is_open)

        self.is_open = True

    def deposit(self, amount):
        if self.is_open:
            self._balance += amount
        else:
            raise ValueError("Cannot into account")

    def withdraw(self, amount):
        pass

    def close(self):
        pass
