import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.validation import Validar
from Controller import help
from Controller.list_controller import Tables
from Controller.write import Console

obj = Query.Sql()
class controlSender:
    def __init__(self, table, idcolumns):        
        self.__table = table
        self.__idcolumns = idcolumns

    def senderInsert(self):
        status = False
        column = obj.columns(self.__table)
        tupl = tuple(self.__senderInput(column))
        if not tupl:
            status = False
        else:
            if Sql.insert(self.__table, tupl):
                status = True
            else:
                status = False
        return status
    
    def senderUpdate(self, id):
        status = False      
        herdears = obj.columns(self.__table)
        columns = help.convertArray(herdears)
        tupl = self.__senderInputUpdate(columns, id)
        if not tupl:
            status = False
        else:
            if Sql.update(tupl) == True:
                status = True
            else:
                status = False       
        return status 
    
    def senderDelete(self,id):
        if Validar.checkDelete('documento', 'remitente', 'cod_remitente', 'paquete', id):
            print("No se puede eliminar ya que paquete de envio no se ha entregado")
            return False
        else:
            return Sql.delete(self.__table, self.__idcolumns, id)        
         
    
    def senderSearch(self,id):         
        conn = Database().conexion()
        consulta = conn.cursor()
        sql =  query_extend.extend_sender() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)        
        data = consulta.fetchone()
        if data:
            herdears = help.getTitles(consulta.description)        
            Tables.table_vertical(self.__table, data, herdears)   
        else:
            print("no se encontro el remitente")
        
    def senderList(self):
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extend_sender()
        consulta.execute(sql)
        rows = consulta.fetchall()
        return rows, help.getTitles(consulta.description)
    #----------------------------------------------------------------------*
    # help methods avoid overload
    #----------------------------------------------------------------------*
    def __senderInput(self,column):
        msg = "Ingrese"
        val = Validar(self.__table)
        array = help.convertArray(column)
        lista = []
        for i in range(0, len(array)):
            if i is 0:
                id = Console.inputStringNumber(msg +" "+array[0] + " : ")                
                if val.Register_validation(id, self.__idcolumns) == True:
                    print("ya se encuentra registrado")                    
                    break
                else:
                    lista.append(id)
            if i is 3:                        
                tel = Console.inputStringNumber(msg+" "+array[3]+ " : ")                
                lista.append(tel)                
            elif i is 5:
                city = Console.inputString(msg+" "+array[5]+ " : ")
                lista.append(help.convert_city(city))
            elif i >= 1:
                name = Console.inputString(msg +" " +array[i]+ " : ")
                lista.append(name)
        return lista
        
    def __senderInputUpdate(self,column,id):
            Conn =  Database.conexion()
            update = tuple()
            consulta = Conn.cursor()            
            sql = query_extend.extend_sender() + " where " + self.__idcolumns + " = " + "'" + id + "'"
            consulta.execute(sql)
            data = consulta.fetchone()
            if data:
                update = self.__conditionOne(column, data, id)
            else:
                print ("no se encuentra el remitente")                
            return update
        
    def __conditionOne(self, columns, data, id):            
            update = tuple()
            print("\n")
            for i in range(0, len(columns)):                    
                print(i, " columna :" ,columns[i], " = ", data[i])
                print("\n")
            option = Console.inputNumber("selecione la columna : ")           
            update = self.__condtionTwoo(columns, option, id)
            return update
        
    def __condtionTwoo(self,array, option, id):
        update = tuple()
        msg = "Ingrese"
        for i in range(0, len(array)):
            if option is 0:
                position = array[0]
                edit = Console.inputNumber(msg + " " + array[0] + ": ")
                update = (self.__table, position, edit, self.__idcolumns, id)
                break
            elif option is 3:
                position = array[3]
                edit = Console.inputNumber(msg + " " + array[3] + ": ")
                update = (self.__table, position, edit, self.__idcolumns, id )
                break
            elif option is 5 :
                position = array[5]
                edit = edit = Console.inputString(msg +" "+array[5]+ " : ")
                if help.convert_city(edit) == True :
                    print("No esta el municipio")
                    break
                else:
                    edit = help.v(edit)
                    update = (self.__table, position, edit, self.__idcolumns, id)
                    break
            elif option == i:
                position = array[option]
                edit = Console.inputString(msg +" "+array[option] + " : ")
                update = (self.__table, position, edit, self.__idcolumns, id)
                break              
        return update
                
         
        
    

        
        
        
                
       
            
            
            
            
            
            
                
            
        
        
    
   
      
        
     
    