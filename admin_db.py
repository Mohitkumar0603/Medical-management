
#pip install sqlalchemy==1.4.46
import sqlalchemy
import mysql.connector
from mysql.connector import Error
import string
import random
from datetime import date
import pandas as pd


d3=pd.read_csv("medicines.csv",encoding= 'unicode_escape')
d4=pd.read_csv("hospitals.csv",encoding= 'unicode_escape')
d5=pd.read_csv("fooddiet.csv",encoding= 'unicode_escape')


database_username = 'root'
database_password = 'Aleesha#143'
database_ip       = 'localhost'
database_name     = 'medical'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))

#d3.to_sql(con=database_connection, name='medicine', if_exists='replace',index=False)
#d4.to_sql(con=database_connection, name='hospitals', if_exists='replace',index=False)
#d5.to_sql(con=database_connection, name='fooddiet', if_exists='replace',index=False)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def db_connection():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database='medical',
                                                     user='root',
                                                     password='Aleesha#143')
                if connection.is_connected():
                    db_Info = connection.get_server_info()
                    print("Connected to MySQL Server version ", db_Info)
                    cur = connection.cursor()
                    return connection,cur
            except Error as e:
                print(e)
#connection,cur=db_connection()
def symptoms_db(s):
    connection,cur=db_connection()
    query=("insert into symptoms(Symptoms) values(%s)" )
    cur.execute(query,(s,))
    connection.commit()
def disease_db(d):
    connection,cur=db_connection()
    query=("insert into disease(Disease) values(%s)" )
    cur.execute(query,(d,))
    connection.commit()
def medicine_db(d,m):
    connection,cur=db_connection()
    query=("insert into medicine(Disease,Medicine) values(%s,%s)" )
    cur.execute(query,(d,m))
    connection.commit()
def fooddiet_db(d,fd):
    connection,cur=db_connection()
    query=("insert into fooddiet(Disease, FoodDiet) values(%s,%s)" )
    cur.execute(query,(d,fd))
    connection.commit()

def hospital_db(h,p,l,a):
    connection,cur=db_connection()
    query=("insert into hospitals(HospitalName ,phonenumber ,LocationAddress ,Area) values(%s,%s,%s,%s)" )
    cur.execute(query,(h,p,l,a))
    connection.commit()
def view_symptoms():
    connection,cur=db_connection()
    query=("select Symptoms from  symptoms" )
    cur.execute(query)
    sym=[]
    data=cur.fetchall()
    for i in data:
        sym.append(i[0])
     
    return sym

def view_disease():
    connection,cur=db_connection()
    query=("select Disease from  disease" )
    cur.execute(query)
    sym=[]
    data=cur.fetchall()
    for i in data:
        sym.append(i[0])   
    return sym
def view_medicine(input_value):
    connection,cur=db_connection()
    query=("select * from  medicine" )
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        if i[0].upper()==input_value.upper():
            return i[1]
def view_fooddiet(input_value):
    connection,cur=db_connection()
    query=("select * from  fooddiet" )
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        if i[0].upper()==input_value.upper():
            print(i[1])
            return i[1]

def view_hospitals(input_value):
    connection,cur=db_connection()
    query=("select * from  hospitals" )
    cur.execute(query)
    data=cur.fetchall()
    h=[]
    for i in data:
        if i[3].upper()==input_value:
            h.append(i)
    return h

