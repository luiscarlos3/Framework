import os, sys
import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller import validation
from Controller import help
from Controller.list_controller import Tables

obj = Query.Sql('transporte')

def sql_Shipping_Insert(table):
    status = False    
    column = obj.columns(table)
    lista = []
    for x in range(0, len(column)):
        if x == 0:
            codigo = help.codigo()
            print(str(column[0]).strip("('").strip("',)") + " : " , codigo)
            lista.append(codigo)
        elif x == 5:            
            var = help.selection()
            print(str(column[5]).strip("('").strip("',)") + " : " + var)       
            lista.append(var)
        elif x == 6:
            clock = str(help.time())
            print(str(column[6]).strip("('").strip("',)") + " : " + clock)
            lista.append(clock)
        elif x == 7:
            arrival = str(help.time_arrival_shipping())
            print(str(column[7]).strip("('").strip("',)") + " : " + arrival)
            lista.append(arrival)          
        else:
            register = input("Ingrese " + str(column[x]).strip("('").strip("',)") + " : ")                    
            lista.append(register)
            
    tupl = tuple(lista)
    if  Sql.insert(tupl, table) == True:
        status = True
    else:  
        status = False
            
    return status

def sql_Shipping_Delete(id):
    status = False
    if Sql.delete('envio', 'id_envio', id) == True:
        status = True
    else:
        status = False
    return status

def sql_Search_Shipping(table, colum, id):
    conn = Database().conexion()
    consulta = conn.cursor()
    #sql = "select * from " + table + " where " + colum + " = " + "'" + id + "'"
    sql =  query_extend.extend_shipping_search() + " where "+ colum + " = "+"'" + id + "'"     
    consulta.execute(sql)
    colums = ["codigo_envio", 
            "estado", 
            "direccion",
            "cedula destinatario",
            "nombre destinatario",
            "apellido destinatario",
            "cedula remitente",
            "nombre remitente",
            "apellido remitente",
            "codigo paquete",
            "descripcion",
            "peso kg",
            "fecha de envio",
            "fecha de llegada"                
            ]
    data = consulta.fetchone()
    if data:         
        Tables.table_vertical("envio",data,colums)   
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