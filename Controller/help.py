from Controller.write import Console
import random
import os, sys
from datetime import date, datetime, timedelta
from Model.connection import Database
from Controller.validation import Validar
    
def codigo():    
    num = random.randint(0, 1000000000000000)
    return num

# esto toca cambiar 
def codigoShipper():
    num = random.randint(0, 1000)
    return  num

# esto toca cambiar 
def codigoRouter():
    num = random.randint(0, 1000)
    return  num

def checkElements(array):
    for i in range(0, len(array)):
        if array[i] == None:
            return None
    return array 

def checkQuery(Data, columns):
    elements = {}   
    if not Data:
        for i in range(1, len(columns)):
            elements[i] = ' '
        elements.update({"Bool" : False})              
    else:        
        field_name = [field[0] for field in columns]
        elements = dict(zip(field_name, Data))
        elements.update({"Bool":True})       
    return elements

def getTitles(Query):    
    title = [field[0] for field in Query]    
    return title  

def Check(Data, columns):  
    field_name = [field[0] for field in columns]
    elements = dict(zip(field_name, Data))
    return elements    

def convert_city(village):
    try:
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        sql = "select id_municipio from municipios where municipio = " + "'"+ village + "'"
        consulta.execute(sql)
        data = consulta.fetchone()    
        village = data[0]
        return village
    except :
        return False
           
def util(elements):
    i=0  
    for x in elements:
        i+=1
        print(i ," "+ elements[x])
        
def selection():
        elements = {1: "enviado", 2: "entregado", 3: "salida"}
        quit = False
        while quit == False:
            util(elements)
            num = int(input("seleccione un opcion : "))  
            if num > len(elements) or num <= 0:          
                print("opcion invalida")       
            else:
                quit = True
                return elements[num]   

def Date(msg):
    print("ejemplo : a??o-mes-dia = 2020-06-12")
    year = Console.inputNumber(msg + " a??o : ")
    month =  Console.inputNumber(msg + " mes : ")
    day = Console.inputNumber(msg + " dia : ")
    return str(year)+"-" + str(month)+ "-" + str(day) 

def currentdate():
    today = date.today()
    now = datetime.now()      
    return str(today.year) + "-" + str(today.month) + "-" +str(today.day)  + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)     

def fecha():
    ahora = datetime.now()    
    Date = ahora + timedelta(days=3)
    return str(Date.year) + "-" +str(Date.month) + "-" +str(Date.day) 

def convertArray(array):
        lista= []
        for i in range(len(array)):
            for j in range(len(array[i])):
                lista.append(array[i][j])
        return lista
    
def inputCity(name):
    village = 0     
    if Validar.controller_city(name) == False:                        
        print("Este municipio no se encuentra")        
        return None
    else:
        village = convert_city(name)
    return village   


def testResultList(valor, titulos):        
        if not valor:
           print("Error al cargar los datos")
        registros = {} # opcional
        lista = [] # recursividad fila 
        valores_lista = list(valor)# 
        #titulos = list(valor)[0]
        #titulos = ['matricula', 'modelo', 'tipo', 'potencia', 'doc_camionero', 'nombre_camionero', 'apellido_camionero', 'telefono','municipio']
        registros["titulos"] = titulos
        for x in range(0, len(valores_lista)): 
            lista = list(valores_lista[x])
            registros[x+1] = lista
        return registros
    
def getID(elements, numekey ,position):
    x = dict(elements)
    lista = list(x.get(numekey))       
    return lista[position]


    
    







            
            
            
            
                
                
                               
        
    
    
           


        
    
    
    