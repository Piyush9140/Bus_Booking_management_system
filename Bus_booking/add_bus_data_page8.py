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
Label(root,text='Add Bus Details',font="Arial 18 bold",fg='green').grid(row=2,column=0,columnspan=25,pady=h//20)
Label(root,text='Bus Id',font="Arial 12 bold",fg='black').grid(row=3,column=5)
a=Entry(root)
a.grid(row=3,column=6)
Bus_type=StringVar()
Bus_type.set('select')
option=['2x2','3x2','AC 2x2','AC 3x2']
d_menu=OptionMenu(root,Bus_type, * option)
d_menu.grid(row=3,column=8)
Label(root,text='Bus Type',font="Arial 12 bold",fg='black').grid(row=3,column=7)
#Entry(root).grid(row=3,column=8)
Label(root,text='Capacity',font="Arial 12 bold",fg='black').grid(row=3,column=9)
b=Entry(root)
b.grid(row=3,column=10)
Label(root,text='Fare Rs',font="Arial 12 bold",fg='black').grid(row=3,column=11)
c=Entry(root)
c.grid(row=3,column=12)
Label(root,text='Operator Id',font="Arial 12 bold",fg='black').grid(row=3,column=13)
d=Entry(root)
d.grid(row=3,column=14)
Label(root,text='Route Id',font="Arial 12 bold ",fg='black').grid(row=3,column=15)
e=Entry(root)
e.grid(row=3,column=16)
f=0
def add():
    if((len(a.get())==0)|(len(b.get())==0)|(len(c.get())==0)|(len(d.get())==0)|(len(e.get())==0)):
        messagebox.showerror('Error', 'Error:Please enter required details')
    f=0
    inp1=int(a.get())
    inp2=Bus_type.get()
    inp3=int(b.get())
    inp4=int(c.get())
    inp5=int(d.get())
    inp6=int(e.get())
    s="insert into bus values(%s,%s,%s,%s,%s,%s)"
    tup=(inp1,inp2,inp3,inp4,inp5,inp6)
    mycursor.execute(s,tup)
    f=f+1
    mydb.commit()
    print('success')
    if f>0:
        showinfo('Bus Entry','Bus record added')
def edit():
    if((len(a.get())==0)|(len(b.get())==0)|(len(c.get())==0)|(len(d.get())==0)|(len(e.get())==0)):
        messagebox.showerror('Error', 'Error:Please enter required details')
    f=0
    inp1=int(a.get())
    inp2=Bus_type.get()
    inp3=int(b.get())
    inp4=int(c.get())
    inp5=int(d.get())
    inp6=int(e.get())
    s="update bus set Bus_type=%s,capacity=%s,Fare=%s,Opr_ID=%s,Route_ID=%s where Bus_Id=%s"
    tup=(inp2,inp3,inp4,inp5,inp6,inp1)
    f=f+1

    mycursor.execute(s,tup)
    mydb.commit()
    print("Updated successful")
    if f>0:
        showinfo('Bus Entry','Bus record edited')
def change():
    root.destroy()
    import page2
Button(root,text='Add Bus',command=add,font="Arial 12 bold ",bg='light green',fg='black').grid(row=4,column=11,pady=h//10)
Button(root,text='Edit Bus',command=edit,font="Arial 12 bold ",bg='light green',fg='black').grid(row=4,column=12,pady=h//10)
home=PhotoImage(file='.\\home.png')
Button(root,image=home,command=change).grid(row=4,column=13,pady=h//10)
#Label(root,text='Project based Learning',font="Arial 16 bold", fg='red').grid(row=6,column=0)
