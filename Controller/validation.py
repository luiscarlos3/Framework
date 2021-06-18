import pymysql
from Model.connection import Database

class Validar:
    def __init__(self, table):
        self.__TableName = table
        
    def Register_validation(self, id, colmuns):
        status = False     
        try:                   
            Conn =  Database.conexion()
            consulta = Conn.cursor()
            sql = 'select * from %s' % self.__TableName + ' where '+ colmuns + ' = ' + "'"+'%s'%id+"'"
            consulta.execute(sql)
            Result = consulta.fetchone()       
            if Result:
                status=True
            else:
                status = False                                
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
                print("Ocurrió un error al validar: ", e)         
        return status
    
    def searchData(self,sql):        
        Conn =  Database.conexion()
        consulta = Conn.cursor()  
        consulta.execute(sql)
        Data = consulta.fetchone()
        return Data       
    
    @staticmethod
    def validation_truck_driver(table,id,colmuns):
        status = False
        try:                   
            Conn =  Database.conexion()
            consulta = Conn.cursor()
            sql = 'select * from %s' % table + ' where '+ colmuns + ' = %s'%id           
            consulta.execute(sql)
            Result = consulta.fetchone()
            if Result:
                status=True
            else:
                status = False                                
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al validar estamos aca : ", e)                     
        return status
    
    @staticmethod
    def controller_city(city):
        status = False
        try:                   
            Conn =  Database.conexion()
            consulta = Conn.cursor()
            sql = 'select * from municipios where municipio = ' + "'" + city + "'"
            consulta.execute(sql)
            Result = consulta.fetchone()
            if Result:
                status = True
            else:
                status = False       
                                     
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al validar: ", e)         
        return status
    
    @staticmethod
    def validation_city(Data):
        status = False    
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        sql = "select * from municipios where municipio = " + "'"+ Data + "'"
        consulta.execute(sql)
        data = consulta.fetchone()
        if data:
            status = True
        else:
            status = False 
        return status
    
    @staticmethod
    def checkDelete(*args):
        status = False
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        sql = "select " + args[0]+" from "+ args[1]+ " where " + args[0] + "= (select " + args[2]+ " from " + args[3]+ " where " + args[2] +" = '" + args[4] + "'" + ")"
        consulta.execute(sql)
        data = consulta.fetchone()
        if data:
            status = True
        else:
            status = False        
        return status
        
         
         
    
    
    
               
            
        
        
                    
        
        
        
        
                    
            
        
    
    
    

       
    
    
    