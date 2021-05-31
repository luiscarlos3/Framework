import os, sys
from Controller.sender_controller import controlSender
from View.design import Graphics

sender = controlSender('remitente', 'documento')

class Sender:    
    def __init__(self, table):
        self.__TableName = table   
 
    def registerSender(self):
        Graphics.header("registrar", self.__TableName)        
        if sender.senderInsert() == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
        
    def deleteSender(self):       
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese numero del documento :')
        if sender.senderDelete(Id) == True:
            print("Destinatario ha sido eliminado")
            os.system ('pause')
        else:
            print("destinatario no sido eliminado")
            os.system ('pause')
        
    def updateSender(self):        
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        if sender.senderUpdate(Id) == True:
            print("Registro actualizado")
            os.system ('pause')
        else:
            print("Registro no actualizado")
            os.system ('pause')
        
    def searchSender(self):      
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        sender.senderSearch(Id)
        os.system ('pause')
    
    def listSender(self):        
        Graphics.header("lista", self.__TableName)
        sender.senderList()
        os.system ('pause')
    
    
         
       
    
         




