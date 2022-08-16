from MyDb import*

def Paid():
    try:
        mydb=Connection()
        print('Connection is Paid create')

        mycursor=mydb.cursor()
        sql="select AppId from appointment"

        mycursor.execute(sql)
        result=mycursor.fetchall()

        return result;
    except Exception as e1:

        print("Paid error",e1)

def PidGetInfo(paid):
    try:
        mydb=Connection()
        mycursor=mydb.cursor()
        sql="select AppId,Date,Name,Address,Gender,Mobile,Disease,DrName from appointment where AppId="+paid
        mycursor.execute(sql)
        result=mycursor.fetchone()
        return result;
    except Exception as e2:

        print("SaveError",e2)


def RoomInfoId(room):
    try:
        mydb=Connection()

        mycursor=mydb.cursor()
        sql=""

        if room=="ICU":
            sql="select (Rate+Oxycharge+Ventilator) from icu"

        
        if room=="Special":
            sql="select Rate from special"

        
        if room=="Genaral":
            sql="select Rate from genaral"

        mycursor.execute(sql)

        result=mycursor.fetchone()
        return result

    except Exception as e2:

        print("RoomSaveerror",e2)
        
        







    
