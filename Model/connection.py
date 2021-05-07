import pymysql
import json

class Database:         
    
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
    
    
        
        



            