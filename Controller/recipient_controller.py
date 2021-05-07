import pymysql
import os, sys
from Model.connection import Database
from Model.Query import Sql
from Model import Query,query_extend
from Controller.validation import Validar
from Controller.list_controller import Tables
from Controller.decoration import Decorador
obj = Query.Sql('transporte')

def recipientInsert(table):
    status = False      
    column = obj.columns(table)
    var = Decorador(table, "documento")  
    tupl = tuple(var.recipientInput(column))
    if Sql.insert(table, tupl) == True:
        status = True
    else:
        status = False        
    return status    

def recipientDelete(id):
    status = False      
    if Sql.delete('destinatario', 'documento', id) == True:
        status = True
    else:
        status = False
    return status

def recipientUpdate(table, id, colum):
    status = False
    column = obj.columns(table)
    var = Decorador(table, colum)    
    tupl = var.recipientInputUpdate(column, id)
    if Sql.update(tupl) == True:
        status = True
    else:
        status = False
    return status
 
def recipientSearch(table, colum, id):         
    conn = Database().conexion()
    consulta = conn.cursor()
    sql = query_extend.extend_addressee() + " where " + colum + " = " + "'" + id + "'"
    consulta.execute(sql)
    herdears = obj.columns(table)
    data = consulta.fetchone()
    if data:
        Tables.table_vertical('destinatario',data,herdears)     
    else:
        print("no se encontro el destinatario")
        
def recipientList():
    cs =  query_extend.extend_addressee()
    Tables.design_table('destinatario', cs)
  
 
    
   
      
        
     
    