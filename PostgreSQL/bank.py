import psycopg2
from psycopg2 import Error


def create_table(connection, cursor):
    # check to see if the bank_accounts table already exists
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
        name = input("Please type in your first and last name to access your account.\n: ")

        # check if the account exists. if not, create a new account
        cursor.execute("SELECT * FROM bank_accounts WHERE name=%s", (name,))
        account = cursor.fetchone()
        if not account:
            print("That account does not exist.")

            # ask if they want to create a new account with the name they provided
            # if yes, create a new account. if not, ask for another name
            while True:
                response = input("Would you like to create an account with that name?\n: ").lower()
                if response in ['yes', 'y']:
                    # create the account
                    cursor.execute("INSERT INTO bank_accounts (name, amount) VALUES (%s, %s)", (name, 0))
                    connection.commit()
                    create_acc = True
                    return name
                elif response in ['no', 'n']:
                    break
                else:
                    print("That was not a valid option. Try again.")
        else:
            return name


def deposit(connection, cursor, name):
    cursor.execute("SELECT * FROM bank_accounts WHERE name=%s", (name,))
    amount = cursor.fetchone()[2]
    while True:
        deposit = input("How much would you like to deposit?\n: $")
        if deposit[0] == '-':
            print("Cannot input negative number. Try again.")
            continue
            
        try:
            float(deposit)
            break
        except ValueError:
            print("That was not a valid number. Try again.")

    amount += round(float(deposit), 2)
    cursor.execute("UPDATE bank_accounts SET amount = %s WHERE name=%s", (amount, name,))
    connection.commit()
    print("Successfully desposited.")


def withdraw(connection, cursor, name):
    cursor.execute("SELECT * FROM bank_accounts WHERE name=%s", (name,))
    amount = cursor.fetchone()[2]
    pass


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
            print(f"Hello {account[1]}. You currently have ${account[2]}.")

            action = input("Would you like to: (d)eposit, (w)ithdraw, or (q)uit?\n: ").lower()
            if action in ['d', 'deposit']:
                deposit(connection, cursor, name)
            elif action in ['w', 'withdraw']:
                withdraw(connection, cursor, name)
            elif action in ['q', 'quit']:
                print("Have a nice day!")
                exit(0)
            else:
                print("That was not a valid option. Try again.")




    except(Exception, psycopg2.DatabaseError) as error:
        print("Error: ", error)
        # if(connection):
        #     connection.rollback()  # rollback all changes to the database since last commit
        # print(f"Failed inserting values: {error}")

    finally:
        # closing database connection
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")


main()
