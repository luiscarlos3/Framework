from dis import distb
import os, sys
import pymysql
from Controller import utilis
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.write import Console
from Controller import help
from Controller.list_controller import Tables
from Controller.utilis import utilidades



obj = Query.Sql()
class RouteSetting:
    def __init__(self, table, idcolumns):        
        self.__table = table
        self.__idcolumns = idcolumns

    def routeInsert(self):
        status = False        
        column = obj.columns(self.__table)  
        tupl = tuple(self.__inputTheRoute(column))  
        print(tupl)
        if not tupl:
            status = False      
        else:
            if Sql.insert(self.__table, tupl) == True:
                status = True       
            else:
                status = False    
        return status

    def routeDelete(self,id):            
        return Sql.delete(self.__table, self.__idcolumns, id)             

    def routeSearch(self,id):
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extend_router_to_deliver_search() + " where " + " cedula_camionero " + " = " + "'" + id + "'"
        consulta.execute(sql)    
        data = consulta.fetchone()
        print(help.Empty(data, consulta.description) ) 
        if data:                          
            Tables.table_vertical(self.__table, data, utilidades.columnsSearchRoute())  
        else:
            print("no se encontro la ruta ")

    def routeUpdate(self, id):
        status = False
        herdears = obj.columns(self.__table)
        columns = help.convertArray(herdears)
        tupl = self.__inputUpdateTheRoute(columns, id)
        if not tupl:
            status = False
        else:
            if Sql.update(tupl) == True:
                status = True
            else:
                status = False              
        return status

    def routeList(self):
        cs = query_extend.extend_router_to_deliver()        
        Tables.design_table_columns(cs, utilidades.columnsListRoute())
#----------------------------------------------------------------------*
# help methods avoid overload
#----------------------------------------------------------------------*
    def __inputTheRoute(self,column):
        msg = "Ingrese"
        array = help.convertArray(column)
        lista = []        
        for i in range(0, len(array)):             
            if i == 0:
                cod = help.codigoShipper()               
                print(array[i] +" : ", cod)
                lista.append(cod)
            elif i <= 2:
                var = Console.inputNumber(msg + ' ' + array[i] + " : ")
                lista.append(var)            
            elif i == 3 :
                option = help.selection()
                lista.append(option)            
            else:
                lista.append(self.__subConditionInputRoute(array, i))
        return lista    
                
    def __subConditionInputRoute(self, column, i):                     
        if i<=5:
            Time = help.currentdate()
            print(column[i] + " : " + Time)
            return Time
        if i == 6 :      
            var = Console.inputString("ingrese " +column[6] + " : ")
            return var             
        else:
            city  = Console.inputString("ingrese " +column[7] + " : ")            
            return help.inputCity(city)  
        
    def __inputUpdateTheRoute(self, column, id):
        Conn =  Database.conexion()
        update = tuple()
        consulta = Conn.cursor()   
        sql = "select * from "+ self.__table + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchone()        
        if data:
            update = self.__upgradeOptions(column, data, id)
        else:
            print("No se encuentra")
        return update
            
    def __upgradeOptions(self, columns, data, id):
        update = tuple()
        print("\n")
        for i in range(0, len(columns)):                               
            print(i, " columna :" ,columns[i], " = ", data[i])
            print("\n")
        option = Console.inputNumber("selecione la columna : ")           
        update = self.__changeDataRoute(columns, option, id)           
        return update
    
    def __changeDataRoute(self,columns, option, id):
        update = tuple()
        msg = "Ingrese"
        if option == 1 or option == 2:
            position = columns[option]
            edit = Console.inputNumber(msg +" "+ columns[option] + " : ")
            update = (self.__table, position, edit, self.__idcolumns, id)
        elif option == 3:
            position = columns[option]
            edit = Console.inputString(msg + " "+columns[5] + " : ")           
            if help.v(edit) == True:
                print("No esta el municipio")
            else:
                edit = help.v(edit)
                update = (self.__table, position, edit, self.__idcolumns, id)                        
        return update
       
            

        
        
        
        
        
        
        
            
            
            
            
        
        
                
                
                
                
                
                
    
    
    
                
                
            
            
            
            
        

          
