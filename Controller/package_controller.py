import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.PDF import CreatePdf
from Controller.Email import SendEmail
from Controller.write import Console
from Controller import help

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
                self.__executePdfPackage(tupl)
            else:
                status = False       
        return status
            
    def packageSearch(self,id):
        conn = Database().conexion()
        consulta = conn.cursor()
        sql =  query_extend.extend_package_search()+ " where " + self.__idcolumns + " = '" + id + "'" + " or cod_remitente = " + id 
        consulta.execute(sql)
        data = consulta.fetchone()    
        if data:
            return data, help.getTitles(consulta.description)  
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
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extend_packagelist()  
        consulta.execute(sql)
        rows = consulta.fetchall()
        return rows, help.getTitles(consulta.description)           
        
    def __executePdfPackage(self, lista):
        status = False            
        conn = Database().conexion()
        consulta = conn.cursor()        
        sql = query_extend.queryExePdfPackage() + " where "+ self.__idcolumns + " = " + str(lista[0])
        consulta.execute(sql)        
        data = consulta.fetchone()
        if data:           
            info = help.Check(data, consulta.description)            
            CreatePdf.excutePdf("recibo.html", info, 'cod_remitente')
            self.__executeEmail(data[1])                    
        else:
            status = False
        return status
    def __executeEmail(self,id):
        print ("Desea enviar el recibo por correo ")
        print ("Si >> y")
        print ("No >> n")
        options = Console.inputString("Seleccione una opcion : ")
        if options == "y":
            email =  Console.inputString("Ingrese el correo electronico : ")
            if SendEmail.executeEmail(email, id):
                print("Enviado")
            else:
                print("No enviado")          
        return " "         
#----------------------------------------------------------------------*
# help methods avoid overload
#----------------------------------------------------------------------*
    def __inputInsertPackage(self, column):
        msg = "Ingrese"        
        array = help.convertArray(column)
        lista = []
        for i in range(0,len(array)):
            if i == 0:  
                cod = help.codigo()
                print(array[i] +" : ", cod)
                lista.append(cod)                          
            elif i == 2 or i == 3 :                
                var = Console.inputNumber(msg + ' ' + array[i] + " : ")
                lista.append(var)
            elif i == 4:
                var = Console.inputNumber(msg + ' ' + array[i]  + " : ")
                lista.append(var)
            elif i == 5:
                city = Console.inputString(msg+" "+array[i]+ " : ")
                lista.append(help.convert_city(city))
            elif i == 1:
                describe = Console.inputString(msg + ' ' + array[i] + " : ")
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
            
       
        
                               
            
            
            
        
        
        
    

    