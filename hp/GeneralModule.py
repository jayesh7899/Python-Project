from MyDb import*
from tkinter import messagebox

def GeneralSave(gid1,gdt,gr,gb,grate):
    
    try:

        mydb=Connection()
        mycursor=mydb.cursor()
        sql="insert into genaral values('"+gid1+"','"+gdt+"','"+gr+"','"+gb+"','"+grate+"')"
        
        print(sql)
        mycursor.execute(sql)
        messagebox.showinfo('Insert','Record is inserted')
        mydb.commit()

        

    except Exception as e1:

        print("SaveError",e1)

def GeneralFind(gid1):
    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="select * from genaral where Genid="+gid1

        print(sql)

        mycursor.execute(sql)
        data=mycursor.fetchone()

        #messagebox.showinfo('Record','Record is Find')

        return data

        

    except Exception as e2:

        print("FindError",e2)
        #messagebox.showerror('Record','Record is Not Find')

def GeneralDelete(gid1):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="delete from genaral where Genid="+gid1

        print(sql)
        mycursor.execute(sql)

        mydb.commit()

    except Exception as e3:

        print("DeleteError",e3)

def GeneralUpdate(gid1,gdt,gr,gb,grate):

    try:
        mydb=Connection()

        mycursor=mydb.cursor()

        sql="update genaral set Date='"+gdt+"',Room='"+gr+"',Bed='"+gb+"',Rate='"+grate+"' where Genid="+gid1

        print(sql)

        mycursor.execute(sql)

        mydb.commit()

    except Exception as e4:

        print("UpdateError",e4)

def ShowId7():
    try:

        mydb=Connection()

        mycursor=mydb.cursor()

        sql="select count(Genid) from genaral"

        print(sql)

        mycursor.execute(sql)

        result=mycursor.fetchone()

        return result;

    except Exception as e5:

        print("ShowidError",e5)


        





