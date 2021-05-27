import pymysql
import json

class Database(object):         
    
    @staticmethod  
    def conexion():                       
        try:                    
            mysql = pymysql.connect(
            host = "localhost",
            user = "servidor",
            password = "",
            db = "transporte" 
        )
            return mysql 
                     
        except(pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            
    @staticmethod 
    def namedatabase():
        encoding = 'utf-8'
        x = str(Database.conexion().db, encoding)
        return x
    
    
        
        



            