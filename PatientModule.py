from MyDb import*
from tkinter import messagebox

def PatientSave(pid1,pdb,pnm,pad,pmb,pag,pdis,pgen):
    try:

        mydb=Connection()
        mycursor=mydb.cursor()
        sql="insert into patient values('"+pid1+"','"+pdb+"','"+pnm+"','"+pad+"','"+pmb+"','"+pag+"','"+pdis+"','"+pgen+"')"
        print(sql)
        mycursor.execute(sql)
        messagebox.showinfo('Insert','Record is inserted')
        mydb.commit()

        

    except Exception as e1:

        print("SaveError",e1)


def PatientFind(pid1):
    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="select * from patient where Pid='"+pid1+"'"

        print(sql)

        mycursor.execute(sql)
        data=mycursor.fetchone()

        #messagebox.showinfo('Record','Record is Find')

        return data

        

    except Exception as e2:

        print("FindError",e2)
        #messagebox.showerror('Record','Record is Not Find')



def PatientDelete(pid1):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="delete from patient where Pid="+pid1

        print(sql)
        mycursor.execute(sql)

        mydb.commit()

    except Exception as e3:

        print("DeleteError",e3)

def PatientUpdate(pid1,pdb,pnm,pad,pmb,pag,pdis,pgen):

    try:
        mydb=Connection()

        mycursor=mydb.cursor()

        sql="update patient set Blood='"+pdb+"',Name='"+pnm+"',Address='"+pad+"',Mobile='"+pmb+"',Age='"+pag+"',Disease='"+pdis+"',Gender='"+pgen+"' where Pid="+pid1


        print(sql)

        mycursor.execute(sql)

        mydb.commit()

    except Exception as e4:

        print("UpdateError",e4)


def ShowId():
    try:

        mydb=Connection()

        mycursor=mydb.cursor()

        sql="select count(Pid) from patient"

        print(sql)

        mycursor.execute(sql)

        result=mycursor.fetchone()

        return result;

    except Exception as e5:

        print("ShowidError",e5)

    

    

        

    
