from tkinter import*
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image,ImageTk

from tkinter import messagebox

import mysql.connector as my


from MyDb import*

from PatientModule import*

from DoctorModule import*

from StaffModule import*

from AppoinmentModule import*

from IcuModule import*

from SpecialModule import*

from GeneralModule import*


from AdmitidGenerate import*

from PatientAdmitModule import*

from BillingIdModule import*

from BillingdataModule import*

from Patientreport import*

from ReportDoctor import*

from BillingReportM import*

from Admitnewreport import*

from StaffReport import*

from AppoReport import*

import os
import tempfile

from time import strftime


#from splashwin234 import*




global pd,dd,sd,ad,wd,ic,sp,gw,pa,bh,ck,pk

style=Style(theme="cosmo")

win=style.master

'''['darkly', 'xpnative', 'journal', 'litera', 'clam', 'minty', 'alt', 'superhero',
 'vista', 'lumen', 'yeti', 'pulse', 'winnative', 'classic', 'cosmo', 'solar',
 'united', 'flatly', 'sandstone', 'cyborg', 'default']'''


#==patient dt variable===========

pid1=StringVar()
pdb=StringVar()
pnm=StringVar()
pad=StringVar()
pmb=StringVar()
pag=StringVar()
pdis=StringVar()
pgen=StringVar()

#==doctor dt variable================
did2=StringVar()
ddt2=StringVar()
dnm2=StringVar()
dad2=StringVar()
dmb2=StringVar()
dexp2=StringVar()
dque2=StringVar()
dgen2=StringVar()
dsal2=StringVar()
dspe2=StringVar()


#==staff dt variable====================


sid3=StringVar()
sdt3=StringVar()
snm3=StringVar()
sad3=StringVar()
smb3=StringVar()
sexp3=StringVar()
sque3=StringVar()
sgen3=StringVar()
ssal3=StringVar()
sag3=StringVar()

#==appointment dt variable====================

apid4=StringVar()
apdt4=StringVar()
apnm4=StringVar()
apad4=StringVar()
apgen4=StringVar()
apage4=StringVar()
apwat4=StringVar()
apmob4=StringVar()
apdis4=StringVar()
apdrnm4=StringVar()

#======General ward variable=================
gid1=StringVar()
gdt=StringVar()
gr=StringVar()
gb=StringVar()
grate=StringVar()

#=============Special ward variable==================
sprid1=StringVar()
spdt=StringVar()
spr=StringVar()
spb=StringVar()
sprate=StringVar()

#=======ICU ward variable===========================


icid1=StringVar()
icdt=StringVar()
icr=StringVar()
icb=StringVar()
icrate=StringVar()
icox=StringVar()
icven=StringVar()

#==patient admit variable====================

phid5=StringVar()
phdt5=StringVar()
phnm5=StringVar()
phad5=StringVar()
phmob5=StringVar()
phgen5=StringVar()
phdis5=StringVar()
phdr5=StringVar()
phroom5=StringVar()
phchr5=StringVar()
phdamt5=StringVar()
phdept5=StringVar()

#==Billing hospital variable====================
bhid6=StringVar()
bhdt6=StringVar()
bhnm6=StringVar()
bhmob6=StringVar()

bhdis6=StringVar()

bhroom6=StringVar()
bhchr6=IntVar()
bdayy=IntVar()
bhdps6=StringVar()
bhpamt6=IntVar()
bhtamt6=IntVar()
bhdept6=StringVar()
bhpno6=StringVar()


#===================================Receipt var======================================
#bidr1,dar1,nr1,conr1,roomr1,dayr1,chrr1,damtr1,totr1
bidr1=StringVar()
dar1=StringVar()
nr1=StringVar()
conr1=StringVar()
roomr1=StringVar()
dayr1=StringVar()
chrr1=StringVar()
damtr1=StringVar()
totr1=StringVar()











#=======================================NEW FUNCTION==================================

def NEWP():

    pid1.set("")
            
    pdb.set("")
    pnm.set("")
    pad.set("")
    pmb.set("")
    pag.set("")
    pdis.set("")
    pgen.set("Select")

def NEWD():

    did2.set("")

    ddt2.set("") 
    dnm2.set("")
    dad2.set("")
    dmb2.set("")
    dexp2.set("")
    dque2.set("Select")
    dgen2.set("Select")
    dsal2.set("")
    dspe2.set("Select")

    

def NEWS():

    sid3.set("")

    sdt3.set("") 
    snm3.set("")
    sad3.set("")
    smb3.set("")
    sexp3.set("")
    sque3.set("")
    sgen3.set("Select")
    ssal3.set("")
    sag3.set("")

def NEWA():
    

    apid4.set("")
    apdt4.set("")
    apnm4.set("")
    apad4.set("")
    apgen4.set("Select")
    apage4.set("")
    apwat4.set("")
    apmob4.set("")
    apdis4.set("")
    apdrnm4.set("Select")

def NEWI():

    icid1.set("")
    icdt.set("")
    icr.set("")
    icb.set("")
    icrate.set("")
    icox.set("")
    icven.set("")

def NEWSP():

    sprid1.set("")
    spdt.set("")
    spr.set("")
    spb.set("")
    sprate.set("")

def NEWG():
    gid1.set("")
    gdt.set("")
    gr.set("")
    gb.set("")
    grate.set("")

def NEWPA():
    phid5.set("")
    phdt5.set("")
    phnm5.set("")
    phad5.set("")
    phmob5.set("")
    phgen5.set("")
    phdis5.set("")
    phdr5.set("")
    phroom5.set("")
    phchr5.set("")
    phdamt5.set("")
    phdept5.set("")

def NEWBILLING():

    bhid6.set("")
    bhdt6.set("")
    bhnm6.set("")
    bhmob6.set("")

    bhdis6.set("")

    bhroom6.set("")
    bhchr6.set("")
    bdayy.set("")
    bhdps6.set("")
    bhpamt6.set("")
    bhtamt6.set("")
    bhdept6.set("")
    bhpno6.set("")









    

#==========patient validation===============================

    
def pvalid():
    global msg
    ppdb=pdb.get()
    vpn=pnm.get()
    sn=vpn.replace(" ","")

    vad=pad.get()
    vmb=pmb.get()
    vage=pag.get()
    vdis=pdis.get()
    vgen=pgen.get()
    flag=True
    msg=""

    

    if ppdb=='':
        msg="Enter the Blood"
        flag=False

    elif sn=='' or not sn.isalpha():
        msg="Enter the name"
        flag=False

    elif vad=='':
        msg="Enter the Address"
        flag=False

    elif vmb=='' or not vmb.isdigit() or int(len(vmb))<10:
        msg="Enter the Mobile no"
        flag=False

    elif vage=='' or not vage.isdigit() or int(len(vage))>3:
        msg="Enter the Age"
        flag=False
    elif vdis=='':
        msg="Enter the Disease"
        flag=False
    elif vgen=='':
        msg="Enter the Gender"
        flag=False






    return flag
    


#======Doctor validation========================

def dvalid():
    global msg
    dd=ddt2.get()
    drnm=dnm2.get()
    ss=drnm.replace(" ","")
    dd=ddt2.get()
    dad=dad2.get()
    dm=dmb2.get()
    dex=dexp2.get()
    dqu=dque2.get()
    dge=dgen2.get()
    dsa=dsal2.get()
    dspe=dspe2.get()
    flag=True
    msg=""

    
    if dd=='': 
        msg="Enter the Date"
        flag=False

    elif ss=='' or not ss.isalpha():
        msg="Enter the name"
        flag=False
    elif dad==''or dad.isdigit():
        msg="Enter the Address"
        flag=False
    elif dm=='' or not dm.isdigit() or int(len(dm))<10:
        msg="Enter the Mob no"
        flag=False
    elif dex=='' or int(len(dex))>2:
        msg="Enter the Experiance"
        flag=False
    elif dqu=='':
        msg="Enter the Qualification"
        flag=False
    elif dge=='':
        msg="Enter the Gender"
        flag=False
    elif dsa=='' or not dsa.isdigit():
        msg="Enter the Salary"
        flag=False
    elif dspe=='':
        msg="Enter the Specification"
        flag=False
    



    return flag
#======Staff validation========================


def svalid():
    global msg

    sdtt=sdt3.get()
    snmm=snm3.get()
    gp=snmm.replace(" ","")
    sadd=sad3.get()
    smbb=smb3.get()
    sexpp1=sexp3.get()
    squee=sque3.get()
    sgenn=sgen3.get()
    ssall=ssal3.get()
    sag=sag3.get()

    flag=True
    msg=""

    if sdtt=='': 
        msg="Enter the Date"
        flag=False

    elif gp=='' or not gp.isalpha():
        msg="Enter the name"
        flag=False
    elif sadd==''or sadd.isdigit():
        msg="Enter the Address"
        flag=False
    elif smbb=='' or not smbb.isdigit() or int(len(smbb))<10:
        msg="Enter the Mob no"
        flag=False
    elif sexpp1=='' or int(len(sexpp1))>2:
        msg="Enter the Experiance"
        flag=False
    elif squee=='':
        msg="Enter the Qualification"
        flag=False
    elif sgenn=='':
        msg="Enter the Gender"
        flag=False
    elif ssall=='' or not ssall.isdigit():
        msg="Enter the Salary"
        flag=False
    elif sag=='' or not sag.isdigit() or int(len(sag))>3:
        msg="Enter the Age"
        flag=False

    return flag

#======Appointment validation========================
def avalid():
    global msg

    


    
    aapdt=apdt4.get()
    aapnm=apnm4.get()
    mp=aapnm.replace(" ","")
    aapad=apad4.get()
    aapgen=apgen4.get()
    aapage=apage4.get()
    aapwat=apwat4.get()
    aapmob=apmob4.get()
    aapdis=apdis4.get()
    aapdr=apdrnm4.get()

    flag=True
    msg=""

    if aapdt=='': 
        msg="Enter the Date"
        flag=False

    elif mp=='' or not mp.isalpha():
        msg="Enter the name"
        flag=False
    elif aapad==''or aapad.isdigit():
        msg="Enter the Address"
        flag=False
    elif aapgen=='':
        msg="Enter the Gender"
        flag=False
    elif aapage=='' or not aapage.isdigit() or int(len(aapage))>3:
        msg="Enter the Age"
        flag=False
    elif aapwat=='' or not aapwat.isdigit() or int(len(aapwat))>3:
        msg="Enter the Weight"
        flag=False
    elif aapmob=='' or not aapmob.isdigit() or int(len(aapmob))<10:
        msg="Enter the Mobile"
        flag=False
    elif aapdis=='':
        msg="Enter the Disease"
        flag=False

    elif aapdr=='':
        msg="Enter the Dr Name"
        flag=False


    return flag

