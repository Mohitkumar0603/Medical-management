from cgitb import text
#from curses.textpad import Textbox
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import *
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from admin_db import *
from user_login import *
from admin_login import *
import os
import PIL.Image
import customtkinter

root = Tk()
root.title('HUMAN ILL HEALTH DETECTION')
root.resizable(True, True)
root.geometry('1500x750')
root.configure(bg='ghost white')
#root.wm_attributes('-transparentcolor', '#ab23ff')

titleframe = LabelFrame(root)
titleframe.grid(row=0,column=0)

image=PIL.Image.open("home.jpg")

img=image.resize((1400, 600))
my_img=ImageTk.PhotoImage(img,master=root)
            # Show image using label
label1 = Label( root, image = my_img)
label1.image = my_img
label1.place(x = 0, y = 100)


image=PIL.Image.open("image2.png")

img=image.resize((100, 70))
my_img=ImageTk.PhotoImage(img,master=root)
            # Show image using label
label1 = Label( root, image = my_img,bg='ghost white')
label1.image = my_img
label1.place(x = 40, y = 19)

f= ("Farrah", 25, "bold")
label1 = Label( root, text="WELCOME TO HUMAN ILL HEALTH DETECTION SYSTEM ",font=f,bg="ghost white",fg="red")
label1.place(x = 300, y = 10)

f= ("Times", 15, "bold")
label1 = Label( root, text="",font=f,bg="ghost white")
label1.place(x = 340, y =60)
def user():
     user_login(root)
def admin():
    adminlogin(root)


b= ("Decary Sans", 18, "bold")


open_button = Button(root,text='USER',command=user,bd=0,bg="ghost white",font=b,fg='dark blue')
open_button.place(x=1100,y=50)

open_button = Button(root,text='ADMIN',command=admin,bd=0,bg="ghost white",font=b,fg='dark blue')
open_button.place(x=1200,y=50)


root.mainloop()
