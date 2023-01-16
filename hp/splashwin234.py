from tkinter import*
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image,ImageTk

from tkinter import messagebox

from tkinter import Toplevel


from MyData import*



global lblframe


"""['lumen', 'cosmo', 'clam', 'default', 'solar', 'journal', 'yeti',
'alt', 'flatly', 'minty', 'darkly', 'xpnative', 'united', 'classic',
'vista', 'pulse', 'litera', 'cyborg', 'superhero', 'winnative', 'sandstone']"""






def MyMainLog():

    print("i am call")
    style=Style(theme="clam")
    splash_win=style.master
    splash_win.overrideredirect(True)

    splash_win.geometry("403x287+400+300")

    photo=ImageTk.PhotoImage(file="D:/pictures/h11.jpg")

    label=ttk.Label(splash_win,image=photo)
    label.place(x=0,y=0)

    def Loginwindow():

        
        splash_win.destroy()
        style1=Style(theme="clam")
        sp=style1.master

        sp.config(bg="#85929E")

        """img1=Image.open("D:/pictures/signup16.jpg")
        img1=img1.resize((510,800),Image.ANTIALIAS)
        photoimg1=ImageTk.PhotoImage(img1)

        label90=Label(sp,image=photoimg1)
        label90.place(x=0,y=0)"""


        

        #labelframe1

        

        lf=LabelFrame(sp,text="Login",
                          width=560,height=390,font=("Constantia",18,'bold'),bg="#99ff99")
        lf.place(x=20,y=80)

        def Login():
            def LoginPage():
                
                res=MyLogin(user11.get(),pass11.get())
                print(type(res))

                print(res)

                if res!=None:
                    

                    print("jayesh")
                    import hospitalwin7
                    #homepage()

                else:

                    print("Login Invalid")
                    
                    




            
            global lf
            user11=StringVar()
            pass11=StringVar()

            #labelframe2

            lf=LabelFrame(sp,text="Login",
                              width=560,height=390,font=
                          ("Constantia",18,'bold'),bg="#99ff99",fg="#ff0099")
            
            lf.place(x=20,y=80)
            lf.pack_forget()

            #login window label

            titlogin=Label(lf,text="Login Window",
                               font=("Lucida Fax",20,"bold"),bg="#99ff99")

            titlogin.place(x=160,y=30)

            #userid

            user=Label(lf,text="User Id :",font=("constantia",20,"bold")
                           ,bg="#99ff99")
            user.place(x=70,y=100)

            txtuser=ttk.Entry(lf,font=("constantia",20,"bold"),
                              style="success.TEntry",width=15,
                              textvariable=user11)
            txtuser.place(x=230,y=100)

            #password

            
            pass1=Label(lf,text='Password :',font=('constantia',20,'bold'),
                        bg="#99ff99")
            pass1.place(x=70,y=160)

            txtpass1=ttk.Entry(lf,font=('constantia',20,'bold'),
                               style='success.TEntry',width=15,
                               textvariable=pass11)
            txtpass1.place(x=230,y=160)

            #forget password

            forget=Button(lf,text='Forget Password',bd=0,
                          bg='#28231d',highlightthickness=0,fg='sky blue',
                          activebackground='#28231d',cursor="hand2",
                          font=('',9,'underline'),command=reset)

            forget.place(x=234,y=205)


            #login button    

            login1=Button(lf,text='Login',bg="#9933ff",font=('constantia',18,'bold')
                              ,command=LoginPage)

            login1.place(x=110,y=270)

            #messagebox.showinfo('login','Login Successfully')


            #submit button

            reset1=Button(lf,text='Reset'
                         ,bg="#9933ff",font=('constantia',18,'bold'))

            reset1.place(x=340,y=270)

            #messagebox.showinfo('reset','Invalid User Id and Password')

        def Signup():
            

            def save():
                
                res=Reg(em.get(),ps.get())

                if res==True:

                    messagebox.showinfo("save","Record is Inserted")

                    print("record is Inserted")

                else:

                    messagebox.showerror("error","record is not Inserted")

                    
                
            
            global lf

            em=StringVar()
            ps=StringVar()

            #labelframe3

            lf=LabelFrame(sp,text="Login",
                              width=560,height=390,font=
                              ("Lucida Fax",20,"bold"),bg="#99ff99",fg="#ff0099")
            lf.pack_forget()
            lf.place(x=20,y=80)

            #signuplabel

            titlogin=Label(lf,text='SignUp Window',
                               font=('Lucida Fax',20,'bold'),bg="#99ff99"
                               )

            titlogin.place(x=160,y=20)


            
            #email

            email=Label(lf,text='E-Mail :',bg="#99ff99",
                     font=('constantia',20,'bold'),width=9)
            email.place(x=50,y=100)

            txtemail=ttk.Entry(lf,font=('constantia',20,'bold'),
                               textvariable=em,
                               style='warning.TEntry',width=15)
            txtemail.place(x=240,y=100)


            #password
            pass2=Label(lf,text='P@ssword :',bg="#99ff99",
                     font=('constantia',20,'bold'),width=9)
            pass2.place(x=50,y=170)

            txtpass2=ttk.Entry(lf,font=
                        ('constantia',20,'bold'),style='warning.TEntry'
                               ,width=15,textvariable=ps,show="*")
            txtpass2.place(x=240,y=170)


            

            #buttons



            login1=Button(lf,text='Submit',bg="#9933ff",font=('constantia',18,'bold'),
                              command=save)

            login1.place(x=110,y=260)

            #messagebox.showinfo('login','Login Successfully')


            reset1=Button(lf,text='Cancel',bg="#9933ff",
                              font=('constantia',18,'bold'))

            reset1.place(x=340,y=260)

            #messagebox.showinfo('reset','Invalid User Id and Password')

        def Varifypass():
            print("call",email11.get(),newpass11.get())

            if email11.get()!="" and newpass11.get()=="":

                res=PassVerify(email11.get())

                if res!=None:
                    msg1.config(text="Email Verify")
                    txtpass2.config(state=NORMAL)
                else:
                    msg1.config(text="Email Not Verify")
                    txtpass2.config(state=DISABLED)
                    
            elif email11.get()!="" and newpass11.get()!="":

                print("Come")

                print(email11.get())

                res=PassUpdate(email11.get(),newpass11.get())

                
                print(res)

                print("pp",newpass11.get())

                if res==None:
                    messagebox.showinfo("Save","Password Updated")

                else:

                    messagebox.showinfo("Save","Password not Updated")

                    

                    
                    
                
        
        def reset():
            
            global lf,email11,msg1,txtpass2,newpass11

            email11=StringVar()
            newpass11=StringVar()
            

            #labelframe3

            lf=LabelFrame(sp,text="Generate Pass",
                              width=560,height=390,
                              font=("Lucida Fax",20,"bold"),
                          bg="#99ff99",fg="#ff0099")#ff6633
            lf.pack_forget()
            lf.place(x=20,y=80)

            #signuplabel

            titlogin=Label(lf,text='Reset Password',
                               font=("Lucida Fax",20,"bold"),bg="#99ff99")

            titlogin.place(x=160,y=30)


            
            #email

            email=Label(lf,text='E-Mail :',bg="#99ff99",font=('constantia',20,'bold'))
            email.place(x=40,y=100)

            txtemail=ttk.Entry(lf,font=('constantia',20,'bold'),
                               style='warning.TEntry',width=15,
                               textvariable=email11)
            txtemail.place(x=290,y=100)


            #password
            pass2=Label(lf,text='New P@ssword :',bg="#99ff99",
                     font=('constantia',20,'bold'))
            pass2.place(x=40,y=170)

            txtpass2=ttk.Entry(lf,font=
                        ('constantia',20,'bold'),style='warning.TEntry',width=15,
                               textvariable=newpass11)
            txtpass2.place(x=290,y=170)

            msg1=Label(lf,text="",width=15,bg="black",fg="yellow",
                       font=("constantia",9,"bold"))
            msg1.place(x=294,y=145)


            

            #buttons

            

            login1=Button(lf,text='Submit',
                         bg="#9933ff",font=('constantia',18,'bold'),
                          command=Varifypass)

            login1.place(x=110,y=260)

            #messagebox.showinfo('login','Login Successfully')


            reset1=Button(lf,text='Cancel',bg="#9933ff",
                         font=('constantia',18,'bold'))

            reset1.place(x=340,y=260)

            #messagebox.showinfo('reset','Invalid User Id and Password')




            


        sp.geometry('600x500+500+150')

        sp.title('Login Window')

        '''style1.configure('My.success.Outline.TButton',font=('Lucida Handwriting',
                                         17))'''

        login=Button(sp,text='Login',command=Login,font=('Segoe print',12,'bold')
                         ,bg='#00cc00')

        login.place(x=100,y=10)

        '''style1.configure('My.warning.Outline.TButton',font=('Lucida Handwriting',
                                         17))'''

        reg=Button(sp,text='Sign Up',command=Signup,font=('Segoe print',12,'bold')
                         ,bg='#e91e63')

        reg.place(x=350,y=10)






    splash_win.after(1000,Loginwindow)
    splash_win.mainloop()

            
MyMainLog()
#homepage()

splash_win.withdraw()



