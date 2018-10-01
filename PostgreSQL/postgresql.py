import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = 'ian',
                                password = '',
                                host = 'localhost',
                                port = '5432',
                                database = 'test_db')

    cursor = connection.cursor()

    create_table_query = """CREATE TABLE groceries
                            (id INT PRIMARY KEY NOT NULL,
                            name TEXT NOT NULL,
                            price REAL);"""

    insert_apple_query = """INSERT INTO groceries (id, name, price) VALUES
                            (1, 'apple', 0.68)"""

    insert_banana_query = """INSERT INTO groceries (id, name, price) VALUES
                            (2, 'banana', 0.49)"""

    insert_chicken_query = """INSERT INTO groceries (id, name, price) VALUES
                            (3, 'chicken', 0.98)"""

    multiple_items_list = [ (4, 'almonds', 4.37),
                            (5, 'cheese', 1.88),
                            (6, 'broccoli', 0.77) ]
    insert_multiple_query = """INSERT INTO groceries (id, name, price) VALUES
                            (%s, %s, %s) """

    cursor.execute(create_table_query)
    cursor.execute(insert_apple_query)
    cursor.execute(insert_banana_query)
    cursor.execute(insert_chicken_query)
    cursor.executemany(insert_multiple_query, multiple_items_list)
    connection.commit()  # save changes to the database
    print('Inserted multiple items')

except(Exception, psycopg2.DatabaseError) as error:
    if(connection):
        connection.rollback()  # rollback all changes to the database since last commit
    print(f"Failed inserting values: {error}")

finally:
    # closing database connection
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
