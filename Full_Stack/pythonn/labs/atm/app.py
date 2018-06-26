# app.py 6/25/18

from atm import ATM

# atm = ATM()
# print(atm.check_balance())
# print(atm.deposit(1000))
# print(atm.withdraw(500))
# print(atm.deposit(1))
# print(atm.withdraw(100))
# print(atm.calc_interest())
# atm.print_transactions()
#
# print('*' * 80)
#
# atm2 = ATM(5000, 0.065)
# print(atm2.check_balance())
# print(atm2.deposit(1000))
# print(atm2.withdraw(700))
# print(atm2.deposit(2000))
# print(atm2.withdraw(5000))
# print(atm2.withdraw(3000))
# print(atm2.calc_interest())
# atm2.print_transactions()

atm3 = ATM()
while True:
    user_option = input("Choose an option: (D)eposit, (W)ithdraw, (C)heck Balance, (H)istory, \
(hit return if finished): ")

    if not user_option:
        print("Goodbye.")
        break
    if user_option.lower() in ['d', 'deposit']:
        amount = input("How much would you like to deposit?: ")
        print(atm3.deposit(int(amount)))
    if user_option.lower() in ['w', 'withdraw']:
        amount = input("How much would you like to withdraw?: ")
        print(atm3.withdraw(int(amount)))
    if user_option.lower() in ['c', 'check balance']:
        print(atm3.check_balance())
    if user_option.lower() in ['h', 'history']:
        atm3.print_transactions()
