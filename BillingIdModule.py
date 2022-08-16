from MyDb import*

def PBillingId():
    try:
        mydb=Connection()
        print('Connection is Billing id create')

        mycursor=mydb.cursor()
        sql="select AdmitId from patientadmit"

        mycursor.execute(sql)
        result=mycursor.fetchall()

        return result;
    except Exception as e1:

        print("Paid error",e1)

def BillingidGetInfo(baid):
    try:
        mydb=Connection()
        mycursor=mydb.cursor()
        sql="select AdmitId,Date,Name,Mobile,Disease,Room,Charge,Dept,Damount from patientadmit where AdmitId="+baid
        mycursor.execute(sql)
        result=mycursor.fetchone()
        return result;
    except Exception as e2:

        print("SaveBillling",e2)


    
