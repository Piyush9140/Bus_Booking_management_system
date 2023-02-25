from tkinter import *
from tkinter.messagebox import *
import mysql.connector as sql
from datetime import date
from tkinter import messagebox
from tkinter.messagebox import askyesno
mydb = sql.connect(
    host='localhost',
    user='root',
    passwd='Piyush@123',
    database = 'busbooking'
)

mycursor=mydb.cursor()

mycursor.execute("select * from passenger order by booking_ref desc")
ftabu=mycursor.fetchall()[0]
print(ftabu)
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=10)
Label(root,text='Online Bus Booking System',font="Arial 24 bold", bg='light blue',fg='red').grid(row=1,column=0,columnspan=10)
Label(root,text='Bus Ticket',font="Arial 15 bold",fg='black').grid(row=2,column=0,columnspan=10,pady=h//20)
final=LabelFrame(root)
final.grid(row=8,column=3,columnspan=3)
Label(final, text='Passenger:'+str(ftabu[0]),font='arial 8 bold').grid(row=8,column=0)
Label(final, text='No of Seats: '+str(ftabu[1]),font='arial 8 bold').grid(row=9,column=0)
Label(final, text='Age: '+str(ftabu[2]),font='arial 8 bold').grid(row=10,column=0)
Label(final, text='Booking Ref: '+str(ftabu[3]),font='arial 8 bold').grid(row=11,column=0)
Label(final, text='Travels on:'+str(ftabu[4]),font='arial 8 bold').grid(row=12,column=0)
Label(final, text='destination: '+str(ftabu[5]),font='arial 8 bold').grid(row=13,column=0)
Label(final, text='Gender: '+str(ftabu[6]),font='arial 8 bold').grid(row=8,column=1)
Label(final, text='Phone:'+str(ftabu[7]),font='arial 8 bold').grid(row=9,column=1)
Label(final, text='Fare Rs: '+str(ftabu[8]),font='arial 8 bold').grid(row=10,column=1)
Label(final, text='Bus details:'+str(ftabu[9]),font='arial 8 bold').grid(row=11,column=1)
Label(final, text='Booked On:'+str(ftabu[10]),font='arial 8 bold').grid(row=12,column=1)
Label(final, text='Boarding Point:'+str(ftabu[11]),font='arial 8 bold').grid(row=13,column=1)
Label(final, text='Total amount '+str(ftabu[8])+ ' to be paid at the time of boarding the bus: ',font='arial 8 italic ',fg='grey').grid(row=14,column=1)
showinfo('success','seat booked')
def on_closing():
    
    direct=askyesnocancel("closing","for closing click yes \n to go to main page click no")
    if direct==True:
        showinfo('Thanks','Thank you for using python bus service')
        root.destroy()
    elif direct==False:
        root.destroy()
        import page2
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()









