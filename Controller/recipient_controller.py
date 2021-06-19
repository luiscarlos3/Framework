import pymysql
import os, sys
from Model.connection import Database
from Model.Query import Sql
from Model import Query,query_extend
from Controller.validation import Validar
from Controller.write import Console
from Controller import help

obj = Query.Sql()
class ControllerRecipes:
    
    def __init__(self, table, idcolumns):
        
        self.__table = table
        self.__idcolumns = idcolumns        
    
    def recipientInsert(self):
        status = False      
        column = obj.columns(self.__table)        
        tupl = tuple(self.__recipientInput(column))
        if not tupl:
            status = False
        else:
            if Sql.insert(self.__table, tupl) == True:
                status = True
            else:
                status = False      
        return status    

    def recipientDelete(self,id):
        # mejorar esta parte crear un super metodo que automatize
        if Validar.checkDelete('documento', 'destintario', 'cod_destinatario', 'paquete', id):
            print("No se puede eliminar ya que paquete de envio no se ha entregado")
            return False
        else:         
            return Sql.delete(self.__table, self.__idcolumns, id)            

    def recipientUpdate(self, id):
        status = False
        column = obj.columns(self.__table)         
        tupl = self.__recipientInputUpdate(column, id)       
        if not tupl:
            status = False            
        else:
            if Sql.update(tupl) == True:        
                status = True
            else:
                status = False
        return status
 
    def recipientSearch(self,id):         
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extend_addressee() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)        
        data = consulta.fetchone()
        if data:
            return data, help.getTitles(consulta.description)           
        else:
            print("no se encontro el destinatario")
        
    def recipientList(self):
        conn = Database().conexion()
        consulta = conn.cursor()        
        sql =  query_extend.extend_addressee()
        consulta.execute(sql)
        rows = consulta.fetchall()
        return rows, help.getTitles(consulta.description)    
    #----------------------------------------------------------------------*
    # help methods avoid overload
    #----------------------------------------------------------------------*     
    def __recipientInput(self,column):
        msg = "Ingrese"
        val = Validar(self.__table)
        array = self.__convertArray(column)
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
    
    def __recipientInputUpdate(self,colum,id):       
        msg = "Ingrese"
        update = tuple()       
        arary = self.__convertArray(colum)        
        sql = query_extend.extend_addressee() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        crt = Validar(self.__table)      
        data = crt.searchData(sql)        
        if data:                        
            for i in range(0, len(arary)):                
                print(i, ". "+ "Columna : " + str(arary[i])  + " = " + data[i])
                print("\n")
            option = Console.inputNumber("selecione la columna : ")
            for i in range(0, len(arary)):
                if option == 0:
                    position = arary[0]
                    edit = Console.inputNumber(msg +" "+arary[0]+ " : ")
                    update = (self.__table, position, edit, self.__idcolumns, id )
                                                           
                elif option == 3:
                    position = arary[3]
                    edit = Console.inputNumber(msg +" "+arary[3] + " : ")
                    update = (self.__table, position, edit, self.__idcolumns, id )
                    
                elif option == 5:                    
                    position = arary[5]
                    edit = Console.inputString(msg +" "+arary[5]+ " : ")
                    edit = self.__inputCity(edit)                                  
                    update = (self.__table, position, edit, self.__idcolumns, id)        
                                   
                elif option == i:
                    position = arary[option]
                    edit = Console.inputString(msg +" "+arary[option] + " : ")
                    update = (self.__table, position, edit, self.__idcolumns, id)                    
                                                        
        else:
            print("No se encuentra la informacion")                
        return update         
                    
    def __convertArray(self,array):
        lista= []
        for i in range(len(array)):
            for j in range(len(array[i])):
                lista.append(array[i][j])
        return lista
    
    def __inputCity(self, name):
        village = 0       
        if Validar.controller_city(name) == False:                        
            print("este municipio no se encuentra")
            os.system("pause")
        else:
            village = help.convert_city(name)
        return village
  
 
    
   
      
        
     
    