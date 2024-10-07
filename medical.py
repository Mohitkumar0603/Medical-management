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
import os
import PIL.Image

root = Tk()
root.title('HUMAN ILL HEALTH DETECTION')
root.resizable(True, True)
root.geometry('1500x750')
root.configure(bg='ghost white')
#root.wm_attributes('-transparentcolor', '#ab23ff')

titleframe = LabelFrame(root)
titleframe.grid(row=0,column=0)

image=PIL.Image.open("3.jpg")

img=image.resize((1500, 600))
my_img=ImageTk.PhotoImage(img)
            # Show image using label
label1 = Label( root, image = my_img)
label1.image = my_img
label1.place(x = 0, y = 100)


image=PIL.Image.open("image2.png")

img=image.resize((100, 80))
my_img=ImageTk.PhotoImage(img)
            # Show image using label
label1 = Label( root, image = my_img,bg='ghost white')
label1.image = my_img
label1.place(x = 70, y = 19)

f= ("Farrah", 25, "bold")
label1 = Label( root, text="HUMAN ILL HEALTH DETECTION",font=f,bg="ghost white",fg="red")
label1.place(x = 320, y = 10)

f= ("Times", 15, "bold")
label1 = Label( root, text="By Using Machine Learning",font=f,bg="ghost white")
label1.place(x = 340, y =60)
def find_disease():
    global pd
    lgn_frame1 = Frame(root, bg='Ivory', width=1390, height=900,highlightbackground="gray", highlightthickness=2)
    lgn_frame1.place(x=1, y=100)
    pred2=StringVar()
    pred1=StringVar()
    d=pd.read_csv("disease_description.csv")
    l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
        'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
        'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
        'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
        'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
        'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
        'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
        'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
        'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
        'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
        'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
        'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
        'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
        'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
        'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
        'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
        'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
        'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
        'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
        'yellow_crust_ooze']

    disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
        'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
        'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
        'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
        'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
        'Impetigo']

    l2=[]
    for i in range(0,len(l1)):
        l2.append(0)
    df=pd.read_csv("Training.csv")

    #Replace the values in the imported file by pandas by the inbuilt function replace in pandas.

    df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)
    X= df[l1]
    y = df[["prognosis"]]
    np.ravel(y)

    tr=pd.read_csv("Testing.csv")

    #Using inbuilt function replace in pandas for replacing the values

    tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40,}},inplace=True)

    X_test= tr[l1]
    y_test = tr[["prognosis"]]
    np.ravel(y_test)


    def randomforest():
        global img_label
        if len(NameEn.get()) == 0:
            comp=messagebox.askokcancel("System","Kindly Fill the Name")
            if comp:
                root.mainloop()
        elif((Symptom1.get()=="Select Here") or (Symptom2.get()=="Select Here")):
            sym=messagebox.askokcancel("System","Kindly Fill atleast first two Symptoms")
            if sym:
                root.mainloop()
        else:
            from sklearn.ensemble import RandomForestClassifier
            clf4 = RandomForestClassifier(n_estimators=100)
            clf4 = clf4.fit(X,np.ravel(y))

            '''# calculating accuracy 
            from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
            y_pred=clf4.predict(X_test)
            print("Random Forest")
            print("Accuracy")
            print(accuracy_score(y_test, y_pred))
            print(accuracy_score(y_test, y_pred,normalize=False))
            print("Confusion matrix")
            conf_matrix=confusion_matrix(y_test,y_pred)
            print(conf_matrix)'''
        
            psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

            for k in range(0,len(l1)):
                for z in psymptoms:
                    if(z==l1[k]):
                        l2[k]=1

            inputtest = [l2]
            predict = clf4.predict(inputtest)
            predicted=predict[0]

            h='no'
            for a in range(0,len(disease)):
                if(predicted == a):
                    h='yes'
                    break
            if (h=='yes'):
                pred2.set(" ")
                path=d[d['Disease']==disease[a].upper()]['Path'].values.tolist()[-1]
                pred2.set(disease[a])
                image=PIL.Image.open(path)

                img=image.resize((630, 350))
                my_img=ImageTk.PhotoImage(img)
                            # Show image using label
                img_label = Label( lgn_frame1, image = my_img,bg='Ivory',bd=0)
                img_label.image = my_img
                img_label.place(x = 700, y = 150)
            else:
                pred2.set(" ")
                pred2.set("Not Found")
    
    Symptom1 = StringVar()
    Symptom1.set("Select Here")

    Symptom2 = StringVar()
    Symptom2.set("Select Here")

    Symptom3 = StringVar()
    Symptom3.set("Select Here")

    Symptom4 = StringVar()
    Symptom4.set("Select Here")

    Symptom5 = StringVar()
    Symptom5.set("Select Here")
    Name = StringVar()

    
    def Reset():
        global prev_win

        Symptom1.set("Select Here")
        Symptom2.set("Select Here")
        Symptom3.set("Select Here")
        Symptom4.set("Select Here")
        Symptom5.set("Select Here")
        NameEn.delete(first=0,last=100)
        pred2.set(" ")
        img_label.image=None
        
    from tkinter import messagebox
    def Exit():
        qExit=messagebox.askyesno("System","Do you want to exit the system")
        
        if qExit:
            lgn_frame1.destroy()
            
    #Headings for the GUI written at the top of GUI
    w2 = Label(lgn_frame1, justify=LEFT, text="Human Disease Detection", fg="Red", bg="Ivory")
    w2.config(font=("Times",30,"bold italic"))
    w2.place(x=500,y=10)
    

    #Label for the name
    NameLb = Label(lgn_frame1, text="Name of the Patient *", fg="Red", bg="Ivory")
    NameLb.config(font=("Times",15,"bold italic"))
    NameLb.place(x=200,y=80)
    #Creating Labels for the symtoms
    S1Lb = Label(lgn_frame1, text="Symptom 1 *", fg="Black", bg="Ivory")
    S1Lb.config(font=("Times",15,"bold italic"))
    S1Lb.place(x=200,y=150)

    S2Lb = Label(lgn_frame1, text="Symptom 2 *", fg="Black", bg="Ivory")
    S2Lb.config(font=("Times",15,"bold italic"))
    S2Lb.place(x=200,y=200)

    S3Lb = Label(lgn_frame1, text="Symptom 3", fg="Black",bg="Ivory")
    S3Lb.config(font=("Times",15,"bold italic"))
    S3Lb.place(x=200,y=250)

    S4Lb = Label(lgn_frame1, text="Symptom 4", fg="Black", bg="Ivory")
    S4Lb.config(font=("Times",15,"bold italic"))
    S4Lb.place(x=200,y=300)

    S5Lb = Label(lgn_frame1, text="Symptom 5", fg="Black", bg="Ivory")
    S5Lb.config(font=("Times",15,"bold italic"))
    S5Lb.place(x=200,y=350)

    #Labels for the algorithms

    destreeLb = Label(lgn_frame1, text="Detected Disease", fg="Red", bg="Orange", width = 20)
    destreeLb.config(font=("Times",15,"bold italic"))
    destreeLb.place(x=200,y=400)
    OPTIONS = sorted(l1)

    #Taking name as input from user
    NameEn = Entry(lgn_frame1, textvariable=Name)
    NameEn.place(x=400,y=80)

    #Taking Symptoms as input from the dropdown from the user
    S1 = OptionMenu(lgn_frame1, Symptom1,*OPTIONS)
    S1.place(x=400,y=150)

    S2 = OptionMenu(lgn_frame1, Symptom2,*OPTIONS)
    S2.place(x=400,y=200)

    S3 = OptionMenu(lgn_frame1, Symptom3,*OPTIONS)
    S3.place(x=400,y=250)

    S4 = OptionMenu(lgn_frame1, Symptom4,*OPTIONS)
    S4.place(x=400,y=300)

    S5 = OptionMenu(lgn_frame1, Symptom5,*OPTIONS)
    S5.place(x=400,y=350)

    #Buttons for predicting the disease using different algorithms
    rnf = Button(lgn_frame1, text="Detection", command=randomforest,bg="Light green",fg="red")
    rnf.config(font=("Times",15,"bold italic"))
    rnf.place(x=550,y=80)

    rs = Button(lgn_frame1,text="Reset Inputs", command=Reset,bg="yellow",fg="purple",width=15)
    rs.config(font=("Times",15,"bold italic"))
    rs.place(x=700,y=80)

    ex = Button(lgn_frame1,text="Exit System", command=Exit,bg="yellow",fg="purple",width=15)
    ex.config(font=("Times",15,"bold italic"))
    ex.place(x=900,y=80)

    #Showing the output of different algorithms

    t2=Label(lgn_frame1,font=("Times",15,"bold italic"),text="Random Forest",height=1,bg="Purple"
             ,width=20,fg="white",textvariable=pred2,relief="sunken").place(x=470,y=400)
