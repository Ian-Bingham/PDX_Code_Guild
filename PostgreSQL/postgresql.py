import psycopg2
from psycopg2 import Error
try:
   connection = psycopg2.connect(user="postgres",
                                  password="",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="sample_db")
   postgres_insert_query_one = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1,'IPhone X','900')"""
   postgres_insert_query_two = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (2,'Google Pixel','700')"""
   cursor = connection.cursor()
   cursor.execute(postgres_insert_query_one)
   cursor.execute(postgres_insert_query_two)
   connection.commit()
   print ("Records inserted successfully into mobile")
except (Exception, psycopg2.DatabaseError) as error :
    if(connection):
        connection.rollback()
    print("Failed inserting record into mobile table {}".format(error))
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")