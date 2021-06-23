import pymysql
from Model.connection import Database
from Model import Query,query_extend
from Model.Query import Sql
from Controller.validation import Validar
from Controller import help
from Controller.write import Console

obj = Query.Sql()
class ControllerDriver:
    
    def __init__(self, table, idcolumns):        
        self.__table = table
        self.__idcolumns = idcolumns  

    def truckDriverInsert(self):
        status = False    
        column = obj.columns(self.__table)
        tupl = tuple(self.__driverTruckInput(column))
        print(tupl)        
        if not tupl:
            status = False
        else:
            if Sql.insert(self.__table,tupl) == True:
                status = True
            else:
                status = False
        return status

    def TruckDriverDelete(self, id):        
        return Sql.delete(self.__table, self.__idcolumns, id)

    def truckDriverUpdate(self, id):
        status = False      
        tupl = self.__inputdriverUpdate(id)       
        if not tupl:
            status = False
        else:
            if Sql.update(tupl) == True:
                status = True
            else:
                status = False
        return status

    def truckDriverSearch(self,id):
        status = False        
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extend_truck_driver() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)        
        data = consulta.fetchone()       
        if data:
            status = True
            conn.close()
            return status, data, help.getTitles(consulta.description)            
        else:
            status = False
            return status,None, None    
        
    def listTruckDriver(self):
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extend_truck_driver()
        consulta.execute(sql)
        rows = consulta.fetchall()
        return rows, help.getTitles(consulta.description)       
        
    #----------------------------------------------------------------------*
    # help methods avoid overload
    #----------------------------------------------------------------------*
    def __inputdriverUpdate(self,id):
            Conn =  Database.conexion()
            lista = []
            consulta = Conn.cursor()            
            sql = query_extend.extend_truck_driver() + " where " + self.__idcolumns + " = " + "'" + id + "'"
            consulta.execute(sql)
            data = consulta.fetchone()
            if data:
                lista = self.__conditionOne(help.getTitles(consulta.description), data, id)
            else:
                print ("no se encuentra el camionero")
            return lista
        
    def __conditionOne(self, columns, data, id):
            lista = []
            print("\n")
            for i in range(0, len(columns)):                    
                print(i, " columna :" ,columns[i], " = ", data[i])
                print("\n")
            option = Console.inputNumber("selecione la columna : ")           
            lista = self.__condtionTwoo(columns, option, id)           
            return lista
        
    def __condtionTwoo(self,array, option, id):
        lista = []
        msg = "Ingrese "                 
        if option >= 0 and option <= 3:                
                position = array[option]
                edit = Console.inputString(msg + array[option] + " : ")                             
        elif option == 4 or option == 5:
            position = array[option]
            edit = Console.inputNumber(msg + array[option] + " : ")
        elif option > len(array):
            return None                       
        else:
            return self.__condtionTherre(option, array, id)
        lista = [self.__table, position, edit, self.__idcolumns, id]
        return lista               
        
    
    def __condtionTherre(self, option, array, id):
        lista = []
        msg = "Ingrese "
        if option == 6:
            position = array[option]
            edit = help.Date()           
        elif option == 7:
            position = array[option]
            edit = Console.inputString(msg + array[option] + " : ")
            edit = help.inputCity(edit)       
                      
        elif option > len(array):
            return None
        lista = help.checkElements([self.__table, position, edit, self.__idcolumns, id])      
        return lista      
    
    def __driverTruckInput(self, column):
        msg = "Ingrese"
        val = Validar(self.__table)
        array = help.convertArray(column)
        lista = []
        for i in range(0, len(array)):
            if i is 0:
                id = Console.inputNumber(msg + " " +array[0] + " : ")
                if val.Register_validation(id, self.__idcolumns) == True:
                    print("ya se encuentra registrado")
                    break
                else:
                    lista.append(id)
            if i >= 1 and i <= 3:
                name = Console.inputString(msg +" " +array[i]+ " : ")
                lista.append(name)
            elif i == 4 or i == 5 :
                var = Console.inputNumber(msg + ' ' + array[i]  + " : ")
                lista.append(var)                      
            elif i == 6:
                print(msg + ' ' + array[i])
                date = help.Date(msg)
                lista.append(date)
            elif i == 7:
                edit = Console.inputString(msg + " "+ array[i] + " : ")
                edit = help.inputCity(edit)                                     
        return lista
    
           
                
        
            
            

    
            
            
            
            
        
                
                
            
                
                    
        
        
        
        
        
    
    
    
    