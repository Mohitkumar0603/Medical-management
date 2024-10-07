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
from admin_db import *
import pandas as pd
import numpy as np
from joblib import load
root = Tk()
root.title('HUMAN ILL HEALTH DETECTION')
root.resizable(True, True)
root.geometry('1500x750')
root.configure(bg='ghost white')
root.wm_attributes('-transparentcolor', '#ab23ff')
def user_page(root):
    titleframe = LabelFrame(root,width="1500",height="750",bg="ghost white")
    titleframe.grid(row=0,column=0)

    image=PIL.Image.open("3.jpg")

    img=image.resize((1500, 600))
    my_img=ImageTk.PhotoImage(img)
                # Show image using label
    label1 = Label( titleframe, image = my_img)
    label1.image = my_img
    label1.place(x = 0, y = 100)


    image=PIL.Image.open("image2.png")

    img=image.resize((100, 80))
    my_img=ImageTk.PhotoImage(img)
                # Show image using label
    label1 = Label( titleframe, image = my_img,bg='ghost white')
    label1.image = my_img
    label1.place(x = 70, y = 19)

    f= ("Farrah", 25, "bold")
    label1 = Label( titleframe, text="HUMAN ILL HEALTH DETECTION",font=f,bg="ghost white",fg="red")
    label1.place(x = 320, y = 10)

    f= ("Times", 15, "bold")
    label1 = Label( titleframe, text="By Using Machine Learning",font=f,bg="ghost white")
    label1.place(x = 340, y =60)
    def find_disease():
        global pd
        lgn_frame1 = Frame(titleframe, bg='Ivory', width=1390, height=900,highlightbackground="gray", highlightthickness=2)
        lgn_frame1.place(x=1, y=100)
        pred2=StringVar()
        pred1=StringVar()
        d=pd.read_csv("disease_description.csv")
        l1=['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue',
                                  'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss',
                                  'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration',
                                  'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever',
                                  'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
                                  'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
                                  'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
                                  'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness',
                                  'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
                                  'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes',
                                  'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma',
                                  'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples',
                                  'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']

        


        def randomforest():
            global img_label
            if len(NameEn.get()) == 0:
                comp=messagebox.askokcancel("System","Kindly Fill the Name")
                if comp:
                    titleframe.mainloop()
            elif((Symptom1.get()=="Select Here") or (Symptom2.get()=="Select Here") or (Symptom3.get()=="Select Here") ):
                sym=messagebox.askokcancel("System","Kindly Fill three Symptoms")
                if sym:
                    titleframe.mainloop()
            else:
                symptom_list = [str(Symptom1.get()),str(Symptom2.get()),str(Symptom3.get())]
                
                print(symptom_list)

                symptoms = {'itching': 0, 'skin_rash': 0, 'nodal_skin_eruptions': 0, 'continuous_sneezing': 0,
                'shivering': 0, 'chills': 0, 'joint_pain': 0, 'stomach_pain': 0, 'acidity': 0, 'ulcers_on_tongue': 0,
                'muscle_wasting': 0, 'vomiting': 0, 'burning_micturition': 0, 'spotting_ urination': 0, 'fatigue': 0,
                'weight_gain': 0, 'anxiety': 0, 'cold_hands_and_feets': 0, 'mood_swings': 0, 'weight_loss': 0,
                'restlessness': 0, 'lethargy': 0, 'patches_in_throat': 0, 'irregular_sugar_level': 0, 'cough': 0,
                'high_fever': 0, 'sunken_eyes': 0, 'breathlessness': 0, 'sweating': 0, 'dehydration': 0,
                'indigestion': 0, 'headache': 0, 'yellowish_skin': 0, 'dark_urine': 0, 'nausea': 0, 'loss_of_appetite': 0,
                'pain_behind_the_eyes': 0, 'back_pain': 0, 'constipation': 0, 'abdominal_pain': 0, 'diarrhoea': 0, 'mild_fever': 0,
                'yellow_urine': 0, 'yellowing_of_eyes': 0, 'acute_liver_failure': 0, 'fluid_overload': 0, 'swelling_of_stomach': 0,
                'swelled_lymph_nodes': 0, 'malaise': 0, 'blurred_and_distorted_vision': 0, 'phlegm': 0, 'throat_irritation': 0,
                'redness_of_eyes': 0, 'sinus_pressure': 0, 'runny_nose': 0, 'congestion': 0, 'chest_pain': 0, 'weakness_in_limbs': 0,
                'fast_heart_rate': 0, 'pain_during_bowel_movements': 0, 'pain_in_anal_region': 0, 'bloody_stool': 0,
                'irritation_in_anus': 0, 'neck_pain': 0, 'dizziness': 0, 'cramps': 0, 'bruising': 0, 'obesity': 0, 'swollen_legs': 0,
                'swollen_blood_vessels': 0, 'puffy_face_and_eyes': 0, 'enlarged_thyroid': 0, 'brittle_nails': 0, 'swollen_extremeties': 0,
                'excessive_hunger': 0, 'extra_marital_contacts': 0, 'drying_and_tingling_lips': 0, 'slurred_speech': 0,
                'knee_pain': 0, 'hip_joint_pain': 0, 'muscle_weakness': 0, 'stiff_neck': 0, 'swelling_joints': 0, 'movement_stiffness': 0,
                'spinning_movements': 0, 'loss_of_balance': 0, 'unsteadiness': 0, 'weakness_of_one_body_side': 0, 'loss_of_smell': 0,
                'bladder_discomfort': 0, 'foul_smell_of urine': 0, 'continuous_feel_of_urine': 0, 'passage_of_gases': 0, 'internal_itching': 0,
                'toxic_look_(typhos)': 0, 'depression': 0, 'irritability': 0, 'muscle_pain': 0, 'altered_sensorium': 0,
                'red_spots_over_body': 0, 'belly_pain': 0, 'abnormal_menstruation': 0, 'dischromic _patches': 0, 'watering_from_eyes': 0,
                'increased_appetite': 0, 'polyuria': 0, 'family_history': 0, 'mucoid_sputum': 0, 'rusty_sputum': 0, 'lack_of_concentration': 0,
                'visual_disturbances': 0, 'receiving_blood_transfusion': 0, 'receiving_unsterile_injections': 0, 'coma': 0,
                'stomach_bleeding': 0, 'distention_of_abdomen': 0, 'history_of_alcohol_consumption': 0, 'fluid_overload.1': 0,
                'blood_in_sputum': 0, 'prominent_veins_on_calf': 0, 'palpitations': 0, 'painful_walking': 0, 'pus_filled_pimples': 0,
                'blackheads': 0, 'scurring': 0, 'skin_peeling': 0, 'silver_like_dusting': 0, 'small_dents_in_nails': 0, 'inflammatory_nails': 0,
                'blister': 0, 'red_sore_around_nose': 0, 'yellow_crust_ooze': 0}
    
                # Set value to 1 for corresponding symptoms
                for s in symptom_list:
                    symptoms[s] = 1
                
                # Put all data in a test dataset
                df_test = pd.DataFrame(columns=list(symptoms.keys()))
                df_test.loc[0] = np.array(list(symptoms.values()))
                
                # Load pre-trained model
                clf = load(str("./saved_model/decision_tree.joblib"))
                result = clf.predict(df_test)
                print(result[0])
                pred2.set(" ")
                #path=d[d['Disease']==result[0].upper()]['Path'].values.tolist()[-1]
                pred2.set(result[0])
