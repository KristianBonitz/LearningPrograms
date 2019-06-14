import threading

class BankAccount(object):
    def __init__(self):
        self.is_open = False
        self._balance = 0
        self.lock = threading.Lock()

    def get_balance(self):
        self.lock.acquire()
        if self.is_open:
            return self._balance
        else:
            raise ValueError("Cannot get balance of closed account")
        self.lock.release()

    def open(self):
        self.lock.acquire()
        if self.is_open != False:
            raise ValueError("Cannot open account with status", self.is_open)

        self.is_open = True
        self.lock.release()

    def deposit(self, amount):
        self.lock.acquire()
        if self.is_open and amount > 0:
            self._balance += amount
        else:
            raise ValueError("Cannot deposit into account")
        self.lock.release()

    def withdraw(self, amount):
        self.lock.acquire()
        if self.is_open and amount <= self._balance and amount > 0:
            self._balance -= amount
        else:
            raise ValueError("Invalid operation")
        self.lock.release()

    def close(self):
        self.lock.acquire()
        if self.is_open:
            self.is_open = False
            self._balance = 0
        else:
            raise ValueError("Cannot close already closed account")
        self.lock.release()
        