#======Patient admit validation========================
def PAdmitttvalid():
    
    global msg


    ppid1=phid5.get()
    ppdt1=phdt5.get()
    ppnm1=phnm5.get()
    ppad1=phad5.get()
    ppmob1=phmob5.get()
    ppgen1=phgen5.get()
    ppdis1=phdis5.get()
    ppdr1=phdr5.get()
    pprm1=phroom5.get()
    ppchr1=phchr5.get()
    ppdamt1=phdamt5.get()
    ppdept1=phdept5.get()

    flag=True

    msg=""

    if ppid1=='': 
        msg="Select Id from Combo"
        flag=False


    elif ppdt1=='': 
        msg="Enter the Date"
        flag=False

    elif ppnm1=='': 
        msg="Enter the Name"
        flag=False

    elif ppad1=='': 
        msg="Enter the Address"
        flag=False

    elif ppmob1=='': 
        msg="Enter the Mobile"
        flag=False

    elif ppgen1=='': 
        msg="Enter the Gender"
        flag=False


    elif ppdis1=='': 
        msg="Enter the Disease"
        flag=False

    elif ppdr1=='': 
        msg="Enter the Dr Name"
        flag=False

    elif pprm1=='' or not pprm1.isalpha():
        msg="Enter the Room"
        flag=False
    
    elif ppchr1=='': 
        msg="Enter the Charge"
        flag=False

    elif ppdamt1=='' or not ppdamt1.isdigit(): 
        msg="Enter the Deposite amt"
        flag=False

    elif ppdept1=='' or not ppdept1.isalpha(): 
        msg="Enter the Dept"
        flag=False

    return flag
    
#======Billing validation========================
def Billingpvalid():
    
    global msg


    bbid2=bhid6.get()
    
    bbdy2=bdayy.get()
    bbdps2=bhdps6.get()
    bbpamt2=bhpamt6.get()
    bbtamt2=bhtamt6.get()
    
    bbpno2=bhpno6.get()

    flag=True

    msg=""

    if bbid2=='': 
        msg="Select Id from Combo"
        flag=False


    elif bbdy2=='': 
        msg="Enter the Day"
        flag=False

    elif bbdps2=='': 
        msg="Enter the D-Amount"
        flag=False

    elif bbpamt2=='': 
        msg="Enter the Pay Amount"
        flag=False

    elif bbtamt2=='': 
        msg="Enter the Total Amount"
        flag=False

    elif bbpno2=='': 
        msg="Fill all field"
        flag=False


    
    return flag
    














    
    

        


    



#==================================patient details data===================================#


def Save(id1):


    
    if pd==True and dd==False and sd==False and ad==False and wd==False and ic==False and sp==False and gw==False and pa==False and bh==False and ck==False and pk==False:
        if id1=='INSERT':

            #other if condition for validation

            if pvalid()==True:
                PatientSave(pid1.get(),pdb.get(),pnm.get(),pad.get(),pmb.get(),pag.get(),pdis.get(),pgen.get())

                NEWP()

                k=ShowId()

                pid1.set(k[0]+1)

                    
            else:
                    
                messagebox.showerror("Error pp",msg)
            
            
                

                    


                
        elif id1=='NEW':
            NEWP()

            k=ShowId()

            pid1.set(k[0]+1)


            '''pid1.set("")
            
            pdb.set("")
            pnm.set("")
            pad.set("")
            pmb.set("")
            pag.set("")
            pdis.set("")
            pgen.set("Select")'''

        elif id1=='FIND':
            try:

                data=PatientFind(pid1.get())

                print(data)

                pid1.set(data[0])
                print(pid1)
                pdb.set(data[1])
                pnm.set(data[2])
                pad.set(data[3])
                pmb.set(data[4])
                pag.set(data[5])
                pdis.set(data[6])
                pgen.set(data[7])
                

                messagebox.showinfo("Find","Record is Find")

            except Exception as e2:

                #print("FindError",e2)

                messagebox.showerror("Find","Record is Not Find")



                

            

        elif id1=='DELETE':

            try:

                result=PatientDelete(pid1.get())

                

                messagebox.showinfo("Delete","Record is delete")

                NEWP()

                #show

                k=ShowId()

                pid1.set(k[0]+1)


                
            except Exception as e3:

                print("DeleteError",e3)

        elif id1=="UPDATE":

            try:

                result=PatientUpdate(pid1.get(),pdb.get(),pnm.get(),pad.get(),pmb.get(),pag.get(),pdis.get(),pgen.get())
                print(result)
                messagebox.showinfo("Update","Record is Updated")

                NEWP()

                #show

                k=ShowId()

                pid1.set(k[0]+1)



            except Exception as e4:

                print("UpdateError",e4)

                #messagebox.showinfo("Update","Record is  Not Updated")
            

            
            

            
    

#==================================doctor details data=================================#
     
    elif pd==False and dd==True and sd==False and ad==False and wd==False and ic==False and sp==False and gw==False and pa==False and bh==False and ck==False and pk==False:
        if id1=='INSERT':
            if dvalid()==True:
                 
                DoctorSave(did2.get(),ddt2.get(),dnm2.get(),dad2.get(),dmb2.get(),dexp2.get(),dque2.get(),dgen2.get(),dsal2.get(),dspe2.get())

                NEWD()

                #show

                
                k1=ShowId1()

                did2.set(k1[0]+1)

            else:
                messagebox.showerror("doctor error",msg)
                
            
        elif id1=='NEW':

            NEWD()

                #show

                
            k1=ShowId1()

            did2.set(k1[0]+1)


            '''did2.set("")

            ddt2.set("") 
            dnm2.set("")
            dad2.set("")
            dmb2.set("")
            dexp2.set("")
            dque2.set("Select")
            dgen2.set("Select")
            dsal2.set("")
            dspe2.set("Select")'''

        elif id1=='FIND':
            try:

                data=DoctorFind(did2.get())

                print(data)

                did2.set(data[0])
                print(pid1)
                ddt2.set(data[1])
                dnm2.set(data[2])
                dad2.set(data[3])
                dmb2.set(data[4])
                dexp2.set(data[5])
                dque2.set(data[6])
                dgen2.set(data[7])
                dsal2.set(data[8])

                dspe2.set(data[9])
                
                messagebox.showinfo("Find","Record is Find")

            except Exception as e2:

                #print("FindError",e2)

                messagebox.showerror("Find","Record is Not Find")



        elif id1=='DELETE':

            try:

                result=DoctorDelete(did2.get())

                messagebox.showinfo("Delete","Record is delete")

                NEWD()

                #show

                
                k1=ShowId1()

                did2.set(k1[0]+1)

                

            except Exception as e3:

                print("DeleteError",e3)

        elif id1=="UPDATE":

            try:

                result=DoctorUpdate(did2.get(),ddt2.get(),dnm2.get(),dad2.get(),dmb2.get(),dexp2.get(),dque2.get(),dgen2.get(),dsal2.get(),dspe2.get())
                print(result)
                messagebox.showinfo("Update","Record is Updated")

                NEWD()

                #show

                
                k1=ShowId1()

                did2.set(k1[0]+1)


            except Exception as e4:

                print("UpdateError",e4)

                #messagebox.showinfo("Update","Record is  Not Updated")
            

            
        





            



#==================================staff details data=================================#



    elif pd==False and dd==False and sd==True and ad==False and wd==False and ic==False and sp==False and gw==False and pa==False and bh==False and ck==False and pk==False:
        
        if id1=='INSERT':
            if svalid()==True:
                StaffSave(sid3.get(),sdt3.get(),snm3.get(),sad3.get(),smb3.get(),sexp3.get(),sque3.get(),sgen3.get(),ssal3.get(),sag3.get())

                NEWS()

                #show

                k2=ShowId2()

                sid3.set(k2[0]+1)

            else:

                messagebox.showerror("staff error",msg)
                


        elif id1=='NEW':
            NEWS()
            #NEWA()

            #show

            k2=ShowId2()

            sid3.set(k2[0]+1)


            '''sid3.set("")

            sdt3.set("") 
            snm3.set("")
            sad3.set("")
            smb3.set("")
            sexp3.set("")
            sque3.set("")
            sgen3.set("Select")
            ssal3.set("")
            sag3.set("")'''

        elif id1=='FIND':

            try:

                data=StaffFind(sid3.get())

                print(data)

                sid3.set(data[0])
                print(sid3)
                sdt3.set(data[1])
                snm3.set(data[2])
                sad3.set(data[3])
                smb3.set(data[4])
                sexp3.set(data[5])
                sque3.set(data[6])
                sgen3.set(data[7])
                ssal3.set(data[8])

                sag3.set(data[9])

                messagebox.showinfo('Record','Record is Find')

            except Exception as e2:

                #print("FindError",e1)

                messagebox.showerror('Record','Record is Not Find')




            

        elif id1=='DELETE':

            try:

                result=StaffDelete(sid3.get())

                messagebox.showinfo("Delete","Record is delete")

                NEWS()

                #show

                k2=ShowId2()

                sid3.set(k2[0]+1)


            except Exception as e3:

                print("DeleteError",e3)


        elif id1=="UPDATE":

            try:

                result=StaffUpdate(sid3.get(),sdt3.get(),snm3.get(),sad3.get(),smb3.get(),sexp3.get(),sque3.get(),sgen3.get(),ssal3.get(),sag3.get())
                print(result)
                messagebox.showinfo("Update","Record is Updated")

                NEWS()

                #show

                k2=ShowId2()

                sid3.set(k2[0]+1)



            except Exception as e4:

                print("UpdateError",e4)

                #messagebox.showinfo("Update","Record is  Not Updated")

#==================================appointment details data=================================#
     
    elif pd==False and dd==False and sd==False and ad==True and wd==False and ic==False and sp==False and gw==False and pa==False and bh==False and ck==False and pk==False:
        if id1=='INSERT':
            if avalid()==True:
            
            
                AppoinmentSave(apid4.get(),apdt4.get(),apnm4.get(),apad4.get(),apgen4.get(),apage4.get(),apwat4.get(),apmob4.get(),apdis4.get(),apdrnm4.get())
                NEWA()

                k4=ShowId4()

                apid4.set(k4[0]+1)

            else:

                messagebox.showerror("appointment error",msg)
            
        elif id1=='NEW':

            NEWA()

            #show

            k4=ShowId4()

            apid4.set(k4[0]+1)

            

            
        elif id1=='FIND':
            try:

                data=AppoinmentFind(apid4.get())

                print(data)

                apid4.set(data[0])
                
                apdt4.set(data[1])
                apnm4.set(data[2])
                apad4.set(data[3])
                apgen4.set(data[4])
                apage4.set(data[5])
                apwat4.set(data[6])
                apmob4.set(data[7])
                apdis4.set(data[8])
                apdrnm4.set(data[9])

                messagebox.showinfo("Find","Record is Find")

            except Exception as e2:

                #print("FindError",e2)

                messagebox.showerror("Find","Record is Not Find")


        elif id1=='DELETE':

            try:

                result=AppoinmentDelete(apid4.get())

                messagebox.showinfo("Delete","Record is delete")

                NEWA()

                #show

                k4=ShowId4()

                apid4.set(k4[0]+1)


                

            except Exception as e3:

                print("DeleteError",e3)

        elif id1=="UPDATE":

            try:

                result=AppoinmentSave(apid4.get(),apdt4.get(),apnm4.get(),apad4.get(),apgen4.get(),apage4.get(),apwat4.get(),apmob4.get(),apdis4.get(),apdrnm4.get())
                print(result)
                messagebox.showinfo("Update","Record is Updated")

                NEWA()

                #show

                k4=ShowId4()

                apid4.set(k4[0]+1)


               

            except Exception as e4:

                print("UpdateError",e4)

                #messagebox.showinfo("Update","Record is  Not Updated")


            

            
            
    elif pd==False and dd==False and sd==False and ad==False and wd==True and ic==False and sp==False and gw==False and pa==False and bh==False and ck==False and pk==False:
        if id1=='INSERT':

            print("fun call")

            
