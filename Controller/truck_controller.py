import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.validation import  Validar
from Controller import help

from Controller.write import Console
from Controller.PDF import CreatePdf

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
        tupl = tuple(self.__truckInputUpdate(id))
        if not tupl:
            status = False
        else:
            if Sql.update(tupl) == True:
                status = True
            else:
                status = False
        return status 
    
    def truckSearch(self,id):
        status = False         
        conn = Database().conexion()
        consulta = conn.cursor()        
        sql = query_extend.extendTruckSearch() + " where " + self.__idcolumns +" = '" + id + "'"     
        consulta.execute(sql)       
        data = consulta.fetchone()    
        if data:
            status = True
            conn.close()
            return status, data, help.getTitles(consulta.description)                       
        else:
            status = True
            return status, None, None, 
       
            
    def optionPDF(self):
        print("¿ Desea generar reporte general de vehiculos ?")
        print("Si >> y")
        print("No >> n")
        op = Console.inputString("selecione una opcion ")
        if op == "y":
            self.__generaPdfTruck()
        return " "   
            
    def __generaPdfTruck(self):                   
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extendTruckSearch()       
        consulta.execute(sql)
        data = consulta.fetchall()                    
        if data:
            data = help.testResultList(data, help.getTitles(consulta.description) )
            CreatePdf.excutePdfReport("Reportes.html",data,"vehiculos")
        return" "        
        
    def truckList(self):
        conn = Database().conexion()
        consulta = conn.cursor()        
        sql =  query_extend.extend_truck()
        consulta.execute(sql)
        rows = consulta.fetchall()
        return rows, help.getTitles(consulta.description)
        
    def __driverValidation(self, id):       
        return Validar.validation_truck_driver("camionero",id, "documento") == True
    
    #----------------------------------------------------------------------*
    # help methods avoid overload
    #----------------------------------------------------------------------*       
         
    def __truckInput(self,id,column):
        msg = "Ingrese"        
        array = help.convertArray(column)
        lista = []       
        if self.__driverValidation(id):
             lista = self.__ConditionInput(array,lista, id)# toco pasar mas 3 argumentos               
        else:
            print("No se encuentra registrado")
        return lista
    
    def __truckInputUpdate(self,id):         
        Conn =  Database.conexion()
        lista = []
        consulta = Conn.cursor()
        sql = query_extend.extend_truck() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchone()
        if data:
            lista = self.__conditionOne(help.getTitles(consulta.description), data, id)
        else:
            print("No se encuentra el vehiculo ")           
        return lista  
    
    def __ConditionInput(self,column,lista, id):
        lista = []
        msg = "ingrese"
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
            lista.append(help.inputCity(city))
        lista = help.checkElements(lista)
        print(lista)      
        return lista
    
    def __conditionOne(self, columns, data, id):
        msg = "ingrese "
        lista = []
        print("\n")        
        for i in range(0, len(columns)):                    
            print(i, " columna :" ,columns[i], " = ", data[i])
            print("\n")
        option = Console.inputNumber("selecione la columna : ")                   
        if option == 0:
            position = columns[option]
            edit = input(msg + columns[option] + " : ")                         
        elif option == 1:
            position = columns[option]
            edit = Console.inputNumber(msg + columns[option] + " : ")                            
        elif option == 2:
            position = columns[option]
            edit = Console.inputNumber(msg+ columns[option] + " : ")            
        elif option > len(columns):
            return None            
        else:
            return self.__conditionTwoo(option, columns, id)
        lista = help.checkElements([self.__table, position, edit, self.__idcolumns, id])               
        return lista
    
    def __conditionTwoo(self,option, columns, id):
        msg = "ingrese "
        lista = []        
        if option == 3:
            position = columns[option]
            edit = Console.inputNumber(msg + columns[option] + " : ")                       
        elif option == 4:
            position = columns[option]
            edit = Console.inputNumber(msg + columns[option] + " : ")           
        elif option == 5:
            position = columns[option]
            edit = Console.inputString(msg + columns[option] + " : ")           
            edit = help.inputCity(edit)            
        elif option > len(columns):
            return None
        lista = help.checkElements([self.__table, position, edit, self.__idcolumns, id])
        return lista
    
        
        
        
    
              
        
    
        
        
        
    
   