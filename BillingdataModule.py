from MyDb import*
from tkinter import messagebox

def BillingSave(bhid6,bhdt6,bhnm6,bhmob6,bhdis6,bhroom6,bhchr6,bhday6,bhdps6,bhpamt6,bhtamt6,bhdept6,bhpno6):
    try:

        mydb=Connection()
        mycursor=mydb.cursor()
        sql="insert into billing values('"+bhid6+"','"+bhdt6+"','"+bhnm6+"','"+bhmob6+"','"+bhdis6+"','"+bhroom6+"','"+str(bhchr6)+"','"+str(bhday6)+"','"+bhdps6+"','"+str(bhpamt6)+"','"+str(bhtamt6)+"','"+bhdept6+"','"+bhpno6+"')"
        print(sql)
        mycursor.execute(sql)
        messagebox.showinfo('Insert','Record is inserted')
        mydb.commit()

        

    except Exception as e1:

        print("SavebillingError2",e1)

def BillingFind(bhid6):
    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="select * from billing where Pid='"+bhid6+"'"

        print(sql)

        mycursor.execute(sql)
        data=mycursor.fetchone()

        #messagebox.showinfo('Record','Record is Find')

        return data

        

    except Exception as e2:

        print("FindError",e2)
        #messagebox.showerror('Record','Record is Not Find')

def BillingDelete(bhid6):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()

        sql="delete from billing where Pid="+bhid6

        print(sql)
        mycursor.execute(sql)

        mydb.commit()

    except Exception as e3:

        print("DeleteError",e3)

def BillinggUpdate(bhid6,bhdt6,bhnm6,bhmob6,bhdis6,bhroom6,bhchr6,bhday6,bhdps6,bhpamt6,bhtamt6,bhdept6,bhpno6):
    
    try:
        mydb=Connection()

        mycursor=mydb.cursor()

        sql="update billing set Date='"+bhdt6+"',Name='"+bhnm6+"',Mobile='"+bhmob6+"', Disease='"+bhdis6+"',Room='"+bhroom6+"',Charge='"+str(bhchr6)+"',Noofdays='"+str(bhday6)+"',Deposite='"+bhdps6+"',Payamount='"+str(bhpamt6)+"',Totalamount='"+str(bhtamt6)+"',Dept='"+bhdept6+"',Policyno='"+bhpno6+"' where Pid="+bhid6

        mycursor.execute(sql)
        mydb.commit()

    except Exception as e4:

        print("billingupdateerror",e4)


        



    except Exception as e5:

        print("BillingUpdateError",e5)










