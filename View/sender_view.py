import os, sys
from Controller.sender_controller import controlSender
from View.design import Graphics
from View.list import Tables
# an object instance is created
sender = controlSender('remitente', 'documento')
# class of view sender controller CRUD results

class Sender:
    #constructr of the class     
    def __init__(self, table):
        self.__TableName = table
          
    # methods register or insert 
    def registerSender(self):
        Graphics.header("registrar", self.__TableName)        
        if sender.senderInsert() == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
            
    # methods register or insert     
    def deleteSender(self):       
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese numero del documento :')
        if sender.senderDelete(Id) == True:
            print("Destinatario ha sido eliminado")
            os.system ('pause')
        else:
            print("destinatario no sido eliminado")
            os.system ('pause')
            
    # methods update recipient boo true or False    
    def updateSender(self):        
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        if sender.senderUpdate(Id) == True:
            print("Registro actualizado")
            os.system ('pause')
        else:
            print("Registro no actualizado")
            os.system ('pause')
            
     # methods search and show search results        
    def searchSender(self):      
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        sender.senderSearch(Id)
        os.system ('pause')
        
     # methods lists recipient
    def listSender(self):        
        Graphics.header("Lista", self.__TableName)
        rows, columns = sender.senderList()       
        print("\n")
        Tables.design_table_columns(rows, columns)
        os.system ('pause')
    
    
         
       
    
         




