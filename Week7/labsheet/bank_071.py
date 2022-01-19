class BankAccount(object):

    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
        else:
            print('Insufficient funds available')

    def print_details(self):
        print('Your current balance is: {:.2f} euro'.format(self.balance))
