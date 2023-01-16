from MyDb import*
from tkinter import messagebox

def BillingSave(bhid6,bhdt6,bhnm6,bhmob6,bhdis6,bhroom6,bhchr6,bhday6,bhdps6,bhpamt6,bhtamt6,bhdept6,bhpno6):
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
