import tkinter as tk
from time import sleep
from authenticatePic import authenticate
from attendance import attendance
from QRcodeAuthentication import QRcodeAuthentication
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import Menu
import os
import pandas
import datetime
import csv
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
        title=tk.Label(frame[1],text="Student Id  verified",font=('Helvetica',12),bg='#455357',fg='white')
        title.place(x=0,y=180)
        #global flag_qr
        flag_qr=1
    else:
        title=tk.Label(frame[1],text="Place correct Qr code",font=('Helvetica',12),bg='#455357',fg='white')
        title.place(x=0,y=180)
    frame[1].after(5000,title.destroy)

def authentication():
    if authenticate(roll[-3:]):
        title=tk.Label(frame[1],text="Face Id verified",font=('Helvetica',12),bg='#455357',fg='white')
        title.place(x=0,y=270)
        global flag_auth
        flag_auth=1
    else:
        title=tk.Label(frame[1],text="Try entering face again",font=('Helvetica',12),bg='#455357',fg='white')
        title.place(x=0,y=270)
    frame[1].after(5000,title.destroy)

def submit():
    if flag_qr  and flag_auth:
        attendance(roll,True)
        title=tk.Label(frame[1],text="Attendance marked Successfully",font=('Helvetica',12),bg='#455357',fg='white')
        title.place(x=0,y=500)
    else:
        title=tk.Label(frame[1],text="Try entering again",font=('Helvetica',12),bg='#455357',fg='white')
        title.place(x=0,y=500)
        show_frame(frame[0])
    frame[1].after(5000,title.destroy)



window=tk.Tk()
window.title("attendance")
window.geometry('450x640')
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
frame=[tk.Frame(window,bg='#455357') for i in range(6)]
fontStyle=('Helvetica',15)
Bg='#DBD64E'
Fg='white'

for i in frame:
    i.grid(row=0,column=0,sticky='nsew')
    title=tk.Label(i,text="MVSR Engineering College",font=fontStyle,bg=Bg,fg=Fg)
    title.pack(fill='x')

frame1_btn=tk.Button(frame[0],text='Enter attendance',font=fontStyle,height=2,width=15,command=lambda:show_frame(frame[1]))
frame1_btn.place(x=120,y=220)
frame1_btn=tk.Button(frame[0],text='Admin login',font=fontStyle,height=2,width=15)
frame1_btn.place(x=120,y=400)

title=tk.Label(frame[1],text="Id Card Authentication",font=fontStyle,bg=Bg,fg=Fg)
title.place(x=0,y=70)


frame2_btn=tk.Button(frame[1],text='click to place\n id card',font=fontStyle,height=2,width=15,command=qrcode)
frame2_btn.place(x=120,y=120)

title=tk.Label(frame[1],text="Face Recoginization",font=fontStyle,bg=Bg,fg=Fg)
title.place(x=0,y=220)

frame2_btn=tk.Button(frame[1],text='click here to enter \nfacial data',font=fontStyle,height=2,width=15,command=authentication)
frame2_btn.place(x=120,y=260)

frame2_btn=tk.Button(frame[1],text="Submit",font=fontStyle,height=2,width=15,command=submit)
frame2_btn.place(x=120,y=400)

frame2_btn=tk.Button(frame[1],text="Back to home",font=fontStyle,height=2,width=15,command=lambda:show_frame(frame[0]))
frame2_btn.place(x=120,y=550)

show_frame(frame[0])


#frame1.pack()

window.mainloop()