def medicine():
    global pd
    lgn_frame1 = Frame(root, bg='Ivory', width=2290, height=800)
    lgn_frame1.place(x=150, y=180)
    Name=StringVar()
    pred2=StringVar()
    #Headings for the GUI written at the top of GUI
    w2 = Label(lgn_frame1, justify=LEFT, text="Search Medicine for disease", fg="Red", bg="Ivory")
    w2.config(font=("Times",30,"bold italic"))
    w2.grid(row=1, column=0, columnspan=2, padx=100)
    

    #Label for the name
    NameLb = Label(lgn_frame1, text="Disease Name*", fg="Red", bg="Ivory")
    NameLb.config(font=("Times",15,"bold italic"))
    NameLb.place(x=200,y=50)

    #Taking name as input from user
    NameEn = Entry(lgn_frame1, textvariable=Name,width="30")
    NameEn.grid(row=6, column=1)
    
    def result():
        
        df=pd.read_csv("medicines.csv",encoding = 'unicode_escape')
        med=df[df['Disease']==NameEn.get()]['Medicine'].values.tolist()[0]
        
        pred2.set(med)
    def Exit():
        qExit=messagebox.askyesno("System","Do you want to exit the system")
        
        if qExit:
            lgn_frame1.destroy()
            
    def Reset():
        pred2.set(" ")

        NameEn.delete(first=0,last=100)
    ex = Button(lgn_frame1,text="Submit", command=result,bg="yellow",fg="purple",width=8)
    ex.config(font=("Times",15,"bold italic"))
    ex.grid(row=15, column=1, padx=10)

    rs = Button(lgn_frame1,text="Reset Input", command=Reset,bg="yellow",fg="purple",width=8)
    rs.config(font=("Times",15,"bold italic"))
    rs.grid(row=15, column=3, padx=10)



    ex = Button(lgn_frame1,text="Exit", command=Exit,bg="red",fg="white",width=5)
    ex.config(font=("Times",10,"bold italic"))
    ex.place(x=0,y=0)

    t2=Label(lgn_frame1,font=("Times",15,"bold italic"),text="",height=1
                 ,width=80,fg="white",).grid(row=16, column=1, padx=10)
    
    t2=Label(lgn_frame1,font=("Times",15,"bold italic"),text="Medicines:",height=1,bg="Purple"
                 ,width=80,fg="white",textvariable=pred2).grid(row=20, column=1, padx=10)

