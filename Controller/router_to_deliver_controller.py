import os, sys
import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.validation import Validar
from Controller import help
from Controller.list_controller import Tables

obj = Query.Sql('transporte')

def sql_Router_To_Deliver_Insert(table):
    status = False
    val = Validar(table)  
    column = obj.columns(table)
    lista = []
    for x in range(0, len(column)):
                
        if x == 0:
            codigo = help.codigo()
            print(str(column[0]).strip("('").strip("',)") + " : " , codigo)
            lista.append(codigo)
            
        elif x == 3:
            clock = str(help.time())         
            print(str(column[3]).strip("('").strip("',)") + " : " , clock)       
            lista.append(clock)
            
        elif x == 4:
            arrival = str(help.time_shipping_output())            
            print(str(column[4]).strip("('").strip("',)") + " : " , arrival)
            lista.append(arrival)
            
        elif x == 5:    
            var = help.selection()
            print(str(column[5]).strip("('").strip("',)") + " : " , var)
            lista.append(var)
            
        elif x == 6:
            name = input("Ingrese " + str(column[6]).strip("('").strip("',)") + " : ")                           
            if val.controller_city(name) == False:
                print("este municipio no se encuentra")
                break
            
            else:
                village = help.update_city(name)               
                lista.append(village) 
                        
                    
        else:
            register = input("Ingrese " + str(column[x]).strip("('").strip("',)") + " : ")                    
            lista.append(register)
        print(lista)
        
    tupl = tuple(lista)
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
          
