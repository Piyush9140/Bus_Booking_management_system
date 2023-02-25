from tkinter import *
from tkinter.messagebox import askyesnocancel
from tkinter.messagebox import *
from tkinter import messagebox
import mysql.connector as sql
from datetime import date
mydb = sql.connect(
    host='localhost',
    user='root',
    passwd='Piyush@123',
    database = 'busbooking'
    #use_pure=True
)

mycursor=mydb.cursor()

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=10)
Label(root,text='Online Bus Booking System',font="Arial 24 bold", bg='light blue',fg='red').grid(row=1,column=0,columnspan=10)
Label(root,text='Check Your Booking',font="Arial 18 bold", bg='light green',fg='green').grid(row=2,column=0,columnspan=10,pady=h//20)
Label(root,text='Enter Your Mobile No',font="Arial 12 bold",fg='black').grid(row=3,column=4)
a=Entry(root)
a.grid(row=3,column=5)
def confirm():
    answer = askyesno(title='no booking record',
                    message='would you like to book now?')
    if answer:
        root.destroy()
        import enter_journey_detail_pg3
def info():
    if((len(a.get())==0)):
        messagebox.showerror('Error', 'Error:Please enter required details')
    q1='select * from passenger where ph_no=%s'
    cfn=int(a.get())
    t1=(cfn,)
    mycursor.execute(q1,t1)
    r2=mycursor.fetchone()
    if r2==None:
        confirm()
    else:
        final=LabelFrame(root)
        final.grid(row=8,column=4,columnspan=3)
        Label(final, text='Passenger: '+str(r2[0])).grid(row=8,column=0)
        Label(final, text='No of Seats: '+str(r2[1])).grid(row=9,column=0)
        Label(final, text='Age: '+str(r2[2])).grid(row=10,column=0)
        Label(final, text='Booking Ref.: '+str(r2[3])).grid(row=11,column=0)
        Label(final, text='Travels on: '+str(r2[4])).grid(row=12,column=0)
        Label(final, text='Destination: '+str(r2[5])).grid(row=13,column=0)
        Label(final, text='Gender: '+str(r2[6])).grid(row=8,column=1)
        Label(final, text='Phone: '+str(r2[7])).grid(row=9,column=1)
        Label(final, text='Fare Rs: '+str(r2[8])).grid(row=10,column=1)
        Label(final, text='Bus details: '+str(r2[9])).grid(row=11,column=1)
        Label(final, text='Booked On: '+str(r2[10])).grid(row=12,column=1)
        Label(final, text='Boarding Point: '+str(r2[11])).grid(row=13,column=1)
        Label(final, text='Total amount Rs '+str(r2[8])+'to be paid at the time of boarding he bus: ',fg='grey').grid(row=14,column=1)
def on_closing():
    
    direct=askyesnocancel("closing","for closing click yes \n to go to main page click no")
    if direct==True:
        showinfo('Thanks','Thank you for using python bus service')
        root.destroy()
    elif direct==False:
        root.destroy()
        import page2
root.protocol("WM_DELETE_WINDOW", on_closing)
Button(root,text='Check Booking',command=info,font="Arial 12 bold ",fg='black').grid(row=3,column=6)