def fooddiet():
    global pd
   
    lgn_frame1 = Frame(root, bg='white', width=1390, height=900,highlightbackground="gray", highlightthickness=2)
    lgn_frame1.place(x=0, y=100)
        
    Name=StringVar()
    pred2=StringVar()
    #Headings for the GUI written at the top of GUI
    w2 = Label(lgn_frame1, justify=LEFT, text="Food Diet for Disease", fg="Red", bg="Ivory")
    w2.config(font=("Times",30,"bold italic"))
    w2.place(x=400,y=10)
    

    #Label for the name
    NameLb = Label(lgn_frame1, text="Disease Name*", fg="Red", bg="Ivory")
    NameLb.config(font=("Times",15,"bold italic"))
    NameLb.place(x=300,y=100)

    #Taking name as input from user
    NameEn = Entry(lgn_frame1, textvariable=Name,width="30")
    NameEn.place(x=460,y=100)
    
    def result():
        
        df=pd.read_csv("fooddiet.csv",encoding = 'unicode_escape')
        med=df[df['Disease']==NameEn.get()]['Food Diet'].values.tolist()[0]
        text.insert(INSERT, "\t"+"Food Diet for "+NameEn.get()+" : "+"\n")
        text.insert(INSERT, ""+"\n")
        text.insert(INSERT, "\t"+med+"\n")
    def Exit():
        qExit=messagebox.askyesno("System","Do you want to exit this menu")
        
        if qExit:
            lgn_frame1.destroy()
            
    def Reset():
        text.delete("1.0","end")

        NameEn.delete(first=0,last=100)
    ex = Button(lgn_frame1,text="Submit", command=result,bg="yellow",fg="purple",width=8)
    ex.config(font=("Times",15,"bold italic"))
    ex.place(x=500,y=150)

    rs = Button(lgn_frame1,text="Reset Input", command=Reset,bg="yellow",fg="purple",width=8)
    rs.config(font=("Times",15,"bold italic"))
    rs.place(x=700,y=150)



    ex = Button(lgn_frame1,text="Exit", command=Exit,bg="red",fg="white",width=5)
    ex.config(font=("Times",10,"bold italic"))
    ex.place(x=0,y=0)

    f4= ("Times", 15, "bold")
    text = Text(lgn_frame1,width="95",height="50",font=f4,bg="#faba66")
    text.place(x = 200, y = 200)

