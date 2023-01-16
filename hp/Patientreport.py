from tkinter import*
from ttkbootstrap import Style
from tkinter import ttk
from PIL import Image,ImageTk
from MyDb import*

def PReport(root):
    #root=Tk()
    #root.geometry("1500x750")
    photo=Image.open("C:/Users/jayes/OneDrive/Desktop/Billingdata.jpg")

    im=photo.resize((1293,600))
    img=ImageTk.PhotoImage(im)
    back=Label(root,image=img)
    back.place(x=0,y=0)
    mydb=Connection()
    mycursor=mydb.cursor()
    sql="select Pid,Name,Address,Mobile,Gender,Disease from patient"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    a=70
    b=160

    for data in result:
        l1=Label(root,text=data[0],font=("Constantia",9),bg="white")
        l1.place(x=60,y=b)

        l2=Label(root,text=data[1],font=("Constantia",9),bg="white")
        l2.place(x=160,y=b)

        l3=Label(root,text=data[2],font=("Constantia",9),bg="white")
        l3.place(x=370,y=b)


        l4=Label(root,text=data[3],font=("Constantia",9),bg="white")
        l4.place(x=630,y=b)


        l5=Label(root,text=data[4],font=("Constantia",9),bg="white")
        l5.place(x=890,y=b)


        l6=Label(root,text=data[5],font=("Constantia",9),bg="white")
        l6.place(x=1130,y=b)



        b=b+36
        


    root.mainloop()

#PatientReport()
    
