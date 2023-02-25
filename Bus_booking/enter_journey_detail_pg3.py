from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
from datetime import datetime
from tkinter.messagebox import askyesno
from datetime import date
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
Label(root,text='Enter Journey Details',font="Arial 13 bold", bg='light green',fg='green').grid(row=2,column=0,columnspan=25,pady=h//20)
Label(root,text='To',font="Arial 12 bold",fg='black').grid(row=3,column=7)
q=Entry(root)
q.grid(row=3,column=8)
Label(root,text='From',font="Arial 12 bold",fg='black').grid(row=3,column=9)
w=Entry(root)
w.grid(row=3,column=10)
Label(root,text='Journey Date',font="Arial 12 bold",fg='black').grid(row=3,column=11)
e=Entry(root)
e.grid(row=3,column=12)
choice=1
def digi(z):
    if(z=='1'):
        return 1
    if(z=='2'):
        return 2
    if(z=='3'):
        return 3
    if(z=='4'):
        return 4
    if(z=='5'):
        return 5
    if(z=='6'):
        return 6
    if(z=='7'):
        return 7
    if(z=='8'):
        return 8
    if(z=='9'):
        return 9
    if(z=='0'):
        return 0
def convert(s):
    num=0
    for i in s:
        num=num*10
        j=digi(i)
        num=num+j
    return num
def fun(counter):
    global choice
    choice=counter
'''if((len(q.get())==0)):
        messagebox.showerror('Error', 'Error: Cannot book more seats than available!')'''
    
def info():
    if((len(q.get())==0)|(len(w.get())==0)|(len(e.get())==0)):
        messagebox.showerror('Error', 'Error:Please enter required details')
    x=5
    a1=str(q.get())
    a2=str(w.get())
    a3=e.get()
    mycursor.execute("select * from bus B join running R on B.Bus_Id=R.Bs_ID")
    bd=mycursor.fetchall()
    print(bd[0][7])
    mycursor.execute("select * from route")
    rd=mycursor.fetchall()
    mycursor.execute("select * from operator")
    opd=mycursor.fetchall()
    v = StringVar(root, "1")
    counter = 0
    mp1={}
    d_obj = datetime.strptime(a3,'%Y-%m-%d').date()
    for i in rd:
        for j in rd:
            for k in bd:
                if((i[1]==a2 and j[1]==a1) and i[0]==j[0] and k[7]==d_obj and k[5]==i[0]):
                    for l in opd:
                        if(l[0]==k[4]):
                            op_name=l[1]
                    
                    disp=str(op_name)+"\t"+str(k[1])+"\t"+str(k[8])+"/"+str(k[2])+"\t"+str(k[3])
                    allinfo=(op_name,k[0],k[1],k[8],k[2],k[3])
                    counter=counter+1
                    mp1[counter]=allinfo
                    #mp1.update({counter:allinfo})

                    Radiobutton(root, text = ("bus"+str(counter)), variable = v,
                    value = counter, indicator = 0,
                    background = "light blue",command=fun(counter)).grid(row=x,column=7)

                    Label(root,text=disp,font="arial 15 bold").grid(row=x,column=10)
                    x=x+1
                    
    #pq=convert(v.get())
    global choice 
    restup=mp1[choice]
    Label(root,text='select bus',font="Arial 12 bold",fg='green').grid(row=4,column=7)
    Label(root,text='Operator',font="Arial 12 bold",fg='green').grid(row=4,column=8)
    Label(root,text='bus_type',font="Arial 12 bold",fg='green').grid(row=4,column=9)
    Label(root,text='Available/capacity',font="Arial 12 bold",fg='green').grid(row=4,column=10)
    Label(root,text='Fare',font="Arial 12 bold",fg='green').grid(row=4,column=11)
    #Button(root,text='Bus1',font="Arial 12 bold ",bg='dark green',fg='black').grid(row=5,column=7)
    Button(root,text='Proceed to book',command=lambda:info1(restup,a1,a2,d_obj),font="Arial 12 bold ",bg='dark green',fg='black').grid(row=5,column=13)
def info1(restup,a1,a2,d_obj):
    Label(root,text='Fill Passenger Details To book the bus ticket',font="Arial 20 bold", bg='light blue',fg='red').grid(row=7,column=5,columnspan=30,pady=100)
    Label(root,text='Name',font="Arial 12 bold",fg='black').grid(row=8,column=0)
    a=Entry(root)
    a.grid(row=8,column=2)
    Label(root,text='Gender',font="Arial 12 bold",fg='black').grid(row=8,column=4)
    Gender=StringVar()
    Gender.set('Male')
    option=['Male','Female','Third Gender']
    d_menu=OptionMenu(root,Gender, * option)
    d_menu.grid(row=8,column=6)
    Label(root,text='No of seats',font="Arial 12 bold",fg='black').grid(row=8,column=8)
    b=Entry(root)
    b.grid(row=8,column=9)
    Label(root,text='Mobile No',font="Arial 12 bold",fg='black').grid(row=8,column=10)
    c=Entry(root)
    c.grid(row=8,column=11)
    Label(root,text='Age',font="Arial 12 bold",fg='black').grid(row=8,column=12)
    d=Entry(root)
    d.grid(row=8,column=13)
    Button(root,text='Book seat',command=lambda:add(a,Gender,b,c,d,restup,a1,a2,d_obj),font="Arial 12 bold ",bg='dark green',fg='black').grid(row=8,column=15)
def add(a,Gender,b,c,d,restup,a1,a2,d_obj):
    if((len(a.get())==0)|(len(b.get())==0)|(len(c.get())==0)|(len(d.get())==0)):
        messagebox.showerror('Error', 'Error:Please enter required details')
    if(int(b.get())>restup[3]):
        messagebox.showerror('Error', 'Error: Cannot book more seats than available!')
        return
    inp1=a.get()
    inp2=Gender.get()
    inp3=int(b.get())
    inp4=int(c.get())
    inp5=int(d.get())
    ttf=inp3*restup[5]
    answer = askyesno(title='Fare confirm',
                    message='Total amount to be paid is '+str(ttf))
    if answer:
        s="insert into passenger values(%s,%s,%s,booking_ref,%s,%s,%s,%s,%s,%s,%s,%s)"
        tup=(inp1,inp3,inp5,d_obj,a1,inp2,inp4,ttf,restup[0],date.today(),a2)
        mycursor.execute(s,tup)
        mydb.commit()
        q2="update running set seat_avl=%s where Bs_Id=%s AND Rn_dt=%s"
        fn=restup[3]-inp3
        t2=(fn,restup[1],d_obj)
        mycursor.execute(q2,t2)
        mydb.commit()
        print('success')
        root.destroy()
        import bus_ticket_pg4
def change():
    root.destroy()
    import page2    
Button(root,text='Show Bus',command=info,font="Arial 12 bold ",bg='dark green',fg='black').grid(row=3,column=13)
home=PhotoImage(file='.\\home.png')
Button(root,image=home,command=change).grid(row=3,column=14)
#Label(root,text='Project based Learning',font="Arial 16 bold", fg='red').grid(row=6,column=0)