def hospitals():
    global pd
   
    lgn_frame1 = Frame(root, bg='white', width=1390, height=900,highlightbackground="gray", highlightthickness=2)
    lgn_frame1.place(x=0, y=100)
        
    Name=StringVar()
    pred2=StringVar()
    #Headings for the GUI written at the top of GUI
    w2 = Label(lgn_frame1, justify=LEFT, text="Search Nearby Hospitals", fg="Red", bg="Ivory")
    w2.config(font=("Times",30,"bold italic"))
    w2.place(x=400,y=10)
    

    #Label for the name
    NameLb = Label(lgn_frame1, text="Location*", fg="Red", bg="Ivory")
    NameLb.config(font=("Times",15,"bold italic"))
    NameLb.place(x=300,y=100)

    value_inside = StringVar()
    df=pd.read_csv("hospitals.csv",encoding = 'unicode_escape')
    options_list=df['Area'].values.tolist()
    # Set the default value of the variable
    value_inside.set("Select an Option")
      
    # Create the optionmenu widget and passing 
    # the options_list and value_inside to it.
    question_menu = OptionMenu(lgn_frame1, value_inside, *options_list)
    question_menu.place(x=460,y=100)

    #Taking name as input from user
    #NameEn = Entry(lgn_frame1, textvariable=Name,width="30")
    #NameEn.place(x=460,y=100)
    
    def result():
        global tree
        def selectItem(a):
            curItem = tree.focus()
            data=tree.item(curItem).get('values')
            messagebox.askyesno(data[0],"Mobile No. :"+str(data[1])+"\n"+"Address: "+data[2]+"\n"+"Area : "+data[3])
        df=pd.read_csv("hospitals.csv",encoding = 'unicode_escape')
        med=df[df['Area']==value_inside.get()]
        cols = list(med.columns)
        tree = ttk.Treeview(lgn_frame1)
        tree.place(x = 20, y = 200)
        tree["columns"] = cols
        tree.bind('<ButtonRelease-1>', selectItem)
        for i in cols:
            tree.column(i, anchor="w",width=300)
            tree.heading(i, text=i, anchor='w')
        for index, row in med.iterrows():
                #tree.insert("",0,text=index,values=list(row))
                tree.insert("", "end", values=list(row))
    def Exit():
        qExit=messagebox.askyesno("System","Do you want to exit this menu")
        
        if qExit:
            lgn_frame1.destroy()
            
    def Reset():
        for item in tree.get_children():
                tree.delete(item)
    ex = Button(lgn_frame1,text="Submit", command=result,bg="yellow",fg="purple",width=8)
    ex.config(font=("Times",15,"bold italic"))
    ex.place(x=500,y=150)

    rs = Button(lgn_frame1,text="Reset Input", command=Reset,bg="yellow",fg="purple",width=8)
    rs.config(font=("Times",15,"bold italic"))
    rs.place(x=700,y=150)



    ex = Button(lgn_frame1,text="Exit", command=Exit,bg="red",fg="white",width=5)
    ex.config(font=("Times",10,"bold italic"))
    ex.place(x=0,y=0)

    f4= ("Times", 15, "bold")
    
b= ("Decary Sans", 10, "bold")
open_button = Button(root,text='Home',command="#",bd=0,bg="ghost white",font=b,fg='dark blue')
open_button.place(x=900,y=70)

open_button = Button(root,text='Find Disease',command=find_disease,bd=0,bg="ghost white",font=b,fg='dark blue')
open_button.place(x=990,y=70)

open_button = Button(root,text='Medicine',command=medicine,bd=0,bg="ghost white",font=b,fg='dark blue')
open_button.place(x=1100,y=70)

open_button = Button(root,text='Food Diet',command=fooddiet,bd=0,bg="ghost white",font=b,fg='dark blue')
open_button.place(x=1200,y=70)

open_button = Button(root,text='Hospitals',command=hospitals,bd=0,bg="ghost white",font=b,fg='dark blue')
open_button.place(x=1280,y=70)

root.mainloop()
