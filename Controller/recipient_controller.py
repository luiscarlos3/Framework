import os
from Model.connection import Database
from Model.Query import Sql
from Model import Query,query_extend
from Controller.validation import Validar
from Controller.write import Console
from Controller import help

#The class is called where the connection to the database
# and the different methods to perform the
# CRUD operations are Query.Sql()

obj = Query.Sql()

# the recipient configuration class controls the crud and
# queries fetched from the database 
# and organize the information

class SettingRecipes:
    # constructr of the class 
    def __init__(self, table, idcolumns):        
        self.__table = table
        self.__idcolumns = idcolumns
              
    # methods controller of insertar 
    def recipientInsert(self):
        status = False      
        column = obj.columns(self.__table)  # method calls the columns of the invoked table      
        tupl = tuple(self.__recipientInput(column)) # method controller input recipient
        if not tupl: # validate if tuple is empty
            status = False
        else:
            if Sql.insert(self.__table, tupl) == True:
                status = True
            else:
                status = False      
        return status
      
     # methods controller of delet
    def recipientDelete(self,id):        
        # it verifies if the data that is in another table is using 
        # it if it is true it cannot be eliminated
        # if it is false it is eliminated        
        if Validar.checkDelete('documento', 'destintario', 'cod_destinatario', 'paquete', id): # mejorar esta parte crear un super metodo que automatize
            print("No se puede eliminar ya que paquete de envio no se ha entregado")
            return False
        else:         
            return Sql.delete(self.__table, self.__idcolumns, id) # delete  the information
            
    # method controller update 
    def recipientUpdate(self, id):
        status = False              
        tupl = self.__recipientInputUpdate(id)       
        if not tupl:
            status = False            
        else:
            if Sql.update(tupl) == True:        
                status = True
            else:
                status = False
        return status
    
    # method recipient search a result 
    def recipientSearch(self,id):         
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.QueryRecipient() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)        
        data = consulta.fetchone()
        if data:
            conn.close()
            return data, help.getTitles(consulta.description)                      
        else:
            print("No se encontro el destinatario")
                   
    #method recipient list    
    def recipientList(self):
        conn = Database().conexion()
        consulta = conn.cursor()        
        sql =  query_extend.QueryRecipient()
        consulta.execute(sql)
        rows = consulta.fetchall()
        conn.close()
        return rows, help.getTitles(consulta.description)   
    #----------------------------------------------------------------------*
    # help methods avoid overload
    #----------------------------------------------------------------------*
    # Control the entry of data in the recipient this way avoids repeating the same data
    # create a list organized with the respective data by columns the method return a list    
    def __recipientInput(self,column):
        msg = "Ingrese"
        val = Validar(self.__table)
        array = help.convertArray(column) # flatten the list as the query returns tuples of tuples
        lista = []
        for i in range(0,len(array)):
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
                lista.append(self.__inputCity(city))                              
            elif i >= 1:
                name = Console.inputString(msg +" " +array[i]+ " : ")
                lista.append(name)                
        return lista
    
    # handler method input update return an ordered
    # tuple by selecting the column you want to edit
    def __recipientInputUpdate(self,id):
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        lista = []           
        sql = query_extend.QueryRecipient() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)              
        data = consulta.fetchone()  
        if data:                        
            lista = self.__conditionUpdate(help.getTitles(consulta.description), data, id)                                                       
        else:
            print("No se encuentra la informacion")                
        return lista
    
    def __conditionUpdate(self, array, data, id):
        lista = []
        for i in range(0, len(array)):                
            print(i, ". "+ "Columna : " + str(array[i])  + " = " + data[i])
            print("\n")
        option = Console.inputNumber("selecione la columna : ")
        lista = self.__conditionOneUpdate(array, option, id)
        return lista        
        
    def __conditionOneUpdate(self, arary,option,id):
        msg = "Ingrese "
        lista = []
        for i in range(0, len(arary)):             
            if option == 0:
                position = arary[option]
                edit = Console.inputNumber(msg + arary[0]+ " : ")
                break                                                                       
            elif option == 3:
                position = arary[option]
                edit = Console.inputNumber(msg + arary[3] + " : ")
                break                                  
            elif option == 5:                    
                position = arary[option]
                edit = Console.inputString(msg + arary[5]+ " : ")
                if help.v(edit) == True:
                    print("No esta el municipio")
                    break
                else:
                    edit = help.v(edit)
                break                                                        
            elif option > len(arary):
                return None
            elif option == i:
                position = arary[option]
                edit = Console.inputString(msg + arary[option] + " : ") 
                
                                           
        lista = [self.__table, position, edit, self.__idcolumns, id]
        return lista
    
             
            
        
        
        
        
           
                    
    
    
   
 
    
   
      
        
     
    