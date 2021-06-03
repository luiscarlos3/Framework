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
          

    def packageUpdate(self,id):
        status = False         
        herdears = obj.columns(self.__table)
        columns = help.convertArray(herdears)
        tupl = self.__inputUpdatePackage(columns, id)
        if not tupl:
            status = False
        else:
            if Sql.update(tupl) == True:
                status = True
            else:
                status = False
        return status 
     
       

    def packageList(self):        
        cs = query_extend.extend_packagelist()      
        #print(header)
        Tables.design_table_columns(cs, utilidades.columnsPacketlist())
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
    
    def __inputUpdatePackage(self, column, id):
        Conn =  Database.conexion()
        update = tuple()
        consulta = Conn.cursor()
        sql = query_extend.extend_package() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchone()
        if data:
            update = self.__conditionOne(column, data, id)
        else:
            print("No se encontro el paquete ")
        return update
       
    def __conditionOne(self, columns, data, id):
            msg = "Ingrese" 
            update = tuple()
            print("\n")
            for i in range(0, len(columns)):                    
                print(i, " columna :" ,columns[i], " = " , data[i])
                print("\n")
            option = Console.inputNumber("selecione la columna : ")
            if option >= 0 and option <= 2:
                position = columns[option]
                edit = Console.inputString(msg + ' ' + columns[option] + " : ")          
                update = (self.__table, position, edit, self.__idcolumns, id)
                
            elif option is 4:
                position = columns[option]
                edit = Console.inputNumber(msg + ' ' + columns[option] + " : ")
                update = (self.__table, position, edit, self.__idcolumns, id)
            else:
                print("Opcion invalida")  
           
            return update
            
       
        
                               
            
            
            
        
        
        
    

    