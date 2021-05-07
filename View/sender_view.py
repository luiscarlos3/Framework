import os, sys
from Controller import sender_controller
from View.design import Graphics

class Sender:
    
    def __init__(self, table):
        self.__TableName = table   
 
    def registerSender(self):
        Graphics.header("registrar", self.__TableName)        
        if sender_controller.sql_Sender_Insert(self.__TableName) == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
        
    def deleteSender(self):       
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese numero del documento :')
        if sender_controller.sql_Sender_Delete(Id) == True:
            print("Destinatario ha sido eliminado")
            os.system ('pause')
        else:
            print("destinatario no sido eliminado")
            os.system ('pause')
        
    def updateSender(self):        
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        if sender_controller.sql_Sender_Update(self.__TableName, Id ,'documento') == True:
            print("Registro actualizado")
            os.system ('pause')
        else:
            print("Registro no actualizado")
            os.system ('pause')
        
    def searchSender(self):      
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        sender_controller.sql_Sender_Search(self.__TableName, 'documento', Id)
        os.system ('pause')
    
    def listSender(self):        
        Graphics.header("lista", self.__TableName)
        sender_controller.sql_Sender_List()
        os.system ('pause')
    
    
         
       
    
         




