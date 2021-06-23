import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.validation import Validar
from Controller import help

from Controller.write import Console

obj = Query.Sql()
class SettingSender:
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
        tupl = self.__senderInputUpdate(id)
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
        status = False         
        conn = Database().conexion()
        consulta = conn.cursor()
        sql =  query_extend.extend_sender() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)        
        data = consulta.fetchone()
        if data:
            status = True
            conn.close()
            return data, help.getTitles(consulta.description)              
        else:
            status = False
            return status,None, None
        
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
            if i == 0:
                id = Console.inputStringNumber(msg +" "+array[0] + " : ")                
                if val.Register_validation(id, self.__idcolumns) == True:
                    print("ya se encuentra registrado")                    
                    break
                else:
                    lista.append(id)
            if i == 3:                        
                tel = Console.inputStringNumber(msg+" "+array[3]+ " : ")                
                lista.append(tel)                
            elif i == 5:
                city = Console.inputString(msg+" "+array[5]+ " : ")
                lista.append(help.inputCity(city))
            elif i >= 1:
                name = Console.inputString(msg +" " +array[i]+ " : ")
                lista.append(name)
            lista = help.checkElements(lista)
        return lista
        
    def __senderInputUpdate(self,id):
            Conn =  Database.conexion()
            lista = []
            consulta = Conn.cursor()            
            sql = query_extend.extend_sender() + " where " + self.__idcolumns + " = " + "'" + id + "'"
            consulta.execute(sql)
            data = consulta.fetchone()
            if data:
                lista = self.__conditionOne(help.getTitles(consulta.description), data, id)
            else:
                print ("no se encuentra el remitente")                
            return lista
        
    def __conditionOne(self, columns, data, id):            
            lista = []
            print("\n")
            for i in range(0, len(columns)):                    
                print(i, " columna :" ,columns[i], " = ", data[i])
                print("\n")
            option = Console.inputNumber("selecione la columna : ")           
            lista = self.__condtionTwoo(columns, option, id)
            return lista
        
    def __condtionTwoo(self,array, option, id):
        lista = []
        msg = "Ingrese "
        for i in range(0, len(array)):
            if option == 0:
                position = array[option]
                edit = Console.inputNumber(msg + array[option] + ": ")                
                break
            elif option == 3:
                position = array[option]
                edit = Console.inputNumber(msg + array[option] + ": ")                
                break
            elif option == 5 :
                position = array[option]
                edit =  Console.inputString(msg + array[option]+ " : ")
                edit = help.inputCity(edit)            
            elif option > len(array):
                return None                
            elif option == i:
                position = array[option]
                edit = Console.inputString(msg +array[option] + " : ")                
                break
        lista = help.checkElements([self.__table, position, edit, self.__idcolumns, id])            
        return lista
                
         
        
    

        
        
        
                
       
            
            
            
            
            
            
                
            
        
        
    
   
      
        
     
    