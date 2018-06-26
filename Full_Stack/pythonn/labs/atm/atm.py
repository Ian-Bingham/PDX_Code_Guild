# atm.py 6/25/18

class ATM(object):
    def __init__(self, balance=0, interest_rate=0.001):
        self.transaction_list = []
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        return 'Your balance is ${}.'.format(self.balance)

    def deposit(self, amount):
        self.balance += amount
        self.transaction_list.append('User deposited ${}'.format(amount))
        return 'Deposit complete.'

    def check_withdrawal(self, amount):
        if self.balance - amount >= 0:
            return True
        return False

    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.balance -= amount
            self.transaction_list.append('User withdrew ${}'.format(amount))
            return 'Withdrawal complete.'
        return 'Not enough funds to withdraw ${} from your account.'.format(amount)

    def calc_interest(self):
        return 'Your interest is ${}'.format(self.balance * self.interest_rate)

    def print_transactions(self):
        print('----- Transaction History -----')
        for i in self.transaction_list:
            print(i)
