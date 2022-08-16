from MyDb import*
from tkinter import messagebox

def DoctorSave(did2,ddt2,dnm2,dad2,dmb2,dexp2,dque2,dgen2,dsal2,dspe2):

    try:

        mydb=Connection()
        print(mydb)
        mycursor=mydb.cursor()
        sql="insert into doctor values('"+did2+"','"+ddt2+"','"+dnm2+"','"+dad2+"','"+dmb2+"','"+dexp2+"','"+dque2+"','"+dgen2+"','"+dsal2+"','"+dspe2+"')"
        
        print(sql)
        mycursor.execute(sql)
        messagebox.showinfo('Insert','Record is inserted')
        mydb.commit()

        

    except Exception as e1:

        print("SaveError",e1)

def DoctorFind(did2):
    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="select * from doctor where Did='"+did2+"'"

        print(sql)

        mycursor.execute(sql)
        data=mycursor.fetchone()

        #messagebox.showinfo('Record','Record is Find')

        return data

        mydb.commit()

    except Exception as e2:

        print("FindError",e2)

def DoctorDelete(did2):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="delete from doctor where Did="+did2

        print(sql)
        mycursor.execute(sql)

        mydb.commit()

    except Exception as e3:

        print("DeleteError",e3)

        

def DoctorUpdate(did2,ddt2,dnm2,dad2,dmb2,dexp2,dque2,dgen2,dsal2,dspe2):

    try:
        mydb=Connection()

        mycursor=mydb.cursor()

        sql="update doctor set Date='"+ddt2+"',Name='"+dnm2+"',Address='"+dad2+"',Mobile='"+dmb2+"',Experience='"+dexp2+"',Qualification='"+dque2+"',Gender='"+dgen2+"',Salary='"+dsal2+"',Specilization='"+dspe2+"' where Did="+did2



        print(sql)

        mycursor.execute(sql)

        mydb.commit()

    except Exception as e4:

        print("UpdateError",e4)

def ShowId1():
    try:

        mydb=Connection()

        mycursor=mydb.cursor()

        sql="select count(Did) from doctor"

        print(sql)

        mycursor.execute(sql)

        result=mycursor.fetchone()

        return result;

    except Exception as e5:

        print("ShowidError",e5)









    
    
