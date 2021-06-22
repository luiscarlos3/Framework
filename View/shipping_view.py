import os, sys
from Controller.shipping_controller import controllerShipping
from View.design import Graphics
from View.list import Tables

# an object instance is created
shipping = controllerShipping('envio', 'envio_destinatario', 'envio_remitente')

# class of view sender controller CRUD results
class Shipping:
    
     #constructr of the class
    def __init__(self, table):
        self.__TableName = table
        
     # methods register or insert 
    def registerShipping(self):        
        Graphics.header("Registrar", self.__TableName)
        if shipping.shippingInsert() == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
            
    # methods delete result bool true or false    
    def Deleteshipping(self):      
        Graphics.header("Eliminar", self.__TableName)
        Id = input('ingrese codigo del envio :')
        if shipping.shippingDelete(Id) == True:
            print("envio ha sido eliminado")
            os.system ('pause')
        else:
            print("envio no sido eliminado")
            os.system ('pause')
            
    # methods update recipient boo true or False      
    def updateShipping(self):       
        Graphics.header("Actualizar", self.__TableName)
        Id = input("ingrese el numero del envio : ")
        if shipping.shippingUpdate(Id) == True:
            print("Registro actualizado")
            os.system ('pause')
        else:
            print("Registro no actualizado")
            os.system ('pause')
            
    # methods search and show search results    
    def searchShipping(self):
        Graphics.header("Buscar", self.__TableName)     
        Id = input("Ingrese la cedula del destinatario o remitente : ")
        status,rows,columns = shipping.shippingSearch(Id)      
        if status == True:                        
            Tables.table_vertical(self.__TableName, rows, columns)
            shipping.optionPDF(Id)           
            os.system ('pause')
        else:
            print("No se enconro el destinatario")
            os.system ('pause') 
                  
    # methods lists recipient
    def listShipping(self):       
        Graphics.header("Envio", self.__TableName)
        rows, columns=shipping.shippingList()
        Tables.design_table_columns(rows, columns)
        os.system ('pause')