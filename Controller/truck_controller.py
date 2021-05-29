import os, sys
import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.validation import  Validar
from Controller import help
from Controller.list_controller import Tables
from Controller.write import Console

obj = Query.Sql()
class ControllerTruck:
    
    def __init__(self, table, idcolumns):        
        self.__table = table
        self.__idcolumns = idcolumns
        
    def truckInsert(self,id):
        status = False
        column = obj.columns(self.__table)
        tupl = tuple(self.__truckInput(id,column))
        if not tupl:
            status = False
        else:
            if obj.insert(self.__table, tupl) == True:
                status = True
            else:
                status = False
        return status        
   

    def truckDelete(self,id):        
        return Sql.delete(self.__table, self.__idcolumns, id) 
    
    def truckUpdate(self, id):
        self.__truckInputUpdate(id)        

    def sql_Truck_Update(table, id, colum):
        status = False   
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        sql = query_extend.extend_truck() + " where " + colum + " = " + "'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchone()    
        herdears = obj.columns(table)    
        if data:
            for i in range(0, len(herdears)):
                print(i,". "+ "Columna : " +str(herdears[i]).strip("('").strip("',)") + " = " , data[i])      
                print("\n")
            num = int(input("ingrese la columna : "))              
            for i in range(0, len(herdears)):            
                if num == 5:
                    positio = str(herdears[5]).strip("('").strip("',)")
                    edit = str(input("ingrese dato para actualizar : "))
                    Datos = (table, positio, edit , colum, id)              
                    if help.update_city(Datos) == True:
                        status = True
                        break
                    else:
                        status = False
                        break         
                
                elif num == i:
                    positio = str(herdears[i]).strip("('").strip("',)")
                    edit = str(input("ingrese dato para actualizar : "))
                    Datos = (table, positio, edit , colum, id)
                    if Sql.update(Datos) == True:            
                        status = True
                        break                 
                    else:                    
                        status = False
                        break         
        else:
            print("el vehiculo no se encuentra ")     
        return status

    def sql_Truck_Search(table,colum,id):         
        conn = Database().conexion()
        consulta = conn.cursor()        
        sql =   query_extend.extend_truck() + " where " + colum +" = '" + id + "'"     
        consulta.execute(sql)
        herdears = obj.columns(table)
        data = consulta.fetchone()    
        if data:        
            Tables.table_vertical(table, data, herdears)  
        else:
            print("no se encontro el camion")
        
    def truckList(self):
        cs = query_extend.extend_truck()
        Tables.design_table('camion', cs)
        
    def __driverValidation(self, id):       
        return Validar.validation_truck_driver("camionero",id, "documento") == True         
           
    def __truckInput(self,id,column):
        msg = "Ingrese"        
        array = self.__convertArray(column)
        lista = []       
        if self.__driverValidation(id):
             lista = self.__call(array, msg, lista, id)               
        else:
            print("No se encuentra registrado")
        return lista
    
    def __call(self,column, msg, lista, id):
        lista = []
        val = Validar(self.__table)                       
        register = input(msg +" "+column[0] + " : ")
        if val.Register_validation(register, self.__idcolumns) == True:                    
            print("Ya se encuentra registrado")                    
        else:
            lista.append(register)
            modelo = Console.inputNumber(msg +" "+column[1]+ " : ")
            lista.append(modelo)
            value = Console.inputString(msg +" " +column[2] + " : ")
            lista.append(value)
            potencia = Console.inputNumber(msg +" "+column[3]+ " : ")
            lista.append(potencia)
            lista.append(id)
            city = Console.inputString(msg +" "+column[5] + " : ")                   
            lista.append(self.__inputCity(city))         
        return lista
    
    def __callUpdate(self, data):
        i = 0
        while i >= len(data):
            i+=1
            
    
    def __truckInputUpdate(self,id):
        status = False   
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        sql = query_extend.extend_truck() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchone()    
        herdears = obj.columns(self.__table)
        if data:
            self.__callUpdate(herdears)
        else:
            print("")
            
    
        
            
        
            
            
                
        
    def __convertArray(self,array):
        lista= []
        for i in range(len(array)):
            for j in range(len(array[i])):
                lista.append(array[i][j])
        return lista
    
    def __inputCity(self, name):
        village = 0       
        if Validar.controller_city(name) == False:                        
            print("este municipio no se encuentra")
            os.system("pause")
        else:
            village = help.convert_city(name)
        return village    
        
        
        
    
   