#==================================icu details data=================================#
 

    elif pd==False and dd==False and sd==False and ad==False and wd==False and ic==True and sp==False and gw==False and pa==False and bh==False and ck==False and pk==False:
        if id1=='INSERT':

            IcuSave(icid1.get(),icdt.get(),icr.get(),icb.get(),icrate.get(),icox.get(),icven.get())
            NEWI()
            k5=ShowId5()

            icid1.set(k5[0]+1)

        elif id1=='NEW':
            
            NEWI()
            k5=ShowId5()

            icid1.set(k5[0]+1)


        
        elif id1=='FIND':
            try:

                data=IcuFind(icid1.get())

                print(data)

                icid1.set(data[0])
                icdt.set(data[1])
                icr.set(data[2])
                icb.set(data[3])
                icrate.set(data[4])
                icox.set(data[5])
                icven.set(data[6])

                
                messagebox.showinfo("Find","Record is Find")

            except Exception as e2:

                #print("FindError",e2)

                messagebox.showerror("Find","Record is Not Find")
        
        elif id1=='DELETE':

            try:

                result=IcuDelete(icid1.get())

                messagebox.showinfo("Delete","Record is delete")

                NEWI()

                #show
                k5=ShowId5()

                icid1.set(k5[0]+1)


                

                

            except Exception as e3:

                print("DeleteError",e3)
                
        elif id1=="UPDATE":

            try:

                result=IcuUpdate(icid1.get(),icdt.get(),icr.get(),icb.get(),icrate.get(),icox.get(),icven.get())
                print(result)
                messagebox.showinfo("Update","Record is Updated")

                NEWI()

                #show
                k5=ShowId5()

                icid1.set(k5[0]+1)


                

               

            except Exception as e4:

                print("UpdateError",e4)

                #messagebox.showinfo("Update Record is  Not Updated")

#================================== special details data=================================#
 


    elif pd==False and dd==False and sd==False and ad==False and wd==False and ic==False and sp==True and gw==False and pa==False and bh==False and ck==False and pk==False:
        if id1=='INSERT':

            SpecialSave(sprid1.get(),spdt.get(),spr.get(),spb.get(),sprate.get())

            NEWSP()
            k6=ShowId6()

            sprid1.set(k6[0]+1)


        elif id1=='NEW':
            
            NEWSP()
            k6=ShowId6()

            sprid1.set(k6[0]+1)


        elif id1=='FIND':
            try:

                data=specialFind(sprid1.get())

                print(data)

                sprid1.set(data[0])
                spdt.set(data[1])
                spr.set(data[2])
                spb.set(data[3])
                sprate.set(data[4])
                
                
                messagebox.showinfo("Find","Record is Find")

            except Exception as e2:

                #print("FindError",e2)

                messagebox.showerror("Find","Record is Not Find")
        
        elif id1=='DELETE':
            

            try:

                result=SpecialDelete(sprid1.get())

                messagebox.showinfo("Delete","Record is delete")

                NEWSP()

                #show
                k6=ShowId6()

                sprid1.set(k6[0]+1)

                

                

                

            except Exception as e3:

                print("DeleteError",e3)

        elif id1=="UPDATE":

            try:

                result=SpecialUpdate(sprid1.get(),spdt.get(),spr.get(),spb.get(),sprate.get())
                print(result)
                messagebox.showinfo("Update","Record is Updated")

                NEWSP()

                k6=ShowId6()

                sprid1.set(k6[0]+1)


                #show
                

                

               

            except Exception as e4:

                print("UpdateError",e4)

                #messagebox.showinfo("Update","Record is  Not Updated")

        
        
#==================================General details data=================================#
 
    elif pd==False and dd==False and sd==False and ad==False and wd==False and ic==False and sp==False and gw==True and pa==False and bh==False and ck==False and pk==False:
        if id1=='INSERT':

            GeneralSave(gid1.get(),gdt.get(),gr.get(),gb.get(),grate.get())
            NEWG()
            
            k7=ShowId7()


            gid1.set(k7[0]+1)

            
        elif id1=='NEW':

            NEWG()
            k7=ShowId7()

            gid1.set(k7[0]+1)


        

        elif id1=='FIND':
            try:

                data=GeneralFind(gid1.get())

                print(data)

                gid1.set(data[0])
                gdt.set(data[1])
                gr.set(data[2])
                gb.set(data[3])
                grate.set(data[4])
                
                
                messagebox.showinfo("Find","Record is Find")

            except Exception as e2:

                #print("FindError",e2)

                messagebox.showerror("Find","Record is Not Find")

        elif id1=='DELETE':
            

            try:

                result=GeneralDelete(gid1.get())

                messagebox.showinfo("Delete","Record is delete")

                NEWG()

                #show
                k7=ShowId7()

                gid1.set(k7[0]+1)

                
            except Exception as e3:

                print("DeleteError",e3)

        elif id1=="UPDATE":

            try:

                result=GeneralUpdate(gid1.get(),gdt.get(),gr.get(),gb.get(),grate.get())
                print(result)
                messagebox.showinfo("Update","Record is Updated")

                NEWG()

                k7=ShowId7()

                gid1.set(k7[0]+1)


                #show
                

                

               

            except Exception as e4:

                print("UpdateError",e4)

                #messagebox.showinfo("Update","Record is  Not Updated")

#==================================patient admit details data=================================#
 
    elif pd==False and dd==False and sd==False and ad==False and wd==False and ic==False and sp==False and gw==False and pa==True and bh==False and ck==False and pk==False:
        if id1=='INSERT':
            if PAdmitttvalid()==True:
                
            
                PatientAdmitSave(phid5.get(),phdt5.get(),phnm5.get(),phad5.get(),phmob5.get(),phgen5.get(),phdis5.get(),phdr5.get(),phroom5.get(),phchr5.get(),phdamt5.get(),phdept5.get())
                NEWPA()

            else:

                messagebox.showerror("Patient admit error",msg)
            
                
            
        elif id1=='NEW':

            NEWPA()
            
            #k7=ShowId7()

            #gid1.set(k7[0]+1)

        elif id1=='FIND':
            try:

                data=PatientAdmitFind(phid5.get())

                print(data)

                phid5.set(data[0])
                phdt5.set(data[1])
                phnm5.set(data[2])
                phad5.set(data[3])
                phmob5.set(data[4])
                phgen5.set(data[5])
                phdis5.set(data[6])
                phdr5.set(data[7])
                phroom5.set(data[8])
                phchr5.set(data[9])
                phdamt5.set(data[10])
                phdept5.set(data[11])
                
                
                messagebox.showinfo("Find","Record is Find")

            except Exception as e2:

                #print("FindError",e2)

                messagebox.showerror("Find","Record is Not Find")

        elif id1=='DELETE':
            

            try:

                result=PatientAdmitDelete(phid5.get())

                messagebox.showinfo("Delete","Record is delete")

                NEWPA()

                #show
                
            except Exception as e3:

                print("DeleteError",e3)
                
        elif id1=="UPDATE":

            try:

                result=PatientAdmitUpdate(phid5.get(),phdt5.get(),phnm5.get(),phad5.get(),phmob5.get(),phgen5.get(),phdis5.get(),phdr5.get(),phroom5.get(),phchr5.get(),phdamt5.get(),phdept5.get())

                #print(result)
                messagebox.showinfo("Update","Record is Updated")

                NEWPA()

               

                #show

                
                

                

               

            except Exception as e4:

                print("UpdateError",e4)

                #messagebox.showinfo("Update","Record is  Not Updated")






            
#==================================Billing details data=================================
    elif pd==False and dd==False and sd==False and ad==False and wd==False and ic==False and sp==False and gw==False and pa==False and bh==True and ck==False and pk==False:
        if id1=='INSERT':

            if Billingpvalid()==True:
                
            
                BillingSave(bhid6.get(),bhdt6.get(),bhnm6.get(),bhmob6.get(),bhdis6.get(),bhroom6.get(),bhchr6.get(),bdayy.get(),bhdps6.get(),bhpamt6.get(),bhtamt6.get(),bhdept6.get(),bhpno6.get())

                NEWBILLING()

            else:

                messagebox.showerror("Billing error ",msg)
            
                

        elif id1=='NEW':

            NEWBILLING()

            
        elif id1=='FIND':
            try:

                data=BillingFind(bhid6.get())

                print(data)

                bhid6.set(data[0])
                bhdt6.set(data[1])
                bhnm6.set(data[2])
                bhmob6.set(data[3])

                bhdis6.set(data[4])

                bhroom6.set(data[5])
                bhchr6.set(data[6])
                bdayy.set(data[7])
                bhdps6.set(data[8])
                bhpamt6.set(data[9])
                bhtamt6.set(data[10])
                bhdept6.set(data[11])
                bhpno6.set(data[12])



                messagebox.showinfo("Find","Record is Find")

            except Exception as e2:

                #print("FindError",e2)

                messagebox.showerror("Find","Record is Not Find")

        elif id1=='DELETE':
            

            try:

                result=BillingDelete(bhid6.get())

                messagebox.showinfo("Delete","Record is delete")

                NEWBILLING()

                #show
                
            except Exception as e3:

                print("DeleteError",e3)

        elif id1=="UPDATE":

            try:

                result=BillinggUpdate(bhid6.get(),bhdt6.get(),bhnm6.get(),bhmob6.get(),bhdis6.get(),bhroom6.get(),bhchr6.get(),bdayy.get(),bhdps6.get(),bhpamt6.get(),bhtamt6.get(),bhdept6.get(),bhpno6.get())

                #print(result)
                messagebox.showinfo("Update","Record is Updated")

                NEWBILLING()

               

                #show

                
                

                

               

            except Exception as e4:

                print("UpdateError",e4)

                #messagebox.showinfo("Update","Record is  Not Updated")





                



#==================================unknown details data=================================#
 
    elif pd==False and dd==False and sd==False and ad==False and wd==False and ic==False and sp==False and gw==True and pa==False and bh==False and ck==True and pk==False:
        if id1=='INSERT':
            print('i am call')

#==================================unknown 2 details data=================================#
 
    elif pd==False and dd==False and sd==False and ad==False and wd==False and ic==False and sp==False and gw==True and pa==False and bh==False and ck==False and pk==True:
        if id1=='INSERT':
            print('i am call')

###################################patient report fun###############################################3
def PatientReportt():
    global right,bottom

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    right.add(PReport(right))




###################################doctor report fun###############################################3
def DoctorReportt():
    global right,bottom

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    right.add(DReport(right))

###################################Staff report fun###############################################3
def StaffReportt():
    
    global right,bottom

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    right.add(staffReports(right))
###################################apoointment report fun###############################################3
def AppoReportt():
    global right,bottom

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    right.add(ApReport(right))


###################################patient admit report fun###############################################3

def patientadReportr():

    global right,bottom

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    right.add(PadmitppReport(right))


###################################billind report fun###############################################3
def BillingReportr():
    global right,bottom

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    right.add(BlReport(right))

    

    



#================================== TotalBillingAmt  fun======================


            
def TotalBillingAmt(event):
    print(type(bdayy.get()))
    print(type(bhchr6.get()))
    print(type(bhdps6.get()))

    print(bhtamt6.get())
    print("Charge",bhchr6.get())
    print("days",bdayy.get())
    print("dep",bhdps6.get())
    
    total=bdayy.get()*bhchr6.get()-int(bhdps6.get())
    bhtamt6.set(total)
    #print(type(b.get()))

    
    

    

#================================== Ged id using combobox fun======================
def ComboboxIdget(event):

    res=BillingidGetInfo(bhid6.get())
    print(res)

    

    bhid6.set(res[0])
    bhdt6.set(res[1])
    
   
    bhnm6.set(res[2])
    bhmob6.set(res[3])

    bhdis6.set(res[4])

    bhroom6.set(res[5])
    bhchr6.set(res[6])
    bhdept6.set(res[7])
    bhdps6.set(res[8])
    
    
    #bhpamt6=StringVar()
    #bhtamt6=StringVar()
    
    #bhpno6=StringVar()

   

#================================== BillingHospital details fun=================================#
def BillingHospital():

    global right

    global pd,dd,sd,ad,wd,ic,sp,gw,pa,bh,ck,pk

    #FOR SHOW FUN

    
    pd=False
    dd=False
    sd=False
    ad=False
    wd=False
    ic=False
    sp=False
    gw=False
    pa=False
    bh=True
    ck=False
    pk=False
    

    



    b1.configure(state=NORMAL)
    b2.configure(state=NORMAL)
    b3.configure(state=NORMAL)
    b4.configure(state=NORMAL)
    b5.configure(state=NORMAL)
    sb1.configure(state=NORMAL)
    sb2.configure(state=NORMAL)
    sb3.configure(state=NORMAL)
    b6.configure(state=NORMAL)
    b7.configure(state=NORMAL)
    #b88.configure(state=NORMAL)
    b10.configure(state=NORMAL)
    

    

    new.configure(state=NORMAL)
    
    save.configure(state=NORMAL)
    
    find.configure(state=NORMAL)
    
    exit1.configure(state=NORMAL)

    

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    
    #title

    
    bhtitle=Label(right,text=' Billing Details',
                     fg='#800080',bg='#daf7a6',
                font=('Monotype corsiva',32,'bold'))
    bhtitle.place(x=430,y=16)


    #100,240,470,580


    #b-id
    

    billingid1=Label(right,text='P-Id :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    billingid1.place(x=200,y=100)

    res=PBillingId()

    txtbillingid1=ttk.Combobox(right,width=13,font=('constantia',17,'bold'),
                        textvariable=bhid6,values=res)
    txtbillingid1.place(x=340,y=100)

    txtbillingid1.bind("<<ComboboxSelected>>",ComboboxIdget)
    

    #b date
    
    billingbt1=Label(right,text='Date :',bg='#daf7a6',bd=0,fg='black',
                font=('constantia',15,'bold'))
    billingbt1.place(x=600,y=100)

    txtbillingbt1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,
                        textvariable=bhdt6)
    txtbillingbt1.place(x=750,y=100)
    

    #b-name

    billingname1=Label(right,text='Name :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'),)
    billingname1.place(x=200,y=170)

    
    txtbillingname1=Entry(right,width=44,font=('constantia',17,'bold'),bd=5,
                          textvariable=bhnm6)
    txtbillingname1.place(x=340,y=170)

    #b mobile
    
    billingmb1=Label(right,text='Mobile :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    billingmb1.place(x=200,y=240)

    
    txtbillingmb1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,
                        textvariable=bhmob6)
    txtbillingmb1.place(x=340,y=240)
    #B-dis

    billdis1=Label(right,text='Disease :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    billdis1.place(x=600,y=240)

    
    txtbilldis1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,
                      textvariable=bhdis6)
    txtbilldis1.place(x=750,y=240)


    #B-room

    billroom1=Label(right,text='Room :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    billroom1.place(x=200,y=310)

    
    txtbillroom1=ttk.Combobox(right,width=13,font=('constantia',17,'bold'),
                             textvariable=bhroom6,value=['ICU','Special','Genaral'])
    txtbillroom1.place(x=340,y=310)


    

    #B-charge

    billchar1=Label(right,text='Charge(per day) :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',13,'bold'))
    billchar1.place(x=600,y=310)

    
    txtbillchar1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,
                       textvariable=bhchr6)
    txtbillchar1.place(x=750,y=310)
    

    #B-days


    bdays1=Label(right,text='No of Days :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    bdays1.place(x=200,y=380)

    
    txtbdays1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,
                    textvariable=bdayy)
    txtbdays1.place(x=340,y=380)

    txtbdays1.bind("<FocusIn>",TotalBillingAmt)
    

    #B-deposite


    bdps1=Label(right,text='Deposite :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    bdps1.place(x=600,y=380)

    
    txtbdps1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,
                   textvariable=bhdps6)
    txtbdps1.place(x=750,y=380)

    #B-pay amt


    billamt1=Label(right,text='Pay Amt :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    billamt1.place(x=200,y=450)

    
    txtbillamt1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,
                      textvariable=bhpamt6)
    txtbillamt1.place(x=340,y=450)


    #B-total amt


    billtamt1=Label(right,text='Total Amt :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    billtamt1.place(x=600,y=450)

    
    txtbilltamt1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,
                       textvariable=bhtamt6)
    txtbilltamt1.place(x=750,y=450)

    #B-dept


    billdept1=Label(right,text='Department :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    billdept1.place(x=200,y=520)

    
    txtbilldept1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,
                       textvariable=bhdept6)
    txtbilldept1.place(x=340,y=520)

    #B-policy no


    billpno1=Label(right,text='Policy No :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    billpno1.place(x=600,y=520)

    
    txtbillpno1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,
                      textvariable=bhpno6)
    txtbillpno1.place(x=750,y=520)


   
#==================================roombox id event =================================#
def RoomId(event):
    res=RoomInfoId(phroom5.get())
    phchr5.set(res[0])
    
#==================================Combobox id event=================================#
def ComboboxId(event):
    res=PidGetInfo(phid5.get())

    
    phdt5.set(res[1])
    phnm5.set(res[2])
    phad5.set(res[3])
    phmob5.set(res[5])
    phgen5.set(res[4])
    phdis5.set(res[6])
    phdr5.set(res[7])
    #paroom5.set(res[1])
    #pachr5.set(res[1])
    #padamt5.set(res[9])
    #padept5=StringVar()


#===========================Patient admit fun===================================#3

