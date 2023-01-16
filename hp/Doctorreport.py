from tkinter import*
from ttkbootstrap import Style
from tkinter import ttk
from PIL import Image,ImageTk
from MyDb import*

def DReport(root):
    root=Tk()
    root.geometry("1500x750")
    photo=Image.open("C:/Users/jayes/OneDrive/Desktop/Doctorreport22.jpg")

    im=photo.resize((1533,600))
    img=ImageTk.PhotoImage(im)
    back=Label(root,image=img)
    back.place(x=0,y=0)
    mydb=Connection()
    mycursor=mydb.cursor()
    sql="select Did,Name,Mobile,Experience,Gender,Salary,Specilization from doctor"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    a=70
    b=160

    for data in result:
        l1=Label(root,text=data[0],font=("Constantia",9),bg="white")
        l1.place(x=60,y=b)

        l2=Label(root,text=data[1],font=("Constantia",9),bg="white")
        l2.place(x=130,y=b)

        l3=Label(root,text=data[2],font=("Constantia",9),bg="white")
        l3.place(x=330,y=b)


        l4=Label(root,text=data[3],font=("Constantia",9),bg="white")
        l4.place(x=590,y=b)


        l5=Label(root,text=data[4],font=("Constantia",9),bg="white")
        l5.place(x=830,y=b)


        l6=Label(root,text=data[5],font=("Constantia",9),bg="white")
        l6.place(x=1040,y=b)

        l7=Label(root,text=data[6],font=("Constantia",9),bg="white")
        l7.place(x=1040,y=b)




        b=b+36
        


    root.mainloop()

DReport()


    
