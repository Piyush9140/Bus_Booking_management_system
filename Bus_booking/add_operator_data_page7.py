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
Label(root,text='Add Bus Operator Details',font="Arial 18 bold",fg='green').grid(row=2,column=0,columnspan=25,pady=h//20)
Label(root,text='Operator Id',font="Arial 12 bold",fg='black').grid(row=3,column=5)
a=Entry(root)
a.grid(row=3,column=6)
Label(root,text='Name',font="Arial 12 bold",fg='black').grid(row=3,column=7)
b=Entry(root)
b.grid(row=3,column=8)
Label(root,text='Address',font="Arial 12 bold",fg='black').grid(row=3,column=9)
c=Entry(root)
c.grid(row=3,column=10)
Label(root,text='Phone',font="Arial 12 bold",fg='black').grid(row=3,column=11)
d=Entry(root)
d.grid(row=3,column=12)
Label(root,text='Email',font="Arial 12 bold",fg='black').grid(row=3,column=13)
e=Entry(root)
e.grid(row=3,column=14)
z=0
def add():
    if((len(a.get())==0)|(len(b.get())==0)|(len(c.get())==0)|(len(d.get())==0)|(len(e.get())==0)):
        messagebox.showerror('Error', 'Error:Please enter required details')
    z=0
    inp1=int(a.get())
    inp2=b.get()
    inp3=c.get()
    inp4=int(d.get())
    inp5=e.get()
    s="insert into operator values(%s,%s,%s,%s,%s)"
    tup=(inp1,inp2,inp3,inp4,inp5)
    z=z+1

    mycursor.execute(s,tup)
    mydb.commit()
    print("Addition successful")
    if z>0:
        showinfo('operator','record added')
def edit():
    if((len(a.get())==0)|(len(b.get())==0)|(len(c.get())==0)|(len(d.get())==0)|(len(e.get())==0)):
        messagebox.showerror('Error', 'Error:Please enter required details')
    z=0
    inp1=int(a.get())
    inp2=b.get()
    inp3=c.get()
    inp4=int(d.get())
    inp5=e.get()
    s="update operator set Name=%s,Address=%s,Phone_no=%s,email=%s where OP_Id=%s"
    tup=(inp2,inp3,inp4,inp5,inp1)
    z=z+1

    mycursor.execute(s,tup)
    mydb.commit()
    print("Updated successful")
    if z>0:
        showinfo('Operator','record edited')
def change():
    root.destroy()
    import page2
Button(root,text='Add',command=add,font="Arial 12 bold ",bg='light green',fg='black').grid(row=3,column=15)
Button(root,text='Edit',command=edit,font="Arial 12 bold ",bg='light green',fg='black').grid(row=3,column=16)
home=PhotoImage(file='.\\home.png')
Button(root,image=home,command=change).grid(row=5,column=13,pady=h//10)

