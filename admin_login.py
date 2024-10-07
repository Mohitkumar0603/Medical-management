# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:20:43 2023

@author: dell
"""

import tkinter
from tkinter import *
from tkinter import messagebox
from medical2 import *
from user_database import *
from admin import *

##window = tkinter.Tk()
##window.title("HUMAN ILL HEALTH DETECTION")
##window.geometry('1166x718')
###window.resizable(0, 0)
##window.state('zoomed')
##window.configure(bg='ghost white')
def adminlogin(window):
    titleframe = LabelFrame(window,width="1500",height="750",bg="ghost white")
    titleframe.grid(row=0,column=0)
    image=PIL.Image.open("4.jpg")

    img=image.resize((1400, 800))
    my_img=ImageTk.PhotoImage(img,master=titleframe)
                # Show image using label
    label1 = Label(titleframe, image = my_img)
    label1.image = my_img
    label1.place(x = 0, y = 0)





    def login():
        if username_entry.get()=="admin" and password_entry.get()=="admin@111":
            admin_page(titleframe)
            clear()
               
                
                    
            
                
    
    def clear():
        username_entry.delete(first=0,last=100)
        password_entry.delete(first=0,last=100)
    def back():
        titleframe.destroy()
    frame = Frame(titleframe, bg='Ivory', width=770, height=600,highlightbackground="gray", highlightthickness=2)
    frame.place(x=450, y=100)
    image=PIL.Image.open("login.png")



    img=image.resize((350, 450))
    my_img=ImageTk.PhotoImage(img,master=frame)
                # Show image using label
    label1 = Label(frame, image = my_img,bd=0)
    label1.image = my_img
    label1.place(x = 0, y = 100)

    # Creating widgets
    login_label = tkinter.Label(
        frame, text="Welcome!", bg='Ivory', fg="red", font=("Franklin Gothic Heavy", 40))
    username_label = tkinter.Label(frame, text="Username", bg='Ivory', fg="black", font=("Arial", 16))
    username_entry = tkinter.Entry(frame, font=("Arial", 16))
    password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    password_label = tkinter.Label(
        frame, text="Password", bg='Ivory', fg="black", font=("Arial", 16))

    image4=PIL.Image.open("signin.png")
    img4=image4.resize((100, 52))
    my_img=ImageTk.PhotoImage(img4,master=frame)
    login_button = tkinter.Button(
        frame, image=my_img, bg="Ivory", font=("Arial", 19), bd=0,command=login)
    login_button.image=my_img
    # Placing widgets on the screen
    login_label.place(x=400, y=10)
    username_label.place(x=350, y=200)
    username_entry.place(x=500, y=200)
    password_label.place(x=350, y=300)
    password_entry.place(x=500, y=300)
    login_button.place(x=450, y=400)


    

    login_button = tkinter.Button(
        frame, text="BACK", bg="red",fg="white", font=("Arial", 19), bd=0,command=back)
    login_button.place(x=550, y=400)



