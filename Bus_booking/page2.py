from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=10)
Label(root,text='Online Bus Booking System',font="Arial 24 bold", bg='light blue',fg='red').grid(row=1,column=0,columnspan=10)
def change():
    root.destroy()
    import enter_journey_detail_pg3
def change1():
    root.destroy()
    import check_booking_page5
def change2():
    root.destroy()
    import add_new_data_page6
Button(root,text='Seat booking',command=change,font="Arial 18 bold", bg='light green',fg='black').grid(row=2,column=2,padx=20,pady=50)
Button(root,text='Check Booked seat',command=change1,font="Arial 18 bold", bg='green',fg='black').grid(row=2,column=4,padx=30,pady=50)
Button(root,text='Add bus details',command=change2,font="Arial 18 bold", bg='dark green',fg='black').grid(row=2,column=6,padx=50,pady=50)
Label(root,text='For Admin Only',font="Arial 15 ",fg='red').grid(row=3,column=6)
#Label(root,text='Project based Learning',font="Arial 16 bold", fg='red').grid(row=6,column=0)
