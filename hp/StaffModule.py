from MyDb import*
from tkinter import messagebox

def StaffSave(sid3,sdt3,snm3,sad3,smb3,sexp3,sque3,sgen3,ssal3,sag3):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()
        sql="insert into staff values('"+sid3+"','"+sdt3+"','"+snm3+"','"+sad3+"','"+smb3+"','"+sexp3+"','"+sque3+"','"+sgen3+"','"+ssal3+"','"+sag3+"')"
        
        print(sql)
        mycursor.execute(sql)
        messagebox.showinfo('Insert','Record is inserted')
        mydb.commit()

        

    except Exception as e1:

        print("SaveError",e1)

def StaffFind(sid3):
    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="select * from staff where Sid='"+sid3+"'"

        print(sql)

        mycursor.execute(sql)
        data=mycursor.fetchone()

        #messagebox.showinfo('Record','Record is Find')

        return data

        

    except Exception as e2:

        print("FindError",e2)

def StaffDelete(sid3):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="delete from staff where Sid="+sid3

        print(sql)
        mycursor.execute(sql)

        mydb.commit()

    except Exception as e3:

        print("DeleteError",e3)


def StaffUpdate(sid3,sdt3,snm3,sad3,smb3,sexp3,sque3,sgen3,ssal3,sag3):

    try:
        mydb=Connection()

        mycursor=mydb.cursor()

        sql="update Staff set DOJ='"+sdt3+"',Name='"+snm3+"',Address='"+sad3+"',Mobile='"+smb3+"',Exp='"+sexp3+"',Qualification='"+sque3+"',Gender='"+sgen3+"',Salary='"+ssal3+"',Age='"+sag3+"' where Sid="+sid3



        print(sql)

        mycursor.execute(sql)

        mydb.commit()

    except Exception as e4:

        print("UpdateError",e4)


def ShowId2():
    
    try:

        mydb=Connection()

        mycursor=mydb.cursor()

        sql="select count(Sid) from staff"

        print(sql)

        mycursor.execute(sql)

        result=mycursor.fetchone()

        return result;

    except Exception as e5:

        print("ShowidError",e5)









