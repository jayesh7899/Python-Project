from MyDb import*
from tkinter import messagebox

def SpecialSave(sprid1,spdt,spr,spb,sprate):
    
    try:

        mydb=Connection()
        mycursor=mydb.cursor()
        sql="insert into special values('"+sprid1+"','"+spdt+"','"+spr+"','"+spb+"','"+sprate+"')"
        
        print(sql)
        mycursor.execute(sql)
        messagebox.showinfo('Insert','Record is inserted')
        mydb.commit()

        

    except Exception as e1:

        print("SaveError",e1)



def specialFind(sprid1):
    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="select * from special where speid="+sprid1

        print(sql)

        mycursor.execute(sql)
        data=mycursor.fetchone()

        #messagebox.showinfo('Record','Record is Find')

        return data

        

    except Exception as e2:

        print("FindError",e2)
        #messagebox.showerror('Record','Record is Not Find')


def SpecialDelete(sprid1):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="delete from special where speid="+sprid1

        print(sql)
        mycursor.execute(sql)

        mydb.commit()

    except Exception as e3:

        print("DeleteError",e3)

def SpecialUpdate(sprid1,spdt,spr,spb,sprate):

    try:
        mydb=Connection()

        mycursor=mydb.cursor()

        sql="update special set Date='"+spdt+"',Room='"+spr+"',Bed='"+spb+"',Rate='"+sprate+"' where speid="+sprid1

        print(sql)

        mycursor.execute(sql)

        mydb.commit()

    except Exception as e4:

        print("UpdateError",e4)

def ShowId6():
    try:

        mydb=Connection()

        mycursor=mydb.cursor()

        sql="select count(speid) from special"

        print(sql)

        mycursor.execute(sql)

        result=mycursor.fetchone()

        return result;

    except Exception as e5:

        print("ShowidError",e5)


        




