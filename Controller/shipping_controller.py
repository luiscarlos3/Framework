from datetime import time
import os, sys
import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.validation import Validar
from Controller import help
from Controller.list_controller import Tables
from Controller.utilis import utilidades
from Controller.write import Console

obj = Query.Sql()

class controllerShipping():
    
    def __init__(self, table, idcolumns):        
        self.__table = table
        self.__idcolumns = idcolumns
    

    def shippingInsert(self):
        status = False    
        column = obj.columns(self.__table)
        tupl = tuple(self.__shippingInput(column))
        if not tupl:
            status = False
        else:
            if Sql.insert(self.__table, tupl):
                status = True
            else: 
                status = False
            
        return status

    def sql_Shipping_Delete(self):        
        return Sql.delete( self.__table, self.__idcolumns, id)
           

    def sql_Search_Shipping(self,id):
        conn = Database().conexion()
        consulta = conn.cursor()    
        sql =  query_extend.extend_shipping_search() + " where "+ self.__idcolumns+ " = "+"'" + id + "'"     
        consulta.execute(sql)    
        data = consulta.fetchone()
        if data:         
            Tables.table_vertical(self.__table, data, utilidades.columnsShippings())   
        else:
            print("no se encontro el envio ")    

    def sql_Shipping_Update(table, id, colum):
        status = False   
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        sql = "select * from " + table + " where " + colum + " = " + "'" + id + "'"
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
                    edit = help.selection()               
                    Datos = (table, positio, edit , colum, id)
                    break
                         
                elif num == i:
                    positio = str(herdears[i]).strip("('").strip("',)")
                    edit = str(input("ingrese dato para actualizar : "))
                    Datos = (table, positio, edit , colum, id)
                    break
                
            if  Sql.update(Datos) == True:            
                status = True
                          
            else:                    
                status = False                   
        else:
            print("el vehiculo persona no se encuentra")     
        return status

    def sql_Shipping_List():
        cs = query_extend.extend_shipping()
        columns = ["codigo_envio", "estado", "direccion","cedula destinatario", "cedula remitente","codigo paquete"]
        Tables.design_table_columns(cs, columns)

#----------------------------------------------------------------------*
# help methods avoid overload
#----------------------------------------------------------------------* 
    def __shippingInput(self, column):
        msg = "Ingrese"
        array = help.convertArray(column)
        lista = []
        for i in range(0, len(array)):
            if i is 0:
                cod = help.codigoShipper()               
                print(array[i] +" : ", cod)
                lista.append(cod)
            elif i>=1 and i<=4:
                var = Console.inputNumber(msg + ' ' + array[i] + " : ")
                lista.append(var)
            elif i is 5:
                string = Console.inputString(msg + ' ' + array[i] + " : ")
                lista.append(string)                            
            elif i is 6:                 
                var = self.__valor()
                lista.append(var)                          
            elif i is 7:
                Time = help.currentdate()
                print(array[i] + " : " + Time)
                lista.append(Time)                
            elif i is 8:                
                date = help.fecha()
                print(date)
                print(array[i] + " " +date)
                lista.append(date)
        print(lista)               
        return lista
    
    def __valor(self):      
        print("1 -- enviando")
        print("2 -- entregado")
        print("3 -- salida")
        print("\n")
        num =int(input("seleccione el estado ")) 
        if  num == 1 :
            return "Enviado"
        elif num == 2:
            return "Entregado"
        elif num == 3:
            return "Salida"
              
            
                
               
                
    
            
                 
                
                
        
        


