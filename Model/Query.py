import os, sys
import pymysql
from Model.connection import Database
class Sql:     
    def __init__(self, db):        
        self._db = db        
    
    def columns(self,tables):
        Conn =  Database.conexion()        
        sql = Conn.cursor()
        sql.execute('SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA  LIKE ' + "'"+self._db+"'" + 'AND TABLE_NAME = ' + "'" + tables + "'" )
        data = sql.fetchall()    
        return data   
   
    def name_Table(self):        
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        consulta.execute("SELECT table_name as nombre FROM information_schema.tables WHERE table_schema = " + "'"+ "transporte" + "'"+" and (table_name  = 'paquete' or table_name = 'camion' or table_name = 'camionero' or table_name = 'destinatario' or table_name = 'ruta_entrega_paquete' or table_name = 'remitente' or table_name = 'envio')")
        data = consulta.fetchall()    
        return data
    
    @staticmethod
    def select_Table(table):
        con = Database.conexion()
        sql = con.cursor()
        sql.execute("select * from " + table)
        data = sql.fetchall()
        for i in range(0, len(data)):
            print(i, " : ", data[i], "\n")
                
    @staticmethod
    def insert(table,tupla):        
        status = False    
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        sql = "insert into "+ table+ " values " + str(tupla)
        consulta.execute(sql)
        Conn.commit()
        if consulta.rowcount == 1:            
            status = True
        else:
            status = False           
        return status
    
    @staticmethod
    def delete(table, colum, id):
        status = False       
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        sql = "delete from " + table + " where " + colum + " = " + "'" + str(id)  + "'"
        consulta.execute(sql)
        Conn.commit()
        if consulta.rowcount == 1:
            status = True  
        else:
            status = False
        return status
    
    @staticmethod
    def update(Data):
        status = False
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        sql = "update  " + Data[0] + " set " + Data[1] + " = " + "'" + str(Data[2])+"'" + " where " + Data[3] + " = " + "'" + str(Data[4]) + "'"
        consulta.execute(sql)
        Conn.commit()
        if  consulta.rowcount == 1:
            status = True
        else:
            status = False 
        return status
    
    @staticmethod
    def lits_Select_Table_Extend(cs):
        con = Database.conexion()
        sql = con.cursor()
        sql.execute(cs)
        data = sql.fetchall()  
        return data
   
    
     
    def search(table,colum, id):
        status = False
        con = Database.conexion()
        sql = con.cursor()
        var = "select * from " + table + " where " + colum + " = " + "'" +  str(id) + "'" 
        sql.execute(var)
        data = sql.fetchone()
        if data:
            status = True
        else:
            status = False    
        return status
    
    
        
    


