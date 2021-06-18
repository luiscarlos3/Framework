import pymysql
from Model.connection import Database
from Model import Query,query_extend
from Model.Query import Sql
from Controller.validation import Validar
from Controller import help
from Controller.list_controller import Tables
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
        herdears = obj.columns(self.__table)
        columns = help.convertArray(herdears)
        tupl = self.__inputdriverUpdate(columns, id)       
        if not tupl:
            status = False
        else:
            if Sql.update(tupl) == True:
                status = True
            else:
                status = False
        return status

    def truckDriverSearch(self,id):         
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extend_truck_driver() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)
        herdears = obj.columns(self.__table)
        data = consulta.fetchall()       
        if data:        
            Tables.table_vertical(self.__table, data, herdears)
            self.__optionPDF()
        else:
            print("no se encontro el destinatario")    
        
    def listTruckDriver(self):
        cs = query_extend.extend_truck_driver()
        Tables.design_table(self.__table, cs)
    #----------------------------------------------------------------------*
    # help methods avoid overload
    #----------------------------------------------------------------------*
    def __inputdriverUpdate(self,column,id):
            Conn =  Database.conexion()
            update = tuple()
            consulta = Conn.cursor()            
            sql = query_extend.extend_truck_driver() + " where " + self.__idcolumns + " = " + "'" + id + "'"
            consulta.execute(sql)
            data = consulta.fetchone()
            if data:
                update = self.__conditionOne(column, data, id)
            else:
                print ("no se encuentra el camionero")
            return update
        
    def __conditionOne(self, columns, data, id):
            update = tuple()
            print("\n")
            for i in range(0, len(columns)):                    
                print(i, " columna :" ,columns[i], " = ", data[i])
                print("\n")
            option = Console.inputNumber("selecione la columna : ")           
            update = self.__condtionTwoo(columns, option, id)           
            return update
        
    def __condtionTwoo(self,array, option, id):
        update = tuple()
        msg = "Ingrese"                 
        if option >= 0 and option <= 3:                
                position = array[option]
                edit = Console.inputString(msg +" "+array[option] + " : ")
                update = (self.__table, position, edit, self.__idcolumns, id)               
        elif option is 4 or option is 5:
            position = array[option]
            edit = Console.inputNumber(msg +" "+array[option] + " : ")
            update = (self.__table, position, edit, self.__idcolumns, id)            
        else:
            update = self.__condtionTherre(option, array, id)
                   
        return update
    
    def __condtionTherre(self, option, array, id):
        update = tuple()
        msg = "Ingrese"
        if option is 6:
            position = array[option]
            edit = help.Date()
            update = (self.__table, position, edit, self.__idcolumns, id)
        elif option is 7:
            position = array[7]
            var = Console.inputString(msg + " "+ array[7] + " : ") 
            if help.inputCity(var) == True:
                print("No esta el municipio")
            else:
                edit = help.v(var)
                update = (self.__table, position, edit, self.__idcolumns, id)
        else:
            print("Columna invalida")        
        return update       
    
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
            elif i is 4 or i is 5 :
                var = Console.inputNumber(msg + ' ' + array[i]  + " : ")
                lista.append(var)                      
            elif i is 6:
                print(msg + ' ' + array[i])
                date = help.Date(msg)
                lista.append(date)
            elif i is 7:
                var = Console.inputString(msg + " "+ array[7] + " : ")           
                if help.inputCity(var) == True:
                    print("No esta el municipio")
                else:
                    edit = help.v(var)            
                    lista.append(edit)                            
        return lista
    
           
                
        
            
            

    
            
            
            
            
        
                
                
            
                
                    
        
        
        
        
        
    
    
    
    