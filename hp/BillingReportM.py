from tkinter import*
from ttkbootstrap import Style
from tkinter import ttk
from PIL import Image,ImageTk
from MyDb import*

def BlReport(root):
    #root=Tk()
    #root.geometry("1500x750")
    photo=Image.open("C:/Users/jayes/OneDrive/Desktop/Billingreport.jpg")

    im=photo.resize((1293,590))
    img=ImageTk.PhotoImage(im)
    back=Label(root,image=img)
    back.place(x=0,y=0)
    mydb=Connection()
    mycursor=mydb.cursor()
    sql="select Pid,Name,Mobile,Disease,Room,Charge,Noofdays,Deposite,Payamount,Policyno from billing"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    a=70
    b=120

    for data in result:
        l1=Label(root,text=data[0],font=("Constantia",11),bg="white")
        l1.place(x=60,y=b)

        l2=Label(root,text=data[1],font=("Constantia",11),bg="white")
        l2.place(x=110,y=b)

        l3=Label(root,text=data[2],font=("Constantia",11),bg="white")
        l3.place(x=300,y=b)


        l4=Label(root,text=data[3],font=("Constantia",11),bg="white")
        l4.place(x=460,y=b)


        l5=Label(root,text=data[4],font=("Constantia",11),bg="white")
        l5.place(x=575,y=b)


        l6=Label(root,text=data[5],font=("Constantia",11),bg="white")
        l6.place(x=710,y=b)

        l7=Label(root,text=data[6],font=("Constantia",11),bg="white")
        l7.place(x=850,y=b)

        l8=Label(root,text=data[7],font=("Constantia",11),bg="white")
        l8.place(x=970,y=b)


        l9=Label(root,text=data[8],font=("Constantia",11),bg="white")
        l9.place(x=1070,y=b)


        l10=Label(root,text=data[9],font=("Constantia",11),bg="white")
        l10.place(x=1160,y=b)





        b=b+36
        


    root.mainloop()

#DReport()
    
