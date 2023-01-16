import mysql.connector as my

def Connection():
    try:
        mydb=my.connect(
            host='localhost',
            user='root',
            password='',
            database='info')

        print('connection is created')

        return mydb

    except Exception as e1:

        print("ConnectionError",e1)
