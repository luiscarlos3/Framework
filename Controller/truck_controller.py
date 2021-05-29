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
        status = False
        herdears = obj.columns(self.__table)
        columns = self.__convertArray(herdears)
        tupl = self.__truckInputUpdate(columns, id)
        if not tupl:
            status = False
        else:
            if Sql.update(tupl) == True:
                status = True
            else:
                status = False
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
    #--------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------       
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
    
    def __callUpdate(self, columns, data, id):
        msg = "ingrese"
        update = tuple()
        print("\n")
        j = 0
        for i in range(0, len(columns)):                    
            print(i, " columna :" ,columns[i], " = ", data[i])
            print("\n")
        option = Console.inputNumber("selecione la columna : ")                   
        if option is 0:
            position = columns[0]
            edit = input(msg +" "+columns[0] + " : ")
            update = (self.__table, position, edit,self.__idcolumns, id)
                           
        elif option is 1:
            position = columns[1]
            edit = Console.inputNumber(msg +' '+ columns[1] + " : ")
            update = (self.__table, position, edit, self.__idcolumns, id)
                
        elif option is 2:
            position = columns[2]
            edit = Console.inputNumber(msg+ ' ' + columns[2] + " : ")
            update = (self.__table, position, edit, self.__idcolumns, id)
        else:
            update = self.__val(option, columns, id)    
                
        return update
    
    def __val (self,option, columns, id):
        msg = "ingrese"
        update = tuple()
        print(columns)    
        if option is 3:
            position = columns[option]
            edit = Console.inputNumber(msg + " " +columns[3] + " : ")
            update = (self.__table, position, edit, self.__idcolumns, id)            
        elif option is 4:
            position = columns[option]
            edit = Console.inputNumber(msg + " " +columns[4] + " : ")
            update = (self.__table, position, edit, self.__idcolumns, id)
        elif option is 5:
            position = columns[option]
            edit = Console.inputString(msg + " "+columns[5] + " : ")
            edit = self.__inputCity(edit)  
            update = (self.__table, position, edit, self.__idcolumns, id)     
        return update      
    
    def __truckInputUpdate(self,column, id):         
        Conn =  Database.conexion()
        update = tuple()
        consulta = Conn.cursor()
        sql = query_extend.extend_truck() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchone()
        if data:
            update = self.__callUpdate(column, data, id)
        else:
            print("No se encuentra el vehiculo ")           
        return update          
        
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
        
        
        
    
   