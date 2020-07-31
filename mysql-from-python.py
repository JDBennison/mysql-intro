import os
import datetime
import pymysql

#Get username from workspace

username = os.getenv('USER')

#Connect to the database
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        connection.commit()
        
finally:
    #close the connection, regardless of whether the above was successful
    connection.close()