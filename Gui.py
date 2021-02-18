"""
============
GUI TKINTER ||
============
"""

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

# SETTING ALL VALUES TO NULL
roll = None
validity = None


#  ==================================================================================================

# DISPLAYING THE FIRST LEVEL AUTHENTICATION FRAME
def rollNo():
    # CALLING THE QRCODE AUTHENTICATION FUNCTION
    validity, rollNo = QRcodeAuthentication()

    global roll
    roll = rollNo

    if validity:

        heading_label['text'] = 'Second Level Authentication'
        button1.place(relx=0.25, rely=0.33, relheight=0.33, relwidth=0.5)

    else:
        # SHOWING ERROR DIALOGUE BOX AND FAILURE MESSGAE
        messagebox.showerror("disclaimer", "please try again!!")
        label['text'] = 'not authenticated'
        label.place(relx=0.25, rely=0.33, relheight=0.33, relwidth=0.5)


# os.startfile("main.py")


# ======================================================================================================

# 2ND LEVEL AUTHENTICATION FRAME
def authentication():
    # CALLS FACE_RECOGNITION FUNCTION AND IF TRUE PRINTS BELOW MESSAGE
    if authenticate(roll[-3:]):
        attendance(roll, True)
        label['text'] = 'Attendance is marked'
        label.place(relx=0.2, rely=0.33, relheight=0.33, relwidth=0.6)

    # IF FALSE DISCLAIMER BOX GETS CREATED AND PRINTS BELOW MESSAGE
    else:
        messagebox.showerror("disclaimer", "please try again!!")
        label['text'] = 'not authenticated'
        label.place(relx=0.2, rely=0.33, relheight=0.33, relwidth=0.6)
    # restart()
    sleep(2)


# =========================================================================================================

# LOGIN PAGE FOR THE LOGIN FRAME
def LoginPage():
    # ============================================================================
    # IF AUTHENTICATED , ADMIN FRAME IS POPPED ON TOP LEVEL
    def access():

        # CHECKING THE GIVEN USERNAME AND PASSWORD
        # IF TRUE ADMIN FRAME IS CREATED
        if (username_login_entry.get() == "admin" and password__login_entry.get() == "password"):
            access_screen = tk.Toplevel(root)
            access_screen.title("admin page")
            access_screen.geometry("400x400")

            # THIS PIECE OF CODE DISPLAYS ALL THE MEMBERS WHO GAVE ATTENDACE IN ADMIN PAGE IN A TABLE
            file_name = (str(datetime.datetime.now()).split())[0] + ".csv"
            with open(file_name, newline="") as file:
                reader = csv.reader(file)
                r = 0
                for col in reader:
                    c = 0
                    for row in col:
                        label = tk.Label(access_screen, width=10, height=2, text=row, relief=tk.RIDGE)
                        label.place(relx=0.1 + (c * 0.4), rely=r * 0.1, relheight=0.1, relwidth=0.4)
                        c += 1
                    r += 1

        # IF FALSE ERROR WINDOW IS POPPED OUT
        else:
            messagebox.showerror("disclaimer", "enter correct password")

    # ===========================================================================

    # LOGIN PAGE FRAME CODE
    login_screen = tk.Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.configure(bg="khaki")
    tk.Label(login_screen, text="Please enter login details", bg="snow").pack()
    tk.Label(login_screen, text="", bg="khaki").pack()
    tk.Label(login_screen, text="Username *", bg="snow").pack()
    username_login_entry = tk.Entry(login_screen, textvariable="username")
    username_login_entry.pack()
    tk.Label(login_screen, text="", bg="khaki").pack()
    tk.Label(login_screen, text="Password *", bg="snow").pack()
    password__login_entry = tk.Entry(login_screen, textvariable="password", show='*')
    password__login_entry.pack()
    tk.Label(login_screen, text="", bg="khaki").pack()
    tk.Button(login_screen, text="Login", width=10, height=1, command=access, activebackground="aquamarine").pack()

    login_screen.mainloop()


# ===================================================================================================================

# TRY AGAIN FUNCTION
# UNDER DEVELOPMENT
def try_again():
    canvas.pack()
    # os.destroy()
    os.startfile("Gui.py")


#  ====================================================================================================================

"""
================================
MAIN FRAME STARTS FROM HERE!!!!
================================
"""
# SETTING UP THE HEIGHT AND WINDOW OF FRAME
# YOU CAN CUSTOMISE YOURS!!!
h = 484
w = 1029

root = tk.Tk()

# SETTING UP TH FONT
fontStyle = tkFont.Font(family="Helvetica", size=20)

# WINDOW TITLE
root.title("ATTENDANCE")

# ICON OF THE WINDOW
root.iconbitmap("discussion.ico")

"""
===============
MENU BAR FRAME ||
===============
"""
# ================================
menu = Menu(root)
new_item = Menu(menu)

# ADDING AN ITEM IN MENU BAR FRAME (LOGIN BUTTON FRAME)
new_item.add_command(label="login", command=LoginPage)
new_item.add_separator()

# MENU BAR HEADING FRAME
menu.add_cascade(label="options", menu=new_item)
root.config(menu=menu)
# ================================


canvas = tk.Canvas(root, height=h, width=w, bg="snow")
canvas.pack()

# HEADING LABEL
heading_label = tk.Label(root, text="First Level Authentication", font=('courier', 32,), bg='snow')
heading_label.place(relx=0.1, relheight=.3, relwidth=.8)

# FRAME CODE
frame = tk.Frame(root, bg='khaki', bd=5)
frame.place(relx=0, rely=0.3, relwidth=1.0, relheight=0.35)

# BUTTON FRAME (PRESS TO PLACE ID)
button = tk.Button(frame, text='press to place id card', command=rollNo, font=fontStyle,
                   activebackground="khaki")  # .command=shirish_function
button.place(relx=0.33, rely=0.33, relheight=0.33, relwidth=0.33)

"""
button0=tk.Button(frame,text='Go back',command=try_again,font=fontStyle,activebackground="khaki")
button0.place(relx=0.33,rely=0.75,relheight=0.25,relwidth=0.33)
"""

# BUTTON FRAME (PRESS TO PLACE YOUR FACE)
button1 = tk.Button(frame, text='press to place your face', command=authentication, font=fontStyle)
label = tk.Label(frame, text="", font=('courier', 20))

root.mainloop()
