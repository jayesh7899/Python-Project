from MyDb import*
from tkinter import messagebox

def PatientAdmitSave(phid5,phdt5,phnm5,phad5,phmob5,phgen5,phdis5,phdr5,phroom5,phchr5,phdamt5,phdept5):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()
        sql="insert into patientadmit values('"+phid5+"','"+phdt5+"','"+phnm5+"','"+phad5+"','"+phmob5+"','"+phgen5+"','"+phdis5+"','"+phdr5+"','"+phroom5+"','"+phchr5+"','"+phdamt5+"','"+phdept5+"')"
        print(sql)
        mycursor.execute(sql)
        #messagebox.showinfo("Insert","Record is Inserted")
        mydb.commit()
        sql1="update  "+phroom5+" set Bed=Bed-1"
        print(sql1)
        mycursor.execute(sql1)
        messagebox.showinfo("Insert","Record is Inserted")
        
        mydb.commit()

        
        
        
        

    except Exception as e1:

        print("Fi",e1)

def PatientAdmitFind(phid5):
    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="select * from patientadmit where AdmitId='"+phid5+"'"

        #print(sql)

        mycursor.execute(sql)
        data=mycursor.fetchone()

        #messagebox.showinfo('Record','Record is Find')

        return data

        

    except Exception as e2:

        print("FindError",e2)
        #messagebox.showerror('Record','Record is Not Find')

def PatientAdmitDelete(phid5):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="delete from patientadmit where AdmitId="+phid5

        print(sql)
        mycursor.execute(sql)

        mydb.commit()

    except Exception as e3:

        print("DeleteError",e3)

def PatientAdmitUpdate(phid5,phdt5,phnm5,phad5,phmob5,phgen5,phdis5,phdr5,phroom5,phchr5,phdamt5,phdept5):
    
    try:
        mydb=Connection()

        mycursor=mydb.cursor()
        
        #select id    
        sql1="select Room from patientadmit where AdmitId='"+phid5+"'"
        mycursor.execute(sql1)
        data=mycursor.fetchone()
        ss=(data[0])
        print(ss)

        #

        sql2="update "+ss+" set Bed=Bed+1"
        print(sql2)

        mycursor.execute(sql2)

        mydb.commit()

        #

        sql3="update "+phroom5+" set Bed=Bed-1"
        print(sql3)
        

        mycursor.execute(sql3)

        mydb.commit()


        #
        sql="update patientadmit set Date='"+phdt5+"',Name='"+phnm5+"',Address='"+phad5+"',Mobile='"+phmob5+"',Gender='"+phgen5+"',Disease='"+phdis5+"',DrName='"+phdr5+"',Room='"+phroom5+"',Charge='"+phchr5+"',Damount='"+phdamt5+"' ,Dept='"+phdept5+"'where AdmitId="+phid5


        print(sql)

        mycursor.execute(sql)

        mydb.commit()

        

    except Exception as e4:

        print("UpdateError",e4)