##                image=PIL.Image.open(path)
##
##                img=image.resize((630, 350))
##                my_img=ImageTk.PhotoImage(img)
##                            # Show image using label
##                img_label = Label( lgn_frame1, image = my_img,bg='Ivory',bd=0)
##                img_label.image = my_img
##                img_label.place(x = 700, y = 150)
        
        Symptom1 = StringVar()
        Symptom1.set("Select Here")

        Symptom2 = StringVar()
        Symptom2.set("Select Here")

        Symptom3 = StringVar()
        Symptom3.set("Select Here")

        
        Name = StringVar()

        
        def Reset():
            global prev_win

            Symptom1.set("Select Here")
            Symptom2.set("Select Here")
            Symptom3.set("Select Here")
            
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

        S3Lb = Label(lgn_frame1, text="Symptom 3 *", fg="Black",bg="Ivory")
        S3Lb.config(font=("Times",15,"bold italic"))
        S3Lb.place(x=200,y=250)

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
        lgn_frame1 = Frame(titleframe, bg='white', width=1390, height=900,highlightbackground="gray", highlightthickness=2)
        lgn_frame1.place(x=0, y=100)
            
        Name=StringVar()
        pred2=StringVar()
        #Headings for the GUI written at the top of GUI
        w2 = Label(lgn_frame1, justify=LEFT, text="Medicine for Disease", fg="Red", bg="Ivory")
        w2.config(font=("Arial",20,"bold italic"))
        w2.place(x=400,y=10)
        

        #Label for the name
        NameLb = Label(lgn_frame1, text="Disease Name*", fg="Red", bg="Ivory")
        NameLb.config(font=("Times",15,"bold italic"))
        NameLb.place(x=300,y=100)

        #Taking name as input from user
        NameEn = Entry(lgn_frame1, textvariable=Name,width="30")
        NameEn.place(x=460,y=100)
        
        def result():
            
        
            med=view_medicine(NameEn.get())
            text.insert(INSERT, "\t"+"Medicine for "+NameEn.get()+" : "+"\n")
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

    def fooddiet():
        global pd
       
        lgn_frame1 = Frame(titleframe, bg='white', width=1390, height=900,highlightbackground="gray", highlightthickness=2)
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
            
        
            med=view_fooddiet(NameEn.get())
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
       
        lgn_frame1 = Frame(titleframe, bg='white', width=1390, height=900,highlightbackground="gray", highlightthickness=2)
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
            #df=pd.read_csv("hospitals.csv",encoding = 'unicode_escape')
            #med=df[df['Area']==value_inside.get()]
            med=view_hospitals(value_inside.get())
            cols = ["Hospital Name","Phone Number","Location Address","Area"]
            tree = ttk.Treeview(lgn_frame1)
            tree.place(x = 20, y = 200)
            tree["columns"] = cols
            tree.bind('<ButtonRelease-1>', selectItem)
            for i in cols:
                tree.column(i, anchor="w",width=300)
                tree.heading(i, text=i, anchor='w')
            #for index, row in med.iterrows():
            for row in med:
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
    def logout():
        titleframe.destroy()
        
    b= ("Decary Sans", 10, "bold")
    open_button = Button(titleframe,text='Home',command="#",bd=0,bg="ghost white",font=b,fg='dark blue')
    open_button.place(x=800,y=70)

    open_button = Button(titleframe,text='Find Disease',command=find_disease,bd=0,bg="ghost white",font=b,fg='dark blue')
    open_button.place(x=890,y=70)

    open_button = Button(titleframe,text='Medicine',command=medicine,bd=0,bg="ghost white",font=b,fg='dark blue')
    open_button.place(x=1000,y=70)

    open_button = Button(titleframe,text='Food Diet',command=fooddiet,bd=0,bg="ghost white",font=b,fg='dark blue')
    open_button.place(x=1100,y=70)

    open_button = Button(titleframe,text='Hospitals',command=hospitals,bd=0,bg="ghost white",font=b,fg='dark blue')
    open_button.place(x=1180,y=70)

    open_button = Button(titleframe,text='Logout',command=logout,bd=0,bg="ghost white",font=b,fg='dark blue')
    open_button.place(x=1280,y=70)

user_page(root)

