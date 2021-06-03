import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.validation import Validar
from Controller import help
from Controller.write import Console
from Controller.list_controller import Tables
from Controller.utilis import utilidades

obj = Query.Sql()
class ControllerPackage():
    
    def __init__(self, table, idcolumns):        
        self.__table = table
        self.__idcolumns = idcolumns 

    def packageInsert(self):
        status = False    
        column = obj.columns(self.__table)
        tupl = tuple(self.__inputInsertPackage(column))        
        if not tupl:
            status = False
        else:
            if Sql.insert(self.__table,tupl) == True:
                status = True
            else:
                status = False
        return status
        
    def packageSearch(self,id):
        conn = Database().conexion()
        consulta = conn.cursor()
        sql =  query_extend.extend_package_search()+ " where " + self.__idcolumns + " = '" + id + "'"   
        consulta.execute(sql)
        data = consulta.fetchone()    
        if data:
            Tables.table_vertical(self.__table, data, utilidades.columnsPacket())          
        else:
            print("no se encontro el paquete")
              
    def packageDelete(self,id):        
        return Sql.delete(self.__table, self.__idcolumns, id)
          

    def sql_Package_Update(table, id, colum):
        status = False   
     
        return status

    def packageList(self):        
        cs = query_extend.extend_package()
        header = ("codigo","nombre_remitente","telefono_remitente","nombre_destinatario","telefono_destinatario")
        #print(header)
        Tables.design_table_columns(cs, header)
#----------------------------------------------------------------------*
# help methods avoid overload
#----------------------------------------------------------------------*
    def __inputInsertPackage(self, column):
        msg = "Ingrese"        
        array = help.convertArray(column)
        lista = []
        for i in range(0,len(array)):
            if i is 0:  
                cod = help.codigo()
                print(array[i] +" : ", cod)
                lista.append(cod)                          
            elif i is 2 or i is 3 :                
                var = Console.inputNumber(msg + ' ' + array[i] + " : ")
                lista.append(var)
            elif i is 4:
                var = Console.inputNumber(msg + ' ' + array[i]  + " : ")
                lista.append(var)
            else:
                describe = Console.inputString(msg + ' ' + array[1] + " : ")
                lista.append(describe)
        return lista
    def __inputUpdatePackage(self):
        pass
        
                               
            
            
            
        
        
        
    

    