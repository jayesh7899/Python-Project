from MyConnection import*

from tkinter import messagebox

import smtplib


def Reg(em,ps):

    flag=False
    try:
        mydb=Connection()
        mycursor=mydb.cursor()
        sql="insert into login values('"+em+"','"+ps+"')"
        mycursor.execute(sql)
        mydb.commit()
        
        ###############################email Send code#############################

        
        sender="jayeshmali183@gmail.com"
        reciever=em
        message="Hiii....."+em+" Your Password1="+ps
        
        s=smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(sender,'nhybtuejfdxbyvif')
        
        print('login successfully')
        s.sendmail(sender,reciever,message)
        
        print("Email send")
        messagebox.showinfo("Send","Email Send ")
        
        s.quit()
        flag=True
        
        return flag
        
    except Exception as e1:
        return flag
        print("ErrorReg",e1)

def MyLogin(user11,pass11):

    try:

        mydb=Connection()
        mycursor=mydb.cursor()
        sql="select email,password1 from login where email='"+user11+"' and password1='"+pass11+"'"
        mycursor.execute(sql)
        result=mycursor.fetchone()
        mydb.commit()

        return result

    
    except Exception as e2:
        
        print("Myloginerror",e2)


def PassVerify(email1):
    try:
    

        print("jayuuu")
        mydb=Connection()
        mycursor=mydb.cursor()
        sql="select email from login where email='"+email1+"'"
        print(email1)
        print(sql)
        mycursor.execute(sql)
        result=mycursor.fetchone()
        #mydb.commit()
        return result
          
    except Exception as e3:
        print("Error=",e3)

def PassUpdate(email12,pass12):

    try:

        mydb=Connection()

        mycursor=mydb.cursor()
        sql="update login set password1='"+pass12+"' where email='"+email12+"'"
        print(sql)

        mycursor.execute(sql)
        result=mycursor.fetchone()
        print("res up",result)

        mydb.commit()
        return result

    
    except Exception as e4:
        print("updateerrorpass=",e4)
    
        
    


































        

   
    
