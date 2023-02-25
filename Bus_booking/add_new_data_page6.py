from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=25)
Label(root,text='Online Bus Booking System',font="Arial 24 bold", bg='light blue',fg='red').grid(row=1,column=0,columnspan=25)
Label(root,text='Add New Details To Database',font="Arial 16 bold",fg='green').grid(row=2,column=0,columnspan=25,pady=h//20)
def change():
    root.destroy()
    import add_operator_data_page7
def change1():
    root.destroy()
    import add_bus_data_page8
def change2():
    root.destroy()
    import add_route_page9
def change3():
    root.destroy()
    import add_bus_Runnig_details_page10
Button(root,text='New Operator',command=change,font="Arial 12 bold",bg='light green',fg='black').grid(row=3,column=8)
Button(root,text='New Bus',command=change1,font="Arial 12 bold",bg='orange',fg='black').grid(row=3,column=11)
Button(root,text='New Route',command=change2,font="Arial 12 bold",bg='blue',fg='black').grid(row=3,column=14)
Button(root,text='New Run',command=change3,font="Arial 12 bold ",bg='purple',fg='black').grid(row=3,column=17)
#Label(root,text='Project based Learning',font="Arial 16 bold", fg='red').grid(row=6,column=0)
