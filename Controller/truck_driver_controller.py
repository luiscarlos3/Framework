import os, sys
import pymysql
from Model.connection import Database
from Model import Query,query_extend
from Model.Query import Sql
from Controller.validation import Validar
from Controller import help
from Controller.list_controller import Tables

obj = Query.Sql('transporte')

def sql_Truck_Driver_Insert(table):
    status = False 
    val = Validar(table)   
    column = obj.columns(table)
    lista = []
    for x in range(0, len(column)):
        if x == 7:                                    
            name = input("Ingrese " + str(column[7]).strip("('").strip("',)") + " : ")
            if val.controller_city(name) == False:
                print("este municipio no se encuentra")
                break
            else:
                village = help.convert_city(name)
                lista.append(village)
                tupl = tuple(lista)
                if val.Register_validation(tupl[0], "documento") == True:
                    print("ya se encuentra registrado")         
                else:        
                    if Sql.insert(tupl, table) == True:
                        status = True       
                    else:
                        status = False
        
        else:
            Register = input("Ingrese " + str(column[x]).strip("('").strip("',)") + " : ")                    
            lista.append(Register)      
        
    return status

def sql_Truck_Driver_Delete(id):
    status = False
    if Sql.delete('camionero', 'documento', id) == True:
        status = True
    else:
        status = False
    return status



def sql_Truck_Driver_Update(table, id, colum):
    status = False   
    Conn =  Database.conexion()
    consulta = Conn.cursor()    
    sql = query_extend.extend_truck_driver() + " where " + colum  + " = " + "'" + id + "'"
    consulta.execute(sql)
    data = consulta.fetchone()   
    herdears = obj.columns(table)
    if data:
        for i in range(0, len(herdears)):
            print(i,". "+ "Columna : " +str(herdears[i]).strip("('").strip("',)") + " = " , data[i])      
            print("\n")
        num = int(input("seleccione la columna : ")) 
             
        for i in range(0, len(herdears)):
            if num == 7:
                positio = str(herdears[7]).strip("('").strip("',)")
                edit = str(input("ingrese dato para actualizar : "))
                Datos = (table, positio, edit , colum, id)              
                if help.update_city(Datos) == True:
                    status = True
                    break
                else:
                    status = False
                    break
            elif num == i:
                positio = str(herdears[i]).strip("('").strip("',)")
                edit = str(input("ingrese dato para actualizar : "))
                Datos = (table, positio, edit , colum, id)
                print("\n")
                print(Datos)
                print("\n")
                if Sql.update(Datos) == True :
                    status = True
                    break
                else:
                    status = False
                    break              
                  
    else:
        print("la persona no se encuentra")     
    return status

def sql_Truck_Driver_Search(table, colum, id):         
    conn = Database().conexion()
    consulta = conn.cursor()
    sql = query_extend.extend_truck_driver() + " where " + colum + " = " + "'" + id + "'"
    consulta.execute(sql)
    herdears = obj.columns(table)
    data = consulta.fetchone()
    if data:        
        Tables.table_vertical(table, data, herdears)
    else:
        print("no se encontro el destinatario")
        
def sql_Truck_Driver_List():
    cs = query_extend.extend_truck_driver()
    Tables.design_table('camionero', cs)
    