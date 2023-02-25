from tkinter import *
import mysql.connector as sql
from tkinter.messagebox import *
from tkinter import messagebox
mydb=sql.connect(
    host='localhost',
    user='root',
    passwd='Piyush@123',
    database='busbooking'
)
mycursor=mydb.cursor()
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=25)
Label(root,text='Online Bus Booking System',font="Arial 24 bold", bg='light blue',fg='red').grid(row=1,column=0,columnspan=25)
Label(root,text='Add Bus Running Details',font="Arial 18 bold",fg='green').grid(row=2,column=0,columnspan=25,pady=h//20)
Label(root,text='Bus Id',font="Arial 12 bold",fg='black').grid(row=3,column=5)
a=Entry(root)
a.grid(row=3,column=6)
Label(root,text='Runnig Date',font="Arial 12 bold",fg='black').grid(row=3,column=7)
b=Entry(root)
b.grid(row=3,column=8)
Label(root,text='Seat Available',font="Arial 12 bold",fg='black').grid(row=3,column=9)
c=Entry(root)
c.grid(row=3,column=10)
z=0
def add():
    if((len(a.get())==0)|(len(b.get())==0)|(len(c.get())==0)):
        messagebox.showerror('Error', 'Error:Please enter required details')
    z=0
    inp1=int(a.get())
    inp2=b.get()
    inp3=int(c.get())
    #inp4=int(d.get())
    #inp5=e.get()
    s="insert into running values(%s,%s,%s)"
    tup=(inp1,inp2,inp3)
    z=z+1

    mycursor.execute(s,tup)
    mydb.commit()
    print("Addition successful")
    if z>0:
        showinfo('Run','record added')
def dlt():
    if((len(a.get())==0)|(len(b.get())==0)|(len(c.get())==0)):
        messagebox.showerror('Error', 'Error:Please enter required details')
    z=0
    inp1=int(a.get())
    s="delete from running where Bs_ID=%s"
    tup=(inp1,)
    z=z+1
    mycursor.execute(s,tup)
    mydb.commit()
    print("deleted successful")
    if z>0:
        showinfo('Run','record deleted')
def change():
    root.destroy()
    import page2
Button(root,text='Add Run',command=add,font="Arial 12 bold ",bg='light green',fg='black').grid(row=3,column=11)
Button(root,text='Delete Run',command=dlt,font="Arial 12 bold ",bg='light green',fg='black').grid(row=3,column=12)
home=PhotoImage(file='.\\home.png')
Button(root,image=home,command=change).grid(row=5,column=11,pady=h//10)

