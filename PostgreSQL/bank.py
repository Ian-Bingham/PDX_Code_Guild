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


def create_account(connection, cursor, name):
    cursor.execute("INSERT INTO bank_accounts (id, name, amount) VALUES (,name,)")
    connection.commit()


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

        create_acc = False
        while not create_acc:
            name = input("Please type in your first and last name to access your account.\n: ")
            cursor.execute("SELECT * FROM bank_accounts WHERE name=%s", (name,))
            account = cursor.fetchone()
            if not account:
                print("That account does not exist.")

                while True:
                    response = input("Would you like to create an account with that name?\n: ").lower()
                    if response in ['yes', 'y']:
                        # create the account
                        cursor.execute("INSERT INTO bank_accounts (name) VALUES (%s)", (name,))
                        connection.commit()
                        create_acc = True

                        # get the account
                        cursor.execute("SELECT * FROM bank_accounts WHERE name=%s", (name,))
                        account = cursor.fetchone()
                        print("Account successfully created")
                        break
                    elif response in ['no', 'n']:
                        break
                    else:
                        print("That was not a valid option. Try again.")
            else:
                create_acc = True


        print(account)








    except(Exception, psycopg2.DatabaseError) as error:
        print("Error ", error)
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