def Patientad():

    global right

    global pd,dd,sd,ad,wd,ic,sp,gw,pa,bh,ck,pk

    #FOR SHOW FUN

    
    pd=False
    dd=False
    sd=False
    ad=False
    wd=False
    ic=False
    sp=False
    gw=False
    pa=True
    bh=False
    ck=False
    pk=False
    
    

    



    b1.configure(state=NORMAL)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    sb1.configure(state=DISABLED)
    sb2.configure(state=DISABLED)
    sb3.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=NORMAL)
    #b88.configure(state=NORMAL)
    b10.configure(state=NORMAL)
    
    


    

    new.configure(state=NORMAL)
    
    save.configure(state=NORMAL)
    
    find.configure(state=NORMAL)
    
    exit1.configure(state=NORMAL)

    

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    
    #title

    
    patitle=Label(right,text=' Patient Admit Details',
                     fg='#800080',bg='#daf7a6',
                font=('Monotype corsiva',32,'bold'))
    patitle.place(x=380,y=16)


    #100,240,470,580
    


    #pa-id

    patid1=Label(right,text='P-Id :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    patid1.place(x=200,y=100)
    

    res=Paid()

    txtpatid1=ttk.Combobox(right,width=13,font=('constantia',17,'bold')
                           ,values=res,textvariable=phid5)
    txtpatid1.place(x=340,y=100)

    txtpatid1.bind("<<ComboboxSelected>>",ComboboxId)

    

    #date admit
    
    patbt1=Label(right,text='Date :',bg='#daf7a6',bd=0,fg='black',
                font=('constantia',15,'bold'))
    patbt1.place(x=580,y=100)

    txtpatbt1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5
                    ,textvariable=phdt5)
    txtpatbt1.place(x=750,y=100)
    

    #pa-name

    patname1=Label(right,text='P-Name :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',16,'bold'))
    patname1.place(x=200,y=170)

    
    txtpatname1=Entry(right,width=50,font=('constantia',17,'bold'),bd=5,
                      textvariable=phnm5)
    txtpatname1.place(x=340,y=170)

    #pa-address
    
    patadd1=Label(right,text='Address :',bg='#daf7a6',bd=0,fg='black',
                font=('constantia',16,'bold'))
    patadd1.place(x=200,y=240)

    
    txtpatadd1=Entry(right,width=50,font=('constantia',17,'bold'),
                     bd=5,textvariable=phad5)
    txtpatadd1.place(x=340,y=240)

    #pa-mobile


    patmob1=Label(right,text='Mobile :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',16,'bold'))
    patmob1.place(x=200,y=310)

    
    txtpatmob1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5
                     ,textvariable=phmob5)
    txtpatmob1.place(x=340,y=310)

    #pa-gender

    patgen1=Label(right,text='Gender :',bg='#daf7a6',fg='black',
                font=('constantian',15,'bold'))
    patgen1.place(x=580,y=310)
    
    txtpatgen1=ttk.Combobox(right,width=12,font=('constantia',17,'bold'),
                     value=['Male','Female','Other'],textvariable=phgen5)
    txtpatgen1.place(x=750,y=310)

    #pa-disease

    patdis1=Label(right,text='Disease :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    patdis1.place(x=200,y=380)
    
    txtpatdis1=Entry(right,width=13,font=('constantia',17,'bold'),
                     bd=5,textvariable=phdis5)
    txtpatdis1.place(x=340,y=380)


    
    

    #pa-doctor name
    patgender1=Label(right,text='Dr Name :',bg='#daf7a6',fg='black',
                font=('constantian',15,'bold'))
    patgender1.place(x=580,y=380)
    

    
    
        

    txtpatgender1=Entry(right,width=13,font=('constantia',17,'bold'),
                  bd=5,textvariable=phdr5)

    txtpatgender1.place(x=750,y=380)

    #pa-room

    patroom1=Label(right,text='Room :',bg='#daf7a6',fg='black',
                font=('constantian',15,'bold'))
    patroom1.place(x=200,y=450)
    
    txtpatroom1=ttk.Combobox(right,width=12,font=('constantia',17,'bold'),
                     value=['ICU','Special','Genaral'],textvariable=phroom5)
    txtpatroom1.place(x=340,y=450)

    #bind

    txtpatroom1.bind("<<ComboboxSelected>>",RoomId)

    #pa-charge

    patchar1=Label(right,text='Charge(per day) :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    patchar1.place(x=580,y=450)
    
    txtpatchar1=Entry(right,width=13,font=('constantia',17,'bold'),
                      bd=5,textvariable=phchr5)
    txtpatchar1.place(x=750,y=450)

    #pa-dept amt

    patamt1=Label(right,text='Dept amt :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    patamt1.place(x=200,y=520)
    
    txtpatamt1=Entry(right,width=13,font=('constantia',17,'bold'),
                     bd=5,textvariable=phdamt5)
    txtpatamt1.place(x=340,y=520)



    #pa dept

    patdept1=Label(right,text='Department :',bg='#daf7a6',fg='black',
                font=('constantian',15,'bold'))
    patdept1.place(x=580,y=520)
    
    txtpatdept1=ttk.Combobox(right,width=12,font=('constantia',17,'bold'),
                     value=['Government','Private'],textvariable=phdept5)
    txtpatdept1.place(x=750,y=520)





    


#==========================General ward details=================================================
def Generaldt():
    global right

    global pd,dd,sd,ad,wd,ic,sp,gw,pa,bh,ck,pk

    k7=ShowId7()

    gid1.set(k7[0]+1)


    

    pd=False
    dd=False
    sd=False
    ad=False
    wd=False
    ic=False
    
    sp=False
    gw=True
    pa=False
    bh=False
    ck=False
    pk=False
    

  

    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    sb1.configure(state=DISABLED)
    sb2.configure(state=DISABLED)
    sb3.configure(state=NORMAL)
    b6.configure(state=NORMAL)
    b7.configure(state=NORMAL)
    #b88.configure(state=NORMAL)
    b10.configure(state=NORMAL)
    
   
    new.configure(state=NORMAL)
    save.configure(state=NORMAL)
    find.configure(state=NORMAL)
    update.configure(state=NORMAL)
    delete.configure(state=NORMAL)
    exit1.configure(state=NORMAL)
    
   

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    #title

    
    genatitle=Label(right,text=' Genaral ward Details',
                     fg='#800080',bg='#daf7a6',
                font=('Monotype corsiva',32,'bold'))
    genatitle.place(x=380,y=8)


    
    
    aid=Label(right,text='Gen-Id',
                  bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    aid.place(x=150,y=80)

    txtaid=Entry(right,textvariable=gid1,
                  font=('constantia',17,'bold'),bd=5)
    txtaid.place(x=340,y=80)

    dt=Label(right,text='Date',
                  bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    dt.place(x=690,y=80)

    txtdt=Entry(right,width=19,textvariable=gdt,
                            
                  font=('constantia',17,'bold'),bd=5)
    txtdt.place(x=790,y=80)


    room=Label(right,text='No Of Room',
                  bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    room.place(x=150,y=150)

    txtroom=Entry(right,textvariable=gr,font=('constantia',17,'bold'),bd=5)
    txtroom.place(x=340,y=150)

    bed=Label(right,text='No Of Bed',
                  bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    bed.place(x=150,y=220)

    txtbed=Entry(right,textvariable=gb,
                  font=('constantia',17,'bold'),bd=5)

    txtbed.place(x=340,y=220)

    rate=Label(right,text='Rate(Per day)',
                  bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    rate.place(x=150,y=290)

    txtrate=Entry(right,textvariable=grate,
                  font=('constantia',17,'bold'),bd=5)
    txtrate.place(x=340,y=290)


    
#=================================Special ward deatils========================================

def Specialdt():
    
    
    global right
    global pd,dd,sd,ad,wd,ic,sp,gw,pa,bh,ck,pk

    k6=ShowId6()

    sprid1.set(k6[0]+1)
    

    pd=False
    dd=False
    sd=False
    ad=False
    wd=False
    ic=False
    sp=True
    gw=False
    pa=False
    bh=False
    ck=False
    pk=False
    

  
   
   

   
   
   
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    
    sb1.configure(state=DISABLED)
    sb2.configure(state=NORMAL)
    sb3.configure(state=NORMAL)
    b6.configure(state=DISABLED)
    b7.configure(state=NORMAL)
    #b88.configure(state=NORMAL)
    b10.configure(state=NORMAL)
    
   
    
    new.configure(state=NORMAL)
    save.configure(state=NORMAL)
    find.configure(state=NORMAL)
    update.configure(state=NORMAL)
    delete.configure(state=NORMAL)
    exit1.configure(state=NORMAL)

    right.pack_forget()
    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    #title
    speatitle=Label(right,text=' Special ward Details',
                     fg='#800080',bg='#daf7a6',
                font=('Monotype corsiva',30,'bold'))
    speatitle.place(x=380,y=8)


   
   
   
    aid=Label(right,text='Spec-Id',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    aid.place(x=150,y=80)
   
    txtaid=Entry(right,textvariable=sprid1,
                  font=('constantia',17,'bold'),bd=5)
    txtaid.place(x=340,y=80)
   
    dt=Label(right,text='Date',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    dt.place(x=690,y=80)
   
    txtdt=Entry(right,width=19,
                            textvariable=spdt,
                  font=('constantia',17,'bold'),bd=5)
    txtdt.place(x=790,y=80)
   
    room=Label(right,text='No Of Room',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    room.place(x=150,y=150)

    txtroom=Entry(right,textvariable=spr,
                 font=('constantia',17,'bold'),bd=5)
    txtroom.place(x=340,y=150)

    bed=Label(right,text='No Of Bed',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    bed.place(x=150,y=220)

    txtbed=Entry(right,textvariable=spb,
                  font=('constantia',17,'bold'),bd=5)
    txtbed.place(x=340,y=220)

    rate=Label(right,text='Rate(per day)',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    rate.place(x=150,y=290)

    txtrate=Entry(right,textvariable=sprate,
                 font=('constantia',17,'bold'),bd=5)
    txtrate.place(x=340,y=290)


   
   

    
#========================================ICU ward details==================================

def Icudt():
    global right
    global pd,dd,sd,ad,wd,ic,sp,gw,pa,bh,ck,pk

    k5=ShowId5()

    icid1.set(k5[0]+1)


    

    pd=False
    dd=False
    sd=False
    ad=False
    wd=False
    ic=True
    sp=False
    gw=False
    pa=False
    bh=False
    ck=False
    pk=False
    

    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    sb1.configure(state=NORMAL)
    sb2.configure(state=NORMAL)
    sb3.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=NORMAL)
    #b88.configure(state=NORMAL)
    b10.configure(state=NORMAL)
    
   
    new.configure(state=NORMAL)
    save.configure(state=NORMAL)
    find.configure(state=NORMAL)
    update.configure(state=NORMAL)
    delete.configure(state=NORMAL)
    exit1.configure(state=NORMAL)
    
   

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    #title

    
    icuatitle=Label(right,text=' ICU ward',
                     fg='#800080',bg='#daf7a6',
                font=('Monotype corsiva',30,'bold'))
    icuatitle.place(x=410,y=8)


    
    
    aid=Label(right,text='ICU-Id',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    aid.place(x=150,y=80)

    txtaid=Entry(right,textvariable=icid1,
                  font=('constantia',17,'bold'),bd=5)
    txtaid.place(x=340,y=80)

    dt=Label(right,text='Date',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    dt.place(x=690,y=80)

    txtdt=Entry(right,width=19,textvariable=icdt,
                  font=('constantia',17,'bold'),bd=5)
    txtdt.place(x=790,y=80)


    room=Label(right,text='No Of Room',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    room.place(x=150,y=150)

    txtroom=Entry(right,textvariable=icr,
                 font=('constantia',17,'bold'),bd=5)
    txtroom.place(x=340,y=150)

    bed=Label(right,text='No Of Bed',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    bed.place(x=150,y=220)

    txtbed=Entry(right,textvariable=icb,
                  font=('constantia',17,'bold'),bd=5)
    txtbed.place(x=340,y=220)

    rate=Label(right,text='Rate(Per day)',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    rate.place(x=150,y=290)

    txtrate=Entry(right,textvariable=icrate,
                  font=('constantia',17,'bold'),bd=5)
    txtrate.place(x=340,y=290)

    ox=Label(right,text='Oxygen Charge',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))

    ox.place(x=150,y=360)

    txtox=Entry(right,textvariable=icox,
                 font=('constantia',17,'bold'),bd=5)
    txtox.place(x=340,y=360)

    ven=Label(right,text='Ventilator Chrg ',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    ven.place(x=150,y=430)

    txtven=Entry(right,
                     textvariable=icven,
                  font=('constantia',17,'bold'),bd=5)
    txtven.place(x=340,y=430)
    

                
            

################################word dt fun################################################3
def warddt():
    pass
    
    
   



#################################appointment dt fun################################################3


def appointmentdt():

    
    global right

    global pd,dd,sd,ad,wd,ic,sp,gw,pa,bh,ck,pk

    k4=ShowId4()

    apid4.set(k4[0]+1)


    


    

    pd=False
    dd=False
    sd=False
    ad=True
    wd=False
    ic=False
    sp=False
    gw=False
    pa=False
    bh=False
    ck=False
    pk=False
    

    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=NORMAL)
    b5.configure(state=DISABLED)
    
    sb1.configure(state=NORMAL)
    sb2.configure(state=DISABLED)
    sb3.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=NORMAL)
    #b88.configure(state=NORMAL)
    b10.configure(state=NORMAL)
    




    new.configure(state=NORMAL)
    
    save.configure(state=NORMAL)
    
    find.configure(state=NORMAL)
    
    exit1.configure(state=NORMAL)

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    
    
    #a-title

    
    atitle2=Label(right,text=' Appointment Details',fg='#800080',
                     bg='#daf7a6',
                font=('Monotype corsiva',32,'bold'))
    atitle2.place(x=380,y=10)





    
    
    #a-id

    appid4=Label(right,text='Appo-Id :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    appid4.place(x=200,y=100)

    txtappid4=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=apid4)
    txtappid4.place(x=340,y=100)

    #a-date
    
    appdt4=Label(right,text='Date :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    appdt4.place(x=580,y=100)

    txtappdt4=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=apdt4)
    txtappdt4.place(x=710,y=100)


    #a-name

    appname4=Label(right,text='Name :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'),)
    appname4.place(x=200,y=170)

    
    txtappname4=Entry(right,width=44,font=('constantia',17,'bold'),bd=5,textvariable=apnm4)
    txtappname4.place(x=340,y=170)

    #a-address
    
    appadd4=Label(right,text='Address :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    appadd4.place(x=200,y=240)

    
    txtappadd4=Entry(right,width=44,font=('constantia',17,'bold'),bd=5,textvariable=apad4)
    txtappadd4.place(x=340,y=240)

    #a-gender
    appgender4=Label(right,text='Gender :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    appgender4.place(x=200,y=310)
    

    
    
    txtappgender4=ttk.Combobox(right,font=('constantia',17,'bold'),textvariable=apgen4
                        ,width=12,value=['Male','Female','Other'])

    txtappgender4.place(x=340,y=310)

     #a-age

    appage4=Label(right,text='Age :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    appage4.place(x=580,y=310)
    
    txtappage4=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=apage4)
    txtappage4.place(x=710,y=310)

    #a-weight
    
    

    appwt4=Label(right,text='Weight :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    appwt4.place(x=200,y=380)

    
    txtappwt4=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=apwat4)
    txtappwt4.place(x=340,y=380)

    
    #a-mobile


    appmob4=Label(right,text='Mobile :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    appmob4.place(x=580,y=380)

    
    txtappmob4=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=apmob4)
    txtappmob4.place(x=710,y=380)


    
    #a-disease


    appdis4=Label(right,text='Disease :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    appdis4.place(x=200,y=450)

    
    txtappdis4=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=apdis4)
    txtappdis4.place(x=340,y=450)

    #a-drname


    appdrname4=Label(right,text='Dr Name :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    appdrname4.place(x=580,y=450)

    
    txtappdrname4=ttk.Combobox(right,width=12,font=('constantia',17),textvariable=apdrnm4,
                        value=['Dr.Bhaghwat Mahajan','Dr.Prashant Mahajan','Dr.Usha Mahajan','Dr.Shalini Mahajan'])
    txtappdrname4.place(x=710,y=450)





##################################staff dt fun################################################3



def staffdt():

    
    global right

    global pd,dd,sd,ad,wd,ic,sp,gw,pa,bh,ck,pk

    k2=ShowId2()

    sid3.set(k2[0]+1)




    

    pd=False
    dd=False
    sd=True
    ad=False
    wd=False
    ic=False
    sp=False
    gw=False
    pa=False
    bh=False
    ck=False
    pk=False
    
    

    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=NORMAL)
    b4.configure(state=NORMAL)
    b5.configure(state=DISABLED)
    
    sb1.configure(state=DISABLED)
    sb2.configure(state=DISABLED)
    sb3.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=NORMAL)
    #b88.configure(state=NORMAL)
    b10.configure(state=NORMAL)
    



    new.configure(state=NORMAL)
    
    save.configure(state=NORMAL)
    
    find.configure(state=NORMAL)
    
    exit1.configure(state=NORMAL)

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    '''frame1=Frame(right,bg='white',bd=5)
    frame1.place(x=150,y=50,width=700,height=600)'''

    
    #s-title

    
    stitle=Label(right,text=' Staff Details',fg='#800080',
                     bg='#daf7a6',
                font=('Monotype corsiva',30,'bold'))
    stitle.place(x=420,y=13)


    #s-id

    staffid3=Label(right,text='S-Id :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    staffid3.place(x=200,y=100)

    txtstaffid3=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=sid3)
    txtstaffid3.place(x=340,y=100)

    #s-date
    
    staffdt3=Label(right,text='DOJ :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    staffdt3.place(x=580,y=100)

    txtstaffdt3=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=sdt3)
    txtstaffdt3.place(x=710,y=100)


    #S-name

    staffname3=Label(right,text='Name :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'),)
    staffname3.place(x=200,y=170)

    
    txtstaffname3=Entry(right,width=44,font=('constantia',17,'bold'),bd=5,textvariable=snm3)
    txtstaffname3.place(x=340,y=170)

    #s-address
    
    staffadd3=Label(right,text='Address :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    staffadd3.place(x=200,y=240)

    
    txtstaffadd3=Entry(right,width=44,font=('constantia',17,'bold'),bd=5,textvariable=sad3)
    txtstaffadd3.place(x=340,y=240)

    '''#s-Post
    
    staffpost3=Label(right,text='Post :',bg='white',bd=0,fg='black',
                font=('constantian',15,'bold'))
    staffpost3.place(x=470,y=230)
    

    staffpost3=ttk.Combobox(right,font=('constantia',15,'bold'),textvariable=spt3
                        ,width=7,value=['Male','Female'])

    staffpost3.place(x=580,y=230)'''

    

    

    #s-mobile


    staffmob3=Label(right,text='Mobile :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    staffmob3.place(x=200,y=310)

    
    txtstaffmob3=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=smb3)
    txtstaffmob3.place(x=340,y=310)

    #s-experience

    staffexp3=Label(right,text='Exp :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    staffexp3.place(x=580,y=310)
    
    txtstaffexp3=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=sexp3)
    txtstaffexp3.place(x=710,y=310)

    #s-qualification

    staffque3=Label(right,text='Qualification :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    staffque3.place(x=200,y=380)

    staffque3=ttk.Combobox(right,font=('constantia',17,'bold'),textvariable=sque3
                        ,width=10,value=['Male','Female','Other'])

    staffque3.place(x=340,y=380)

    
    
    
    

    #s-gender
    staffgender3=Label(right,text='Gender :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    staffgender3.place(x=580,y=380)
    

    
    
        #label12=Label(showdataframe,text='Select :')
        #label12.place(x=320,y=330)


    txtstaffgender3=ttk.Combobox(right,font=('constantia',17,'bold'),textvariable=sgen3
                        ,width=10,value=['Male','Female','Other'])

    txtstaffgender3.place(x=710,y=380)

    #s-salary


    staffsal3=Label(right,text='Salary :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    staffsal3.place(x=200,y=450)

    
    txtstaffsal3=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=ssal3)
    txtstaffsal3.place(x=340,y=450)

    #s-age

    staffage3=Label(right,text='Age :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    staffage3.place(x=580,y=450)
    
    txtstaffage3=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=sag3)
    txtstaffage3.place(x=710,y=450)


###################################doctor dt fun##############################################3


def doctordt():

    
    global right

    global pd,dd,sd,ad,wd,ic,sp,gw,pa,bh,ck,pk

    k1=ShowId1()

    did2.set(k1[0]+1)



    pd=False
    dd=True
    sd=False
    ad=False
    wd=False
    ic=False
    sp=False
    gw=False
    pa=False
    bh=False
    ck=False
    pk=False
    


    b1.configure(state=DISABLED)
    b2.configure(state=NORMAL)
    b3.configure(state=NORMAL)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    
    sb1.configure(state=DISABLED)
    sb2.configure(state=DISABLED)
    sb3.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=NORMAL)
    #b88.configure(state=NORMAL)
    b10.configure(state=NORMAL)
    


    new.configure(state=NORMAL)
    
    save.configure(state=NORMAL)
    
    find.configure(state=NORMAL)
    
    exit1.configure(state=NORMAL)

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    '''frame1=Frame(right,bg='white',bd=5)
    frame1.place(x=150,y=50,width=700,height=600)'''

    
    #d-title

    
    dtitle=Label(right,text=' Doctor Details',fg='#800080',
                     bg='#daf7a6',
                font=('Monotype corsiva',32,'bold'))
    dtitle.place(x=380,y=25)

    


    #d-id

    docid2=Label(right,text='D-Id :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    docid2.place(x=200,y=120)

    txtdocid2=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=did2)
    txtdocid2.place(x=360,y=120)

    #d-date
    
    docdt2=Label(right,text='DOJ :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    docdt2.place(x=600,y=120)

    txtdocdt2=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=ddt2)
    txtdocdt2.place(x=750,y=120)


    #d-name

    docname2=Label(right,text='D-Name :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    docname2.place(x=200,y=190)

    
    txtdocname2=Entry(right,width=44,font=('constantia',17,'bold'),bd=5,textvariable=dnm2)
    txtdocname2.place(x=360,y=190)

    #d-address
    
    docadd2=Label(right,text='Address :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    docadd2.place(x=200,y=260)

    
    txtdocadd2=Entry(right,width=44,font=('constantia',17,'bold'),bd=5,textvariable=dad2)
    txtdocadd2.place(x=360,y=260)

    #d-mobile


    docmob2=Label(right,text='Mobile :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    docmob2.place(x=200,y=330)

    
    txtdocmob2=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=dmb2)
    txtdocmob2.place(x=360,y=330)

    #d-experience

    docexp2=Label(right,text='Exp :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    docexp2.place(x=600,y=330)
    
    txtdocexp2=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=dexp2)
    txtdocexp2.place(x=750,y=330)

    #d-qualification

    docque2=Label(right,text='Qualification :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    docque2.place(x=200,y=400)

    txtdocque2=ttk.Combobox(right,font=('constantia',17,'bold'),textvariable=dque2
                        ,width=12,value=['Male','Female','Other'])

    txtdocque2.place(x=360,y=400)

    
    

    
    

    #d-gender
    docgender2=Label(right,text='Gender :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    docgender2.place(x=600,y=400)
    

    
    
        #label12=Label(showdataframe,text='Select :')
        #label12.place(x=320,y=330)


    docgender2=ttk.Combobox(right,font=('constantia',17,'bold'),textvariable=dgen2
                        ,width=12,value=['Male','Female','Other'])

    docgender2.place(x=750,y=400)

    #d-salary


    docsal2=Label(right,text='Salary :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    docsal2.place(x=200,y=470)

    
    txtdocsal2=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=dsal2)
    txtdocsal2.place(x=360,y=470)

    #d-specification

    docspe2=Label(right,text='Specilazation :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    docspe2.place(x=600,y=470)

    txtdocspe2=ttk.Combobox(right,font=('constantia',17,'bold'),textvariable=dspe2
                        ,width=12,value=['Anesthesiologists','Cardiologists','Dermatologists','Family Physicians','Hematologists','Neurologists','Nephrologists','Radiologists','Rheumatologists','Podiatrist','Urologists','General Surgeons','Pathologists','Plastic Surgeons','ENT'])

    txtdocspe2.place(x=750,y=470)

    


###################################patient dt fun###############################################3


def patientdt():
    global right

    global pd,dd,sd,ad,wd,ic,sp,gw,pa,bh,ck,pk

    #FOR SHOW FUN

    k=ShowId()

    pid1.set(k[0]+1)

    pd=True
    dd=False
    sd=False
    ad=False
    wd=False
    ic=False
    sp=False
    gw=False
    pa=False
    bh=False
    ck=False
    pk=False
    
    

    



    b1.configure(state=NORMAL)
    b2.configure(state=NORMAL)
    b3.configure(state=NORMAL)
    b4.configure(state=NORMAL)
    b5.configure(state=NORMAL)
    sb1.configure(state=NORMAL)
    sb2.configure(state=NORMAL)
    sb3.configure(state=NORMAL)
    b6.configure(state=NORMAL)
    b7.configure(state=NORMAL)
    #b88.configure(state=NORMAL)
    b10.configure(state=NORMAL)
    





    

    new.configure(state=NORMAL)
    
    save.configure(state=NORMAL)
    
    find.configure(state=NORMAL)
    
    exit1.configure(state=NORMAL)

    

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    
    #title

    
    ptitle=Label(right,text=' Patient Details',
                     fg='#800080',bg='#daf7a6',
                font=('Monotype corsiva',32,'bold'))
    ptitle.place(x=390,y=17)


    #100,240,470,580


    #p-id

    ptid1=Label(right,text='P-Id :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    ptid1.place(x=200,y=100)

    txtptid1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=pid1)
    txtptid1.place(x=340,y=100)

    #blood grp
    
    ptbd1=Label(right,text='Blood Group :',bg='#daf7a6',bd=0,fg='black',
                font=('constantia',15,'bold'))
    ptbd1.place(x=580,y=100)

    txtptbd1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=pdb)
    txtptbd1.place(x=740,y=100)
    

    #p-name

    ptname1=Label(right,text='P-Name :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'),)
    ptname1.place(x=200,y=170)

    
    txtptname1=Entry(right,width=44,font=('constantia',17,'bold'),bd=5,textvariable=pnm)
    txtptname1.place(x=340,y=170)

    #p-address
    
    ptadd1=Label(right,text='Address :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    ptadd1.place(x=200,y=240)

    
    txtptadd1=Entry(right,width=44,font=('constantia',17,'bold'),bd=5,textvariable=pad)
    txtptadd1.place(x=340,y=240)

    #p-mobile


    ptmob1=Label(right,text='Mobile :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    ptmob1.place(x=200,y=310)

    
    txtptmob1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=pmb)
    txtptmob1.place(x=340,y=310)

    #p-age

    ptage1=Label(right,text='Age :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    ptage1.place(x=580,y=310)
    
    txtptage1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=pag)
    txtptage1.place(x=740,y=310)

    #p-disease

    ptdis1=Label(right,text='Disease :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    ptdis1.place(x=200,y=380)
    
    txtptdis1=Entry(right,width=13,font=('constantia',17,'bold'),bd=5,textvariable=pdis)
    txtptdis1.place(x=340,y=380)


    
    

    #p-gender
    ptgender1=Label(right,text='Gender :',bg='#daf7a6',bd=0,fg='black',
                font=('constantian',15,'bold'))
    ptgender1.place(x=580,y=380)
    

    
    
        #label12=Label(showdataframe,text='Select :')
        #label12.place(x=320,y=330)


    ptgender1=ttk.Combobox(right,font=('constantia',17,'bold'),
                           textvariable=pgen,
                        width=12,value=['Male','Female','Other'],)

    ptgender1.place(x=740,y=380)

#============================bill print function=======================================

def BillPrint():
    filename=tempfile.mktemp(".txt")
    open(filename,"w")
    os.startfile(filename,"Print")




###################################billing data  fun###############################################3


def BillingSlip():
    

    
    global right

    global pd,dd,sd,ad,wd,ic,sp,gw,pa,bh,ck,pk

    search1=StringVar()

    combosearch=StringVar()


    

    right.pack_forget()

    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    
    #title

    
    ptitle=Label(right,text=' Billing Data Slip',
                     fg='#800080',bg='#daf7a6',
                font=('Monotype corsiva',32,'bold'))
    ptitle.place(x=390,y=17)

    lblframe22=LabelFrame(right,font=('time new roman',10,'bold'),text='Search Info',
                    width=520, height=160,bg="white",bd=2)
    lblframe22.place(x=5, y=85)

    #search label

    search2=Label(lblframe22,text="Search By :",bg="orange",fg="black",font=
                  ('constantia',14,'bold'),width=10)
    search2.place(x=10,y=8)

    #combosearch
    search3=ttk.Combobox(lblframe22,font=('constantia',13,'bold'),
                         state='readonly',textvariable=combosearch
                         ,width=11,values=["Select","Pid","Name"])
    

    search3.current(0)
    search3.place(x=160,y=8)

    #Search info

    txtsearch3=Entry(lblframe22,font=('constantia',16,'bold'),
                    bd=2,textvariable=search1,width=14,)
    txtsearch3.place(x=320,y=10)

    
    #label frame for treeview

    lblframe44=LabelFrame(right,font=
                         ('constantia',15,'bold'),bd=3)
    lblframe44.place(x=5,y=350,width=650,height=180)

    # treeview
    tv=ttk.Treeview(lblframe44,column=("Pid","Date","Name","Mobile","Room","Charge","Noofdays","Deposite","Totalamount"))
    tv.pack(fill=BOTH,expand=1)


    

    #==================================SelctView========================================
    def SelectView(event):#here we use event arg bcz we use bind method to tv

        #bill reciept var data show hoto yaa select view ne using bind method
        try:
            view=tv.selection()
            item=tv.item(view)
            data=item['values']
            bidr1.set(data[0])
            dar1.set(data[1])
            nr1.set(data[2])
            conr1.set(data[3])
            roomr1.set(data[4])
            chrr1.set(data[5])
            dayr1.set(data[6])
            damtr1.set(data[7])
            totr1.set(data[8])
            
        except Exception as e:
            print("Error",e)






    
    #heading
    tv.heading("Pid",text="Id",anchor=CENTER)
    tv.heading("Date",text="Date",anchor=CENTER)
    tv.heading("Name",text="Name",anchor=CENTER)
    tv.heading("Mobile",text="Mobile",anchor=CENTER)
    tv.heading("Room",text="Room",anchor=CENTER)
    tv.heading("Charge",text="Charge",anchor=CENTER)
    tv.heading("Noofdays",text="Days",anchor=CENTER)
    tv.heading("Deposite",text="Deposite",anchor=CENTER)
    tv.heading("Totalamount",text="Total Amt",anchor=CENTER)
    

    tv["show"]="headings"

    tv.column("Pid",width=10,anchor=CENTER)
    tv.column("Date",width=20,anchor=CENTER)
    tv.column("Name",width=60,anchor=CENTER)
    tv.column("Mobile",width=40,anchor=CENTER)
    tv.column("Room",width=30,anchor=CENTER)
    
    tv.column("Charge",width=30,anchor=CENTER)
    tv.column("Noofdays",width=20,anchor=CENTER)
    tv.column("Deposite",width=30,anchor=CENTER)
    tv.column("Totalamount",width=30,anchor=CENTER)

    tv.bind("<ButtonRelease>",SelectView)


    #====================================Search data==================================================
    def Search():

        global search
        if combosearch.get()=="" or search1.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                mydb=Connection()
                mycursor=mydb.cursor()
                sql=("select Pid ,Date,Name,Mobile,Room,Charge,Noofdays,Deposite,Totalamount from billing where " +str(combosearch.get())+" LIKE  '%" +str(search1.get())+"%' ")
                mycursor.execute(sql)
                row=mycursor.fetchall()

                
                if len(row)!=0:
                    tv.delete(*tv.get_children())
                    for i in row:
                        tv.insert("",END,values=i)  
                        
                    mydb.commit()

                    messagebox.showinfo('find','record is found')

                else:
                    messagebox.showerror('find','record is not  found')
                   
                mydb.close()
            except Exception as ep3:
                
                messagebox.showerror("Record is Not Found",ep3)

    def ShowAllRecord():
        
        mydb=Connection()
        mycursor=mydb.cursor()
        sql="select Pid ,Date,Name,Mobile,Room,Charge,Noofdays,Deposite,Totalamount from billing"
        mycursor.execute(sql)
        data=mycursor.fetchall()
        
        if len(data)!=0:
            tv.delete(*tv.get_children())
            for A in data:
                tv.insert("",END,values=A)
            mydb.commit()
            
        mydb.close()

    #show button

    b40=Button(lblframe22,text="Show",bg="blue",fg="white",width=15,
          font=('time new roman',13,'bold'),bd=2,command=Search)
    b40.place(x=60,y=80)

    #show all button

    b42=Button(lblframe22,text="Show All",bg="blue",fg="white",width=15,
              font=('time new roman',13,'bold'),bd=2,command=ShowAllRecord)
    b42.place(x=280,y=80)

    def BillInfoClear():
        bidr1.set("")
        dar1.set("")
        nr1.set("")
        conr1.set("")
        roomr1.set("")
        chrr1.set("")
        dayr1.set("")
        damtr1.set("")
        totr1.set("")
            

    #====================================receipt=======================================
    lf3=LabelFrame(right,bd=2)
    lf3.place(x=710,y=40,height=480,width=500)

    
    hplabel=Label(lf3,text="SANJEEVANI HOSPITAL ",font=("Times New Roman",20,"bold"),bg="yellow",fg="#ff4400")
    hplabel.place(x=85,y=15)

    bidr=Label(lf3,text="Bill Receipt",font=("Times New Roman",16,"bold"),width=40,
               bd=5,relief=GROOVE)
    bidr.place(x=2,y=76)

    bir=Label(lf3,text="B-Id :",font=("Times New Roman",13,"bold"))
    bir.place(x=30,y=130)
    txtbir=Label(lf3,textvariable=bidr1)
    txtbir.place(x=88,y=130)

    dar=Label(lf3,text="Date :",font=("Times New Roman",13,"bold"))
    dar.place(x=285,y=130)

    txtdar=Label(lf3,textvariable=dar1)
    txtdar.place(x=365,y=130)

    nr=Label(lf3,text="Name :",font=("Times New Roman",13,"bold"))
    nr.place(x=30,y=170)

    txtnr=Label(lf3,textvariable=nr1)
    txtnr.place(x=88,y=170)

    conr=Label(lf3,text="Contact :",font=("Times New Roman",13,"bold"))
    conr.place(x=285,y=170)

    txtconr=Label(lf3,textvariable=conr1)
    txtconr.place(x=365,y=170)

    l=Label(lf3,text="----------------------------------------------------------------------",font=("bold"))
    l.place(x=0,y=195)

    dr=Label(lf3,text="Description",font=("Times New Roman",16,"bold"))
    dr.place(x=65,y=230)

    amtr=Label(lf3,text="Amount",font=("Times New Roman",16,"bold"))
    amtr.place(x=350,y=230)
    
    roomr=Label(lf3,text="Description of service(room) :",
                font=("Times New Roman",12,"bold"))
    roomr.place(x=40,y=265)

    txtroomr=Label(lf3,textvariable=roomr1)
    txtroomr.place(x=362,y=265)

    dayr=Label(lf3,text="Days of service :",font=("Times New Roman",12,"bold"))
    dayr.place(x=40,y=295)

    txtdayr=Label(lf3,textvariable=dayr1)
    txtdayr.place(x=380,y=295)

    chrr=Label(lf3,text="Charges(Per Day) :",font=("Times New Roman",12,"bold"))
    chrr.place(x=40,y=325)

    txtchrr=Label(lf3,textvariable=chrr1)
    txtchrr.place(x=370,y=325)

    damtr=Label(lf3,text="Deposite Amount :",font=("Times New Roman",12,"bold"))
    damtr.place(x=40,y=355)

    txtdamtr=Label(lf3,textvariable=damtr1)
    txtdamtr.place(x=370,y=355)

    l1=Label(lf3,text="----------------------------------------------------------------------",font=("bold"))
    l1.place(x=0,y=380)

    totr=Label(lf3,text="Total Amount :",font=("Times New Roman",14,"bold"))
    totr.place(x=40,y=410)

    txttotr=Label(lf3,textvariable=totr1)
    txttotr.place(x=370,y=410)

    l2=Label(lf3,text="----------------------------------------------------------------------",font=("bold"))
    l2.place(x=0,y=430)

    
    #print button

    btprnt=Button(right,text="Print",bg="orange",fg="white",width=15,
          font=('time new roman',13,'bold'),bd=2,command=BillPrint)
    btprnt.place(x=730,y=540)

    #cleAR button

    btcls=Button(right,text="Clear",bg="orange",fg="white",width=15,
              font=('time new roman',13,'bold'),bd=2,command=BillInfoClear)
    btcls.place(x=1000,y=540)






 

    
    
##################################homepage fun#############################################33
    
    

def homepage():

    global strftime,count,text,right,win,top,new,save,find,update,delete,exit1,frame1,frame,frame2,b1,b2,b3,b4,b5,b6,sb1,sb2,sb3,b7,b10
    
    width=win.winfo_screenwidth()
    height=win.winfo_screenwidth()

    win.geometry("%dx%d+0+0"%(width,height))

    #top window

    #F0FF33

    style.configure("my1.TPanedwindow",background='#D5F5E3')#D5F5E3
    
    
    


    
    #daf7a6
    #85929E
    top=ttk.PanedWindow(win,orient=HORIZONTAL,style=
                        "my1.TPanedwindow",height=100)
    top.pack(fill=X,side=TOP,pady=1)

    """#title

    title=ttk.Label(top,text="Sanjeevani Hospital",font=
                    ('MV Boli',45,'bold'),style='danger.TLabel'
                    ,background='#D5F5E3')
    title.place(x=490,y=10)"""

    #------------------import date fun-----------------------

    #from time import strftime----library

    def time():
        

        string = strftime('%H:%M:%S %p')

        lbl.config(text = string)

        lbl.after(1000, time)
     
    # Styling the label widget so that clock
    # will look more attractive

    lbl = ttk.Label(top, font = ('calibri', 28, 'bold'),

                background = '#daf7a6',

                foreground = 'black')#daf7a6#a52a2a'
     
    # Placing clock at the centre
    # of the tkinter window

    lbl.place(x=50,y=20)
    time()

    
    ###########################################################################
    ss='welcome to Sanjeevani Hospital'

    count=0
    text=""
    #################################Slider label#######################################
    sliderlabel=Label(top,text=ss,font=('chillar',24,'italic bold'),
                      relief=RIDGE,borderwidth=0,width=35,bg='#660033'
                          ,fg='yellow')#85929E
    sliderlabel.place(x=420,y=23,height=50)

    

    ############################### function slider label#########################################
    def introlabel():
        global count,text
        if(count>=len(ss)):
            count=0
            text=""
            sliderlabel.config(text=text)

        else:
            text=text+ss[count]

            sliderlabel.config(text=text)
            count=count+1

        sliderlabel.after(200,introlabel)
      
    introlabel()


#==========================================================================================



    #bottom window
    
    style.configure("my2.TPanedwindow",background='#EC7063')#565051#85C1E9
    

    bottom=ttk.PanedWindow(win,orient=HORIZONTAL,style=
                        "my2.TPanedwindow",height=150)
    bottom.pack(fill=X,side=BOTTOM,pady=1)


####################################bottom button buttons###########################################


    #frame2


    frame2=Frame(bottom,bg='#EC7063',bd=5)#85C1E9
    frame2.place(x=400,y=15,width=970,height=60)

        
    #new btn

    new=Button(frame2,text='*NEW',width=9,bd=0,bg='#33FFD0',
               fg='#003333',font=('constantia',20,'bold','underline'),
              activebackground='#003300',command=lambda:Save('NEW'),state=DISABLED)
    new.place(x=0,y=0)

    #save btn
    save=Button(frame2,text='*INSERT',width=9,
               bd=0,bg='#ffcc00',fg='#003333',
              font=('constantia',20,'bold','underline'),
              activebackground='#003300',
                command=lambda:Save('INSERT'),state=DISABLED)
    save.place(x=160,y=0)


    #find btn
    find=Button(frame2,text='*FIND',width=9,bd=0,
                 bg='#ffcc00',fg='#003333',
              font=('constantia',20,'bold','underline'),
              activebackground='#003300',command=lambda:Save('FIND'),state=DISABLED)
    find.place(x=320,y=0)



    #update btn
    update=Button(frame2,text='*UPDATE',width=9,
                   bd=0,bg='#98fb98',fg='#003333',
              font=('constantia',20,'bold','underline'),
              activebackground='#003300',command=lambda:Save('UPDATE'),state=NORMAL)
    update.place(x=480,y=0)



    #delete btn
    delete=Button(frame2,text='*DELETE',width=9,
                   bd=0,bg='#db7093',fg='#003333',
              font=('constantia',20,'bold','underline'),
              activebackground='#003300',command=lambda:Save('DELETE'),state=NORMAL)
    delete.place(x=640,y=0)




    #exit btn
    exit1=Button(frame2,text='*EXIT',width=9,
                 bd=0,bg='#ffcc00',fg='#003333',
              font=('constantia',20,'bold','underline'),
              activebackground='#003300',command=win.destroy,state=DISABLED)
    exit1.place(x=800,y=0)
    


    #left window

    

    style.configure("my3.TPanedwindow",background='#008b8b')#008b8b

    #008b8b
    #663300
    #006064

    left=ttk.PanedWindow(win,orient=VERTICAL,style=
                           "my3.TPanedwindow",width=230)
    left.pack(fill=Y,side=LEFT,pady=1)

    #Buttons

    b1=Button(left,text='* Patient Details : ',bd=0,bg='white',fg='black',
          font=('constantia',10,'bold','underline'),width=15,
          activebackground='#c1f80a',command=patientdt)

    b1.place(x=50,y=20)

    b2=Button(left,text='* Doctor Details  :',bd=0,bg='white',fg='black',
              font=('constantia',10,'bold','underline'),width=15,
              activebackground='#c1f80a',command=doctordt)

    b2.place(x=50,y=60)


    b3=Button(left,text='* Staff Details :',bd=0,bg='white',fg='black',
              font=('constantia',10,'bold','underline'),width=15,
              activebackground='#c1f80a',command=staffdt)

    b3.place(x=50,y=100)


    b4=Button(left,text='* Appointment :',bd=0,bg='white',fg='black',
              font=('constantia',10,'bold','underline'),width=15,
              activebackground='#c1f80a',command=appointmentdt)

    b4.place(x=50,y=140)


    b5=Button(left,text='* Ward Details  :',bd=0,bg='white',fg='black',
              font=('constantia',10,'bold','underline'),width=15,
              activebackground='#c1f80a',command=warddt
            )
    b5.place(x=50,y=180)

    sb1=Button(left,text='>>>  * ICU Word  :',bd=0,bg='white',fg='black',
              font=('constantia',8,'bold','underline'),width=15,
              activebackground='#c1f80a',command=Icudt
            )
    sb1.place(x=80,y=210)

    sb2=Button(left,text='>>>  * Special Word  :',bd=0,bg='white',fg='black',
              font=('constantia',8,'bold','underline'),width=15,
              activebackground='#c1f80a',command=Specialdt
            )
    sb2.place(x=80,y=240)

    sb3=Button(left,text='>>>  * General Word  :',bd=0,bg='white',fg='black',
              font=('constantia',8,'bold','underline'),width=15,
              activebackground='#c1f80a',command=Generaldt
            )
    sb3.place(x=80,y=270)

    b6=Button(left,text='* Patient Admit  :',bd=0,bg='white',fg='black',
              font=('constantia',10,'bold','underline'),width=15,
              activebackground='#c1f80a',command=Patientad
            )
    b6.place(x=50,y=300)

    b7=Button(left,text='* Billing Details  :',bd=0,bg='white',fg='black',
              font=('constantia',10,'bold','underline'),width=15,
              activebackground='#c1f80a',command=BillingHospital
            )
    b7.place(x=50,y=340)

    #Reports buttons

    r1=Button(left,text='* 1  :',bd=0,bg='white',fg='black',
              font=('constantia',12,'bold'),width=4,
              activebackground='#c1f80a',command=PatientReportt
            )
    r1.place(x=25,y=380)

    r2=Button(left,text='* 2',bd=0,bg='white',fg='black',
              font=('constantia',12,'bold'),width=4,
              activebackground='#c1f80a',command=DoctorReportt
            )
    r2.place(x=90,y=380)

    r3=Button(left,text='* 3',bd=0,bg='white',fg='black',
              font=('constantia',12,'bold'),width=4,
              activebackground='#c1f80a',command=StaffReportt
            )
    r3.place(x=150,y=380)


    r4=Button(left,text='* 4',bd=0,bg='white',fg='black',
              font=('constantia',12,'bold'),width=4,
              activebackground='#c1f80a',command=AppoReportt
            )
    r4.place(x=25,y=470)


    r5=Button(left,text='* 5',bd=0,bg='white',fg='black',
              font=('constantia',12,'bold'),width=4,
              activebackground='#c1f80a',command=patientadReportr
            )
    r5.place(x=90,y=470)

    r6=Button(left,text='* 6',bd=0,bg='white',fg='black',
              font=('constantia',12,'bold'),width=4,
              activebackground='#c1f80a',command=BillingReportr
            )
    r6.place(x=150,y=470)

    b11=Button(left,text='* Billing Data Slip :',bd=0,bg='white',fg='black',
              font=('constantia',10,'bold','underline'),width=15,
              activebackground='#c1f80a',command=BillingSlip
              )
    b11.place(x=50,y=520)
    
    
    
    
    
    
    b10=Button(left,text='* Exit :',bd=0,bg='white',fg='black',
              font=('constantia',10,'bold','underline'),width=15,
              activebackground='#c1f80a',command=win.destroy
              )
    b10.place(x=50,y=550)
    
    #right window
    
    right=ttk.PanedWindow(win,orient=VERTICAL,style=
                        "my4.TPanedwindow")
    right.pack(fill=BOTH,side=RIGHT,expand=1)

    style.configure("my4.TPanedwindow",background='#daf7a6')#FDEDEC#ffcc99#FDED8C


    #fdedaa
    #img4

    img4=Image.open("/pictures/90.jpg")
    img4=img4.resize((1298,590),Image.ANTIALIAS)
    photoimg4=ImageTk.PhotoImage(img4)

    label=ttk.Label(right,image=photoimg4)
    label.place(x=0,y=0)


    
    """lblframe78=LabelFrame(right,width=770,height=250,font=
                         ('constantia',14,'bold'),bd=3)
    lblframe78.place(x=5,y=1700)

    

    tv=ttk.Treeview(lblframe22)
    tv.place(x=30,y=0)"""

    win.mainloop()


    


homepage()
#MyMainLog()

        


