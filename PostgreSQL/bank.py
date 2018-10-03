import psycopg2
from psycopg2 import Error


def create_table(connection, cursor):
    # create table if it does not exist
    cursor.execute("SELECT * FROM information_schema.tables WHERE table_name='bank_accounts'")
    if not bool(cursor.rowcount):
        create_table_query = """CREATE TABLE bank_accounts (
                                    id SERIAL PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    amount REAL) """
        cursor.execute(create_table_query)
        connection.commit()


def create_account(connection, cursor):
    while True:
        name = input("\nPlease type in your first and last name to access your account.\n: ")

        # create account if it does not exist
        cursor.execute("SELECT * FROM bank_accounts WHERE name=%s", (name,))
        account = cursor.fetchone()
        if not account:
            print("That account does not exist.")

            # ask if they want to create a new account with the name they provided
            # if yes, create a new account. if not, ask for another name
            while True:
                response = input("\nWould you like to create an account with that name?\n: ").lower()
                if response in ['yes', 'y']:
                    # create the account
                    cursor.execute("INSERT INTO bank_accounts (name, amount) VALUES (%s, %s)", (name, 0))
                    connection.commit()
                    create_acc = True
                    return name
                elif response in ['no', 'n']:
                    break
                else:
                    print("Invalid input")
        else:
            return name


# ask for an amount to deposit/withdraw
def ask_for_amount(action):
    while True:
        amount = input(f"\nHow much would you like to {action}?\n: $")
        if amount == '' or amount.find('-') == 0:
            print("Invalid input.")
            continue

        try:
            float(amount)
            break
        except ValueError:
            print("Invalid input.")

    return round(float(amount), 2)


def deposit(connection, cursor, name):
    # get the current amount
    cursor.execute("SELECT * FROM bank_accounts WHERE name=%s", (name,))
    amount = cursor.fetchone()[2]

    # add the deposit
    deposit = ask_for_amount('deposit')
    amount += deposit
    cursor.execute("UPDATE bank_accounts SET amount = %s WHERE name=%s", (amount, name,))
    connection.commit()
    print("Successfully desposited.")


def withdraw(connection, cursor, name):
    # get the current amount
    cursor.execute("SELECT * FROM bank_accounts WHERE name=%s", (name,))
    amount = cursor.fetchone()[2]

    # check if they have enough money to withdraw
    while True:
        withdraw = ask_for_amount('withdraw')
        if withdraw > amount:
            print('Not enough funds in your account.')
            continue
        else:
            break

    # subtract withdraw
    amount -= withdraw
    cursor.execute("UPDATE bank_accounts SET amount = %s WHERE name=%s", (amount, name,))
    connection.commit()
    print("Successfully withdrew.")


def main():
    try:
        connection = psycopg2.connect(  user = 'ian',
                                        password = '',
                                        host = 'localhost',
                                        port = 5432,
                                        database = 'bank')

        connection.autocommit = False
        cursor = connection.cursor()

        print("\nWelcome To The Bank!\n")
        create_table(connection, cursor)
        name = create_account(connection, cursor)

        while True:
            cursor.execute("SELECT * FROM bank_accounts WHERE name=%s", (name,))
            account = cursor.fetchone()
            print(f"\nHello {account[1]}. You currently have ${account[2]}.")

            action = input("\nWould you like to: (d)eposit, (w)ithdraw, or (q)uit?\n: ").lower()
            if action in ['d', 'deposit']:
                deposit(connection, cursor, name)
            elif action in ['w', 'withdraw']:
                withdraw(connection, cursor, name)
            elif action in ['q', 'quit']:
                print("Have a nice day!")
                exit(0)
            else:
                print("Invalid input.")

    except(Exception, psycopg2.DatabaseError) as error:
        print("Error: ", error)
        if(connection):
            connection.rollback()  # rollback all changes to the database since last commit

    finally:
        # closing database connection
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")


main()
