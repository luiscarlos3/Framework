from Controller.write import Console
import pymysql
import random
import os, sys
from datetime import date, datetime, timedelta
from Model.connection import Database
from Controller.validation import Validar


    
def codigo():    
    num = random.randint(0, 1000000000000000)
    return num

def convert_city(village):
    Conn =  Database.conexion()
    consulta = Conn.cursor()
    sql = "select id_municipio from municipios where municipio = " + "'"+ village + "'"
    consulta.execute(sql)
    data = consulta.fetchone()    
    village = data[0]
    return village    

            
def selection():
    op = ''
    print("1 -- enviando")
    print("2 -- entregado")
    print("3 -- salida")
    print("\n")
    num =int(input("seleccione el estado ")) 
    if  num == 1 :
        op = 'enviado'
    elif num == 2:
        op = 'entregado'
    elif num == 3:
        op = 'salida'        
    return op

def birthDate(msg):
    print("ejemplo : año-mes-dia = 2020-06-12")
    year = Console.inputNumber(msg + " año : ")
    month =  Console.inputNumber(msg + " mes : ")
    day = Console.inputNumber(msg + " dia : ")
    return str(year)+"-" + str(month)+ "-" + str(day) 


def inputDatetime():
    today = date.today()
    now = datetime.now()
    fecha = str()   
    month = input("ingrese el mes : ")
    day = input("ingrese el dia : ")
    fecha = str(today.year) + "-" + month + "-" + day + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    return fecha

def time_arrival_shipping():
    now = datetime.now()
    new_Date = now + timedelta(days=2)  
    return new_Date

def convertArray(array):
        lista= []
        for i in range(len(array)):
            for j in range(len(array[i])):
                lista.append(array[i][j])
        return lista
    
def inputCity(name):
    village = 0     
    if Validar.controller_city(name) == False:                        
        print("este municipio no se encuentra")
        os.system("pause")
    else:
        village = convert_city(name)
    return village
   
def v(name):
    status = False                         
    if Validar.controller_city(name) == False:
        status = True                         
    else:
        status = False                              
        return convert_city(name)
    return status


            
            
            
            
                
                
                               
        
    
    
           


        
    
    
    