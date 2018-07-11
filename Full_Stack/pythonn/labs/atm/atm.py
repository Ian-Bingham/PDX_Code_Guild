# atm.py 6/25/18

class ATM(object):
    def __init__(self, balance=0, interest_rate=0.001):
        self.transaction_list = []
        self.balance = balance
        self.interest_rate = interest_rate

    # return the balance
    def check_balance(self):
        return 'Your balance is ${}.'.format(self.balance)

    # add the deposited amount to the balance
    # update transaction history
    def deposit(self, amount):
        self.balance += amount
        self.transaction_list.append('User deposited ${}'.format(amount))
        return 'Deposit complete.'

    # return True if they have enough funds to perform the withdrawal
    def check_withdrawal(self, amount):
        if self.balance - amount >= 0:
            return True
        return False

    # if they have enough funds, subtract the amount from their balance
    # if not, print an error message
    # update transaction history
    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.balance -= amount
            self.transaction_list.append('User withdrew ${}'.format(amount))
            return 'Withdrawal complete.'
        return 'Not enough funds to withdraw ${} from your account.'.format(amount)

    # calculate their interest
    def calc_interest(self):
        return 'Your interest is ${}'.format(self.balance * self.interest_rate)

    # print the list of transactions
    def print_transactions(self):
        print('----- Transaction History -----')
        for i in self.transaction_list:
            print(i)
