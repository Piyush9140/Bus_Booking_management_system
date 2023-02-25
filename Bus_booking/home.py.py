from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.state('zoomed')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=w//2.5)
Label(root,text='Online Bus Booking System',font="Arial 24 bold", bg='light blue',fg='red').grid(row=1,column=0)
Label(root,text='Name: Piyush agarwal',font="Arial 14 bold", fg='blue').grid(row=2,column=0,pady=h//20)
Label(root,text='Er: 211b206',font="Arial 14 bold", fg='blue').grid(row=3,column=0,pady=h//80)
Label(root,text='Mobile: 9140282979',font="Arial 14 bold", fg='blue').grid(row=4,column=0,pady=h//20)
Label(root,text='Submitted to: Dr. Mahesh kumar And Dr Neelesh Patel',font="Arial 18 bold", bg='light blue',fg='red').grid(row=5,column=0)
Label(root,text='Project based Learning',font="Arial 16 bold", fg='red').grid(row=6,column=0)
def change():
    root.destroy()
    import page2
Button(root, text='NEXT', command=change).place(x=700,y=700)
