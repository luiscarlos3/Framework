import os, sys
from Controller.recipient_controller import ControllerRecipes
from View.design import Graphics
from Controller.write import Console

recipient = ControllerRecipes('destinatario', 'documento')

class RecipientView:    
    
    def __init__(self, table):
        self.__table = table  

    def registerRecipient(self):                
        Graphics.header("Registrar", self.__table)            
        if recipient.recipientInsert(self.__table) == True:                              
            print("Datos han sido ingresados")           
            os.system("pause")            
        else:
            print("datos no han sido ingresados")
            os.system("pause")         
        
    def deleteRecipient(self):       
        Graphics.header("Eliminar", self.__table)
        Id = Console.inputNumber('ingrese numero del documento : ')
        if recipient.recipientDelete(Id) == True:
            print("Destinatario ha sido eliminado")
            os.system("pause")         
        else:
            print("destinatario no sido eliminado")
            os.system("pause")   
       
        
    def updateRecipient(self):      
        Graphics.header("Actualizar", self.__table)
        Id = input("ingrese el documento : ")
        if recipient.recipientUpdate(str(Id)) == True:
            print("Registro actualizado") 
            os.system("pause")      
        else:
            print("Registro no actualizado")
            os.system("pause")  
        
        
    def searchRecipient(self):      
        Graphics.header("Buscar", self.__table)
        Id = input("ingrese el numero del documento : ")
        recipient.recipientSearch(Id)
        os.system("pause")   
    
    def listRecipient(self):      
        Graphics.header("Lista", self.__table)
        recipient.recipientList()
        print("\n")
        os.system("pause")
        
    
    
    
   
    
         
       
    
         




