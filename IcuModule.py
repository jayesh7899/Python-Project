from MyDb import*
from tkinter import messagebox

def IcuSave(icid1,icdt,icr,icb,icrate,icox,icven):
    
    try:

        mydb=Connection()
        mycursor=mydb.cursor()
        sql="insert into icu values('"+icid1+"','"+icdt+"','"+icr+"','"+icb+"','"+icrate+"','"+icox+"','"+icven+"')"
        print(sql)
        mycursor.execute(sql)
        messagebox.showinfo('Insert','Record is inserted')
        mydb.commit()

        

    except Exception as e1:

        print("SaveError",e1)

def IcuFind(icid1):
    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="select * from icu where Icuid='"+icid1+"'"

        print(sql)

        mycursor.execute(sql)
        data=mycursor.fetchone()

        #messagebox.showinfo('Record','Record is Find')

        return data

        

    except Exception as e2:

        print("FindError",e2)
        #messagebox.showerror('Record','Record is Not Find')


def IcuDelete(icid1):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="delete from icu where Icuid="+icid1

        print(sql)
        mycursor.execute(sql)

        mydb.commit()

    except Exception as e3:

        print("DeleteError",e3)

def IcuUpdate(icid1,icdt,icr,icb,icrate,icox,icven):

    try:
        mydb=Connection()

        mycursor=mydb.cursor()

        sql="update icu set Date='"+icdt+"',Room='"+icr+"',Bed='"+icb+"',Rate='"+icrate+"',Oxycharge='"+icox+"',Ventilator='"+icven+"' where Icuid="+icid1

        print(sql)

        mycursor.execute(sql)

        mydb.commit()

    except Exception as e4:

        print("UpdateError",e4)

def ShowId5():
    try:

        mydb=Connection()

        mycursor=mydb.cursor()

        sql="select count(Icuid) from icu"

        print(sql)

        mycursor.execute(sql)

        result=mycursor.fetchone()

        return result;

    except Exception as e5:

        print("ShowidError",e5)





