import csv
import datetime
import os
import tkinter as tk
import tkinter.font as tkFont
from time import sleep
from tkinter import Menu
from tkinter import messagebox

from QRcodeAuthentication import QRcodeAuthentication
from attendance import attendance
from authenticatePic import authenticate

def show_frame(frame):
    frame.tkraise()

#global flag_qr
flag_qr=0
flag_auth=0
roll=''
def qrcode():
    global roll
    validity,roll=QRcodeAuthentication()
    if validity:
        global flag_qr
        title=tk.Label(frame[1],text="Student Id  verified",font=('Helvetica',12),bg='snow',fg='green')
        title.place(x=0,y=180)
        #global flag_qr
        flag_qr=1
    else:
        title=tk.Label(frame[1],text="Place correct Qr code",font=('Helvetica',12),bg='#455357',fg='red')
        title.place(x=0,y=180)
    frame[1].after(5000,title.destroy)

def authentication():
    if authenticate(roll[-3:]):
        title=tk.Label(frame[1],text="Face Id verified",font=('Helvetica',12),bg='snow',fg='green')
        title.place(x=0,y=270)
        global flag_auth
        flag_auth=1
    else:
        title=tk.Label(frame[1],text="Try entering face again",font=('Helvetica',12),bg='#455357',fg='red')
        title.place(x=0,y=270)
    frame[1].after(5000,title.destroy)

def submit():
    global flag_qr
    global flag_auth
    if flag_qr  and flag_auth:
        flag_qr=0
        flag_auth=0
        attendance(roll,True)
        title=tk.Label(frame[1],text="Attendance marked Successfully",font=('Helvetica',12),bg='snow',fg='green')
        title.place(x=0,y=500)
        messagebox.showinfo("sucessful","marked sucessfully!!")
        show_frame(frame[0])
    else:
        messagebox.showerror("disclaimer", "please try again!!")
        title=tk.Label(frame[1],text="Try entering again",font=('Helvetica',12),bg='#455357',fg='red')
        title.place(x=0,y=500)
        #show_frame(frame[0])
    frame[1].after(5000,title.destroy)

def access1():
    if (username_login_entry.get() == "admin" and password_login_entry.get() == "password"):
        show_frame(frame[3])
    elif (username_login_entry.get() == "" and password_login_entry.get() == ""):
        messagebox.showerror("warning","enter details and submit bro")
    else:
        messagebox.showerror("disclaimer", "INCORRECT PASSWORD \nplease try again!!")




window=tk.Tk()
window.title("attendance")
window.geometry('450x640')
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
window.iconbitmap("discussion.ico")
frame=[tk.Frame(window,bg='#455357') for i in range(6)]
fontStyle=('Helvetica',15)
Bg='#DBD64E'
Fg='white'

for i in frame:
    i.grid(row=0,column=0,sticky='nsew')
    title=tk.Label(i,text="FUTURE TECHNOLOGY SOLUTIONS",font=fontStyle,bg=Bg,fg="black")
    title.pack(fill='x')

frame0_btn=tk.Button(frame[0],text='Enter attendance',font=fontStyle,height=2,width=15,command=lambda:show_frame(frame[1]))
frame0_btn.place(x=120,y=220)
frame0_btn=tk.Button(frame[0],text='Admin login',font=fontStyle,height=2,width=15,command=lambda:show_frame(frame[2]))
frame0_btn.place(x=120,y=400)

title=tk.Label(frame[1],text="Id Card Authentication",font=fontStyle,bg=Bg,fg=Fg)
title.place(x=0,y=70)


frame1_btn=tk.Button(frame[1],text='click to place\n id card',font=fontStyle,height=2,width=15,command=qrcode)
frame1_btn.place(x=120,y=120)

title=tk.Label(frame[1],text="Face Recoginization",font=fontStyle,bg=Bg,fg=Fg)
title.place(x=0,y=220)

frame1_btn=tk.Button(frame[1],text='click here to enter \nfacial data',font=fontStyle,height=2,width=15,command=authentication)
frame1_btn.place(x=120,y=260)

frame1_btn=tk.Button(frame[1],text="Submit",font=fontStyle,height=2,width=15,command=submit)
frame1_btn.place(x=120,y=400)

frame1_btn=tk.Button(frame[1],text="Back to home",font=fontStyle,height=2,width=15,command=lambda:show_frame(frame[0]))
frame1_btn.place(x=120,y=550)




login=tk.Label(frame[2],text="login",font=fontStyle,bg=Bg,fg=Fg,height=2,width=15)
login.place(x=130,y=90)

username_label = tk.Label(frame[2], text="Username *", bg="snow",height=2,width=10)
username_label.place(x=180,y=155)

username_login_entry = tk.Entry(frame[2], textvariable="username")
username_login_entry.place(x=160,y=200)

password_label = tk.Label(frame[2], text="Password *", bg="snow",height=2,width=10)
password_label.place(x=180,y=230)

password_login_entry = tk.Entry(frame[2], textvariable="password",show="*")
password_login_entry.place(x=160,y=275)

login_btn=tk.Button(frame[2], text="Login", width=10, height=1,command=access1)
login_btn.place(x=180,y=320)

home_btn=tk.Button(frame[2],text="Back to home",font=fontStyle,height=1,width=12,command=lambda:show_frame(frame[0]))
home_btn.place(x=150,y=400)



frame3_btn=tk.Button(frame[3],text="add user",font=fontStyle,height=1,width=12)
frame3_btn.place(x=150,y=90)

frame3_btn1=tk.Button(frame[3],text="delete user",font=fontStyle,height=1,width=12)
frame3_btn1.place(x=150,y=160)

frame3_btn2=tk.Button(frame[3],text="view attendance",font=('Helvetica',14),height=1,width=12,command=lambda:show_frame(frame[4]))
frame3_btn2.place(x=150,y=230)

frame3_btn3=tk.Button(frame[3],text="Back to home",font=fontStyle,height=1,width=12,command=lambda:show_frame(frame[0]))
frame3_btn3.place(x=150,y=310)

#frame 4
file_name = (str(datetime.datetime.now()).split())[0] + ".csv"
with open(file_name, newline="") as file:
    reader = csv.reader(file)
    r = 1.5
    for col in reader:
        c = 0
        for row in col:
            label = tk.Label(frame[4], width=10, height=2, text=row, relief=tk.RIDGE)
            label.place(relx=0.1 + (c * 0.4), rely=r * 0.1, relheight=0.1, relwidth=0.4)
            c += 1
        r += 1
frame4_btn=tk.Button(frame[4],text="Back",font=fontStyle,height=0,width=15,command=lambda:show_frame(frame[3]))
frame4_btn.place(x=120,y=45)




show_frame(frame[0])
#frame1.pack()

window.mainloop()
