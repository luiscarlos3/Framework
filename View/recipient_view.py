import os, sys
from Controller import recipient_controller
from View.design import Graphics


class RecipientView:
    
    def __init__(self, table):
        self.__TableName = table

    def registerRecipient(self):        
        Graphics.header("Registrar", self.__TableName)            
        if recipient_controller.recipientInsert(self.__TableName) == True:
            print("Datos han sido ingresados")
           
            os.system("pause")            
        else:
            print("datos no han sido ingresados")
            os.system("pause")         
        
    def deleteRecipient(self):       
        Graphics.header("Eliminar", self.__TableName)
        Id = input('ingrese numero del documento : ')
        if recipient_controller.recipientDelete(Id) == True:
            print("Destinatario ha sido eliminado")
            os.system("pause")         
        else:
            print("destinatario no sido eliminado")
            os.system("pause")   
       
        
    def updateRecipient(self):      
        Graphics.header("Actualizar", self.__TableName)
        Id = RecipientView.__inputNumber("el documento")
        if recipient_controller.recipientUpdate(self.__TableName, str(Id) ,'documento') == True:
            print("Registro actualizado") 
            os.system("pause")      
        else:
            print("Registro no actualizado")
            os.system("pause")  
        
        
    def searchRecipient(self):      
        Graphics.header("Buscar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        recipient_controller.recipientSearch(self.__TableName,'documento', Id)
        os.system("pause")   
    
    def listRecipient(self):      
        Graphics.header("Lista", self.__TableName)
        recipient_controller.recipientList()
        print("\n")
        os.system("pause")
        
    @staticmethod
    def __inputNumber(value):
        while True:
            var = input("Ingrese " + value + " : ")
            try:
                var = int(var)
                return var
            except ValueError:    
                print("Entrada invalida")
    
    
   
    
         
       
    
         




