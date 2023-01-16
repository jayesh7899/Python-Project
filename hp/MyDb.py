import mysql.connector as my

def Connection():
    try:

        mydb=my.connect(host="localhost",
                        user="root",
                        password="",
                        database="hospital"
                        )

        mycursor=mydb.cursor()
        print("Connection is created")
        return mydb
    except Exception as e:
        print(e)
