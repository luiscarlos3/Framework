import os, sys
import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.write import Console
from Controller import help
from Controller.list_controller import Tables

obj = Query.Sql()
class router:

    def sql_Router_To_Deliver_Insert(table):
        status = False   
        tupl = tuple(None)
        if Sql.insert(tupl, table) == True:
            status = True       
        else:
            status = False    
        return status

    def sql_Router_To_Deliver_Delete(id):
            status = False
            if Sql.delete('ruta_entrega_paquete', 'id_ruta', id) == True:
                status = True
            else:
                status = False
            return status

    def sql_Router_To_Deliver_Search(table, colum, id):
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extend_router_to_deliver_search() + " where " + colum + " = " + "'" + id + "'"
        consulta.execute(sql)    
        data = consulta.fetchone()
        colums = ["codigo ruta",               
             "cedula camionero", 
             "nombre camionero",
             "apellido camionero",
             "telefono",
             "matricula vehiculo",
             "tipo de vehiculo",
             "fecha inicio de entrega", 
             "fecha final de entrega",
             "estado",
             "ciudad",
             "codigo de envio"]    
        if data:        
            Tables.table_vertical(table, data, colums )  
        else:
            print("no se encontro la ruta ")

    def sql_Router_To_Deliver_Update(table, id, colum):
        status = False   
        Conn =  Database.conexion()
        consulta = Conn.cursor()   
        sql = "select * from "+ table + " where " + colum + " = " + "'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchone()   
        herdears = obj.columns(table)
        if data:
            for i in range(0, len(herdears)):
                print(i,". "+ "Columna : " +str(herdears[i]).strip("('").strip("',)") + " = " , data[i])      
                print("\n")
            num = int(input("seleccione la columna : "))      
            for i in range(0, len(herdears)):
                if num == 5:
                    positio = str(herdears[5]).strip("('").strip("',)")
                    edit = help.selection()               
                    Datos = (table, positio, edit , colum, id)
                    break
            
                elif num == 6:
                    positio = str(herdears[6]).strip("('").strip("',)")
                    edit = str(input("ingrese dato para actualizar : "))
                    Datos = (table, positio, edit , colum, id)              
                
                    if  help.update_city(Datos) == True:
                        status = True
                    else:
                        status = False 
                    break                            
            
                elif num == i:
                    positio = str(herdears[i]).strip("('").strip("',)")
                    edit = str(input("ingrese dato para actualizar : "))
                    Datos = (table, positio, edit , colum, id)
                    if Sql.update(Datos) == True:            
                        status = True
                          
                    else:                    
                        status = False       
                        break                   
        else:
            print("la persona no se encuentra")     
        return status

    def sql_Router_To_Deliver_List():
        cs = query_extend.extend_router_to_deliver()
        columns = ["departamento", "ciudad", "codigo ruta","cedula camionero", "matricula", "fecha inicio entrega", "fecha fin entrega"]
        Tables.design_table_columns(cs, columns)
#----------------------------------------------------------------------*
# help methods avoid overload
#----------------------------------------------------------------------*
    def inputRouter(self,column):
        msg = "Ingrese"
        array = help.convertArray(column)
        lista = []
        for i in range(0, len(array)):             
            if i is 0:
                cod = help.codigoShipper()               
                print(array[i] +" : ", cod)
                lista.append(cod)
            elif i>=2:
                var = Console.inputNumber(msg + ' ' + array[i] + " : ")
                lista.append(var)
            elif i == 3:
                option = help.selection()
                lista.append(option)            
            else:
                lista = lista.append(self.__condition(array, i))
                
    def __condition(self, column, i):        
        if i>=5:
            Time = help.currentdate()
            print(column[i] + " : " + Time)
            return Time
        elif i==6:              
            city = Console.inputString("ingrese" +" "+column[6] + " : ")   
            return city
        elif i == 7:
            id_envio = Console.inputNumber("ingrese " + " " + column[7] + " : ")
            return id_envio
            
            
            
            
            
        
        
                
                
                
                
                
                
    
    
    
                
                
            
            
            
            
        

          
