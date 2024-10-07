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
import os
import PIL.Image


#root.wm_attributes('-transparentcolor', '#ab23ff')
def admin_page(root):
    titleframe = LabelFrame(root,width="1500",height="750",bg="ghost white")
    titleframe.grid(row=0,column=0)

    image=PIL.Image.open("admin.jpg")

    img=image.resize((1500, 600))
    my_img=ImageTk.PhotoImage(img)
                # Show image using label
    label1 = Label( titleframe, image = my_img)
    label1.image = my_img
    label1.place(x = 0, y = 100)


    image=PIL.Image.open("image2.png")

    img=image.resize((100, 70))
    my_img=ImageTk.PhotoImage(img)
                # Show image using label
    label1 = Label( titleframe, image = my_img,bg='ghost white')
    label1.image = my_img
    label1.place(x = 70, y = 19)

    f= ("Farrah", 35, "bold") #"Farrah"
    label1 = Label( titleframe, text="ADMIN PORTAL",font=f,bg="ghost white",fg="red")
    label1.place(x = 350, y = 15)

    f= ("Times", 15, "bold")
    label1 = Label( titleframe, text="",font=f,bg="ghost white")
    label1.place(x = 340, y =60)
    
        
    def medicine():
        lgn_frame1 = Frame(titleframe, bg='Ivory', width=1390, height=900,highlightbackground="gray", highlightthickness=2)
        lgn_frame1.place(x=1, y=100)
        Name=StringVar()
        Name2=StringVar()
        def medicineadd():
            medicine_db(NameEn.get(),NameEn1.get())
            messagebox.showinfo("Success","Successfully medicines data added to database")

        
        def Reset():
            NameEn.delete(first=0,last=100)
            NameEn1.delete(first=0,last=100)
            
        from tkinter import messagebox
        def Exit():
            qExit=messagebox.askyesno("System","Do you want to exit the system")
            
            if qExit:
                lgn_frame1.destroy()
                
        #Headings for the GUI written at the top of GUI
        w2 = Label(lgn_frame1, justify=LEFT, text="Disease and their medicines Database", fg="Red", bg="Ivory")
        w2.config(font=("Arial",20,"bold italic"))
        w2.place(x=480,y=10)
        

        #Label for the name
        NameLb = Label(lgn_frame1, text="Name of the Disease*", fg="Red", bg="Ivory")
        NameLb.config(font=("Times",15,"bold italic"))
        NameLb.place(x=200,y=80)
        
        NameLb = Label(lgn_frame1, text="Name of the Medicine*", fg="Red", bg="Ivory")
        NameLb.config(font=("Times",15,"bold italic"))
        NameLb.place(x=200,y=120)
        

        #Taking name as input from user
        NameEn = Entry(lgn_frame1, textvariable=Name)
        NameEn.place(x=400,y=80)

        NameEn1 = Entry(lgn_frame1, textvariable=Name2)
        NameEn1.place(x=400,y=120)


       

        #Buttons for predicting the disease using different algorithms
        rnf = Button(lgn_frame1, text="Submit", command=medicineadd,bg="Light green",fg="red")
        rnf.config(font=("Times",15,"bold italic"))
        rnf.place(x=400,y=150)

        rs = Button(lgn_frame1,text="Reset Inputs", command=Reset,bg="yellow",fg="purple",width=15)
        rs.config(font=("Times",15,"bold italic"))
        rs.place(x=700,y=80)

        ex = Button(lgn_frame1,text="Exit System", command=Exit,bg="yellow",fg="purple",width=15)
        ex.config(font=("Times",15,"bold italic"))
        ex.place(x=900,y=80)

    def fooddiet():
        lgn_frame1 = Frame(titleframe, bg='Ivory', width=1390, height=900,highlightbackground="gray", highlightthickness=2)
        lgn_frame1.place(x=1, y=100)
        Name=StringVar()
        Name2=StringVar()
        def medicineadd():
            fooddiet_db(NameEn.get(),NameEn1.get())
            messagebox.showinfo("Success","Successfully food diet data added to database")

        
        def Reset():
            NameEn.delete(first=0,last=100)
            NameEn1.delete(first=0,last=100)
            
        from tkinter import messagebox
        def Exit():
            qExit=messagebox.askyesno("System","Do you want to exit the system")
            
            if qExit:
                lgn_frame1.destroy()
                
        #Headings for the GUI written at the top of GUI
        w2 = Label(lgn_frame1, justify=LEFT, text="Disease and their Food Diet Database", fg="Red", bg="Ivory")
        w2.config(font=("Arial",20,"bold italic"))
        w2.place(x=480,y=10)
        

        #Label for the name
        NameLb = Label(lgn_frame1, text="Name of the Disease*", fg="Red", bg="Ivory")
        NameLb.config(font=("Times",15,"bold italic"))
        NameLb.place(x=200,y=80)
        
        NameLb = Label(lgn_frame1, text="Food Diet*", fg="Red", bg="Ivory")
        NameLb.config(font=("Times",15,"bold italic"))
        NameLb.place(x=200,y=120)
        

        #Taking name as input from user
        NameEn = Entry(lgn_frame1, textvariable=Name)
        NameEn.place(x=400,y=80)

        NameEn1 = Entry(lgn_frame1, textvariable=Name2)
        NameEn1.place(x=400,y=120)


       

        #Buttons for predicting the disease using different algorithms
        rnf = Button(lgn_frame1, text="Submit", command=medicineadd,bg="Light green",fg="red")
        rnf.config(font=("Times",15,"bold italic"))
        rnf.place(x=400,y=150)

        rs = Button(lgn_frame1,text="Reset Inputs", command=Reset,bg="yellow",fg="purple",width=15)
        rs.config(font=("Times",15,"bold italic"))
        rs.place(x=700,y=80)

        ex = Button(lgn_frame1,text="Exit System", command=Exit,bg="yellow",fg="purple",width=15)
        ex.config(font=("Times",15,"bold italic"))
        ex.place(x=900,y=80)

    def hospitals():
        lgn_frame1 = Frame(titleframe, bg='Ivory', width=1390, height=900,highlightbackground="gray", highlightthickness=2)
        lgn_frame1.place(x=1, y=100)
        Name=StringVar()
        Name2=StringVar()
        Name3=StringVar()
        Name4=StringVar()
        def medicineadd():
            hospital_db(NameEn.get(),NameEn1.get(),NameEn2.get(),NameEn3.get())
            messagebox.showinfo("Success","Successfully hospitals data added to database")

        
        def Reset():
            NameEn.delete(first=0,last=100)
            NameEn1.delete(first=0,last=100)
            NameEn2.delete(first=0,last=100)
            NameEn3.delete(first=0,last=100)
            
        from tkinter import messagebox
        def Exit():
            qExit=messagebox.askyesno("System","Do you want to exit the system")
            
            if qExit:
                lgn_frame1.destroy()
                
        #Headings for the GUI written at the top of GUI
        w2 = Label(lgn_frame1, justify=LEFT, text="Hospitals Informations Database", fg="Red", bg="Ivory")
        w2.config(font=("Arial",20,"bold italic"))
        w2.place(x=480,y=10)
        

        #Label for the name
        NameLb = Label(lgn_frame1, text="Hospital Name*", fg="Red", bg="Ivory")
        NameLb.config(font=("Times",15,"bold italic"))
        NameLb.place(x=200,y=80)
        
        NameLb = Label(lgn_frame1, text="Phone Number*", fg="Red", bg="Ivory")
        NameLb.config(font=("Times",15,"bold italic"))
        NameLb.place(x=200,y=120)

        NameLb = Label(lgn_frame1, text="Location Address*", fg="Red", bg="Ivory")
        NameLb.config(font=("Times",15,"bold italic"))
        NameLb.place(x=200,y=160)

        NameLb = Label(lgn_frame1, text="Area*", fg="Red", bg="Ivory")
        NameLb.config(font=("Times",15,"bold italic"))
        NameLb.place(x=200,y=200)
        

        #Taking name as input from user
        NameEn = Entry(lgn_frame1, textvariable=Name)
        NameEn.place(x=400,y=80)

        NameEn1 = Entry(lgn_frame1, textvariable=Name2)
        NameEn1.place(x=400,y=120)

        NameEn2 = Entry(lgn_frame1, textvariable=Name3)
        NameEn2.place(x=400,y=160)

        NameEn3 = Entry(lgn_frame1, textvariable=Name4)
        NameEn3.place(x=400,y=200)


       

        #Buttons for predicting the disease using different algorithms
        rnf = Button(lgn_frame1, text="Submit", command=medicineadd,bg="Light green",fg="red")
        rnf.config(font=("Times",15,"bold italic"))
        rnf.place(x=400,y=250)

        rs = Button(lgn_frame1,text="Reset Inputs", command=Reset,bg="yellow",fg="purple",width=15)
        rs.config(font=("Times",15,"bold italic"))
        rs.place(x=700,y=80)

        ex = Button(lgn_frame1,text="Exit System", command=Exit,bg="yellow",fg="purple",width=15)
        ex.config(font=("Times",15,"bold italic"))
        ex.place(x=900,y=80)
    def logout():
        titleframe.destroy()
        
    b= ("The Moon Milter", 15)
    

    open_button = Button(titleframe,text='Medicine',command=medicine,bd=1,bg="grey",font=b,fg='white')
    open_button.place(x=950,y=60)

    open_button = Button(titleframe,text='Food Diet',command=fooddiet,bd=1,bg="dark blue",font=b,fg='white')
    open_button.place(x=1060,y=60)

    open_button = Button(titleframe,text='Hospitals',command=hospitals,bd=1,bg="dark green",font=b,fg='white')
    open_button.place(x=1180,y=60)

    open_button = Button(titleframe,text='Logout',command=logout,bd=1,bg="brown",font=b,fg='white')
    open_button.place(x=1280,y=60)


##root = Tk()
##root.title('HUMAN ILL HEALTH DETECTION')
##root.resizable(True, True)
##root.geometry('1500x750')
##root.configure(bg='ghost white')
##admin_page(root)
