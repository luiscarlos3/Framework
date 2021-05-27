import os, sys
import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller import validation
from Controller import help
from Controller.list_controller import Tables

obj = Query.Sql()

def sql_Package_Insert(table):
    status = False      
    column = obj.columns(table)
    lista = []
    for x in range(0, len(column)):
        if x == 0:
            codigo = help.codigo()
            print(str(column[0]).strip("('").strip("',)") + " : " , codigo)
            lista.append(codigo)            
        else:
            register = input("Ingrese " + str(column[x]).strip("('").strip("',)") + " : ")                    
            lista.append(register)
                       
    tupl = tuple(lista)
    if Sql.insert(tupl, table) == True:
        status = True
       
    else:  
        status = False
                 
    return status                  

def sql_Package_Search(table,colum, id):
    conn = Database().conexion()
    consulta = conn.cursor()
    sql =  query_extend.extend_package_search()+ " where " + colum + " = '" + id + "'"   
    consulta.execute(sql)
    data = consulta.fetchone()
    columns = [
        'codigo',
        'cedula remitente',
        'nombre remitente',
        'apellido remitente',
        'telefono remitente',
        'direccion remitente', 
        'cedula destinatario',
        'nombre destinatario',
        'apellido destinatario',
        'telefono destinatario',
        'direccion destinario',
        'descripcion',
        'peso kg'      
    ]
    if data:
        Tables.table_vertical(table,data, columns)
             
           
    else:
        print("no se encontro el paquete")
              
def sql_Package_Delete(id):
    status = False
    if Sql.delete('paquete', 'codigo', id) == True:
        status = True
    else:
        status = False
    return status

def sql_Package_Update(table, id, colum):
    status = False   
    Conn =  Database.conexion()
    consulta = Conn.cursor()
    sql = "select * from "+ table + " where " + colum + " = '" + id + "'"   
    consulta.execute(sql)
    data = consulta.fetchone()   
    herdears = obj.columns(table)
    if data:
        for i in range(0, len(herdears)):
            print(i,". "+ "Columna : " +str(herdears[i]).strip("('").strip("',)") + " = " , data[i])      
            print("\n")
        num = int(input("ingrese la columna : "))      
        for i in range(0, len(herdears)):
            if num == i:
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
        print("el paquete no se encuentra")     
    return status

def sql_Package_List():        
    cs = query_extend.extend_package()
    header = ("codigo","nombre_remitente","telefono_remitente","nombre_destinatario","telefono_destinatario")
    #print(header)
    Tables.design_table_columns(cs, header)
    