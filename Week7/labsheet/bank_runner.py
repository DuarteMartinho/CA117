from bank_071 import BankAccount

def main():
    b1 = BankAccount()
    b1.print_details()
    b1.withdraw(1)
    b1.deposit(100)
    b1.deposit(150)
    b1.print_details()
    b1.withdraw(50)
    b1.print_details()
    b1.deposit(20)
    b1.withdraw(100)
    b1.print_details()

    b2 = BankAccount(1000)
    b2.deposit(1)
    b2.withdraw(2000)
    b2.print_details()
    b2.withdraw(1001)
    b2.print_details()

if __name__ == '__main__':
    main()