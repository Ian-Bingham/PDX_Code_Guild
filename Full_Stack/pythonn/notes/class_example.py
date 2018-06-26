# class_example.py 6/25/18

class BankAccount(object):
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amt):
        self.balance += amt
        return 'Thank you {}. Your balance is now ${}'.format(self.name, self.balance)

    def withdraw(self, amt):
        if self.balance - amt >= 0:
            self.balance -= amt
            return 'Thank you {}. Your balance is now ${}'.format(self.name, self.balance)
        return 'You do not have enough funds. Your balance is ${}.'.format(self.balance)

    def __str__(self):
        return "{} BankAccount".format(self.name)

class BankAccountPlus(BankAccount):
    def __init__(self, n):
        super().__init__(n)

    def withdraw(self, amt):
        if self.balance - amt - 100 >= 0:
            self.balance -= amt
            return 'Thank you {}. Your balance is now ${}'.format(self.name, self.balance)
        return 'You do not have enough funds. Remember you must keep at least $100 in your account. Your balance is ${}.'.format(self.balance)

chris = BankAccount('Chris')
print(chris.deposit(100))
print(chris.withdraw(95))
print(chris.withdraw(200))
kim = BankAccount('Kim')
