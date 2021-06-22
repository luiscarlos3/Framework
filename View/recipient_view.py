import os, sys
from Controller.recipient_controller import SettingRecipes
from View.design import Graphics
from Controller.write import Console
from View.list import Tables
# an object instance is created
recipient = SettingRecipes('destinatario', 'documento')
# class of view recipiente controller CRUD results
class RecipientView:    
   
    #constructr of the class 
    def __init__(self, table):
        self.__table = table
         
    # methods register or insert 
    def registerRecipient(self):                
        Graphics.header("Registrar", self.__table)        
        if recipient.recipientInsert() == True:                              
            print("Datos han sido ingresados")           
            os.system("pause")            
        else:
            print("datos no han sido ingresados")
            os.system("pause")
                     
    # methods delete result bool true or false   
    def deleteRecipient(self):       
        Graphics.header("Eliminar", self.__table)
        Id = Console.inputNumber('ingrese numero del documento : ')
        if recipient.recipientDelete(Id) == True:
            print("Destinatario ha sido eliminado")
            os.system("pause")         
        else:
            print("destinatario no sido eliminado")
            os.system("pause")
             
    # methods update recipient boo true or False
    def updateRecipient(self):      
        Graphics.header("Actualizar", self.__table)
        Id = input("ingrese el documento : ")
        if recipient.recipientUpdate(str(Id)) == True:
            print("Registro actualizado") 
            os.system("pause")      
        else:
            print("Registro no actualizado")
            os.system("pause")
                 
    # methods search and show search results    
    def searchRecipient(self):      
        Graphics.header("Buscar", self.__table)
        Id = input("ingrese el numero del documento : ")
        status, rows , columns = recipient.recipientSearch(Id)
        if status == True:
            Tables.table_vertical(self.__table, rows, columns)
        else:
            print("No se encuentra el destinatario")      
        os.system("pause")
         
    # methods lists recipient 
    def listRecipient(self):      
        Graphics.header("Lista", self.__table)
        rows, columns = recipient.recipientList()        
        print("\n")
        Tables.design_table_columns(rows, columns)
        os.system("pause")
        
    
    
    
   
    
         
       
    
         




