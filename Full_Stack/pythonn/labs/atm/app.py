# app.py 6/25/18

from atm import ATM


def main():
    atm3 = ATM()  # create ATM object
    while True:
        # get command from user
        # noinspection SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection
        user_option = \
            input(
                "Choose an option: (D)eposit, (W)ithdraw, "
                "(C)heck Balance, (H)istory, (hit return if finished): ")

        if not user_option:  # check if the user is done using the atm
            print("Goodbye.")
            break
        if user_option.lower() in ['d', 'deposit']:  # deposit amount
            amount = input("How much would you like to deposit?: ")
            print(atm3.deposit(int(amount)))
        if user_option.lower() in ['w', 'withdraw']:  # withdraw amount
            amount = input("How much would you like to withdraw?: ")
            print(atm3.withdraw(int(amount)))
        if user_option.lower() in ['c', 'check balance']:  # show their balance
            print(atm3.check_balance())
        if user_option.lower() in ['h', 'history']:  # show transactions
            atm3.print_transactions()


main()
