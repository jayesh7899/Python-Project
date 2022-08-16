from tkinter import*
from ttkbootstrap import Style
from tkinter import ttk
from PIL import Image,ImageTk
from MyDb import*

def PadmitppReport(root):
    #root=Tk()
    #root.geometry("1500x750")
    photo=Image.open("C:/Users/jayes/OneDrive/Desktop/padmit.jpg")

    im=photo.resize((1293,590))
    img=ImageTk.PhotoImage(im)
    back=Label(root,image=img)
    back.place(x=0,y=0)
    mydb=Connection()
    mycursor=mydb.cursor()
    sql="select AdmitId,Name,Mobile,Gender,Disease,DrName,Room,Charge,Damount from patientadmit"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    a=70
    b=120

    for data in result:
        l1=Label(root,text=data[0],font=("Constantia",10),bg="white")
        l1.place(x=40,y=b)

        l2=Label(root,text=data[1],font=("Constantia",10),bg="white")
        l2.place(x=95,y=b)

        l3=Label(root,text=data[2],font=("Constantia",10),bg="white")
        l3.place(x=275,y=b)


        l4=Label(root,text=data[3],font=("Constantia",10),bg="white")
        l4.place(x=450,y=b)


        l5=Label(root,text=data[4],font=("Constantia",10),bg="white")
        l5.place(x=565,y=b)


        l6=Label(root,text=data[5],font=("Constantia",10),bg="white")
        l6.place(x=695,y=b)

        l7=Label(root,text=data[6],font=("Constantia",10),bg="white")
        l7.place(x=920,y=b)

        l8=Label(root,text=data[7],font=("Constantia",10),bg="white")
        l8.place(x=1050,y=b)


        l9=Label(root,text=data[8],font=("Constantia",10),bg="white")
        l9.place(x=1185,y=b)


        



        b=b+36
        


    root.mainloop()

#DReport()
    
