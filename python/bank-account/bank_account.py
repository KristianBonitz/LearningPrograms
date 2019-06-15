import threading

class BankAccount(object):
    def __init__(self):
        self.is_open = False
        self._balance = 0
        self._lock = threading.Lock()

    def get_balance(self):
        with self._lock:
            if self.is_open:
                return self._balance
            else:
                raise ValueError("Cannot get balance of closed account")

    def open(self):
        with self._lock:
            if self.is_open != False:
                raise ValueError("Cannot open account with status", self.is_open)

            self.is_open = True

    def deposit(self, amount):
        with self._lock:
            if self.is_open and amount > 0:
                self._balance += amount
            else:
                raise ValueError("Cannot deposit into account")

    def withdraw(self, amount):
        with self._lock:
            if self.is_open and amount <= self._balance and amount > 0:
                self._balance -= amount
            else:
                raise ValueError("Invalid operation")

    def close(self):
        with self._lock:
            if self.is_open:
                self.is_open = False
                self._balance = 0
            else:
                raise ValueError("Cannot close already closed account")        
