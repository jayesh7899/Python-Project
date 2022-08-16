from MyDb import*
from tkinter import messagebox

def AppoinmentSave(apid4,apdt4,apnm4,apad4,apgen4,apage4,apwat4,apmob4,apdis4,apdrnm4):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()
        sql="insert into appointment values('"+apid4+"','"+apdt4+"','"+apnm4+"','"+apad4+"','"+apgen4+"','"+apage4+"','"+apwat4+"','"+apmob4+"','"+apdis4+"','"+apdrnm4+"')"
        print(sql)
        mycursor.execute(sql)
        messagebox.showinfo("Insert","Record is Inserted")
        mydb.commit()

    except Exception as e1:

        print("FindError",e1)




def AppoinmentFind(apid4):
    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="select * from appointment where AppId='"+apid4+"'"

        print(sql)

        mycursor.execute(sql)
        data=mycursor.fetchone()

        #messagebox.showinfo('Record','Record is Find')

        return data

        #mydb.commit()

    except Exception as e2:

        print("FindError",e2)

def AppoinmentDelete(apid4):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="delete from appointment where AppId="+apid4

        print(sql)
        mycursor.execute(sql)

        mydb.commit()

    except Exception as e3:

        print("DeleteError",e3)

def AppoinmentUpdate(apid4,apdt4,apnm4,apad4,apgen4,apage4,apwat4,apmob4,apdis4,apdrnm4):

    try:
        mydb=Connection()

        mycursor=mydb.cursor()

        sql="update appointment set Date='"+apdt4+"',Name='"+apnm4+"',Address='"+apad4+"',Gender='"+apgen4+"',Age='"+apage4+"',Weight='"+apwat4+"',Mobile='"+apmob4+"',Disease='"+apdis4+"',DrName='"+apdrnm4+"' where AppId="+apid4



        print(sql)

        mycursor.execute(sql)

        mydb.commit()

    except Exception as e4:

        print("UpdateError",e4)

def ShowId4():
    try:

        mydb=Connection()

        mycursor=mydb.cursor()

        sql="select count(AppId) from appointment"

        print(sql)

        mycursor.execute(sql)

        result=mycursor.fetchone()

        return result;

    except Exception as e5:

        print("ShowidError",e5)




        


    
    
        
