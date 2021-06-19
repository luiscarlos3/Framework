import os, sys
from Controller.shipping_controller import controllerShipping
from View.design import Graphics
from View.list import Tables

shipping = controllerShipping('envio', 'id_envio')

class Shipping:
    def __init__(self, table):
        self.__TableName = table

    def registerShipping(self):        
        Graphics.header("registrar", self.__TableName)
        if shipping.shippingInsert() == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
        
    def Deleteshipping(self):      
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese codigo del envio :')
        if shipping.shippingDelete(Id) == True:
            print("envio ha sido eliminado")
            os.system ('pause')
        else:
            print("envio no sido eliminado")
            os.system ('pause')
        
    def updateShipping(self):       
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese el numero del envio : ")
        if shipping.shippingUpdate(Id ) == True:
            print("Registro actualizado")
            os.system ('pause')
        else:
            print("Registro no actualizado")
            os.system ('pause')
        
    def searchShipping(self):
        Graphics.header("buscar", self.__TableName)     
        Id = input("ingrese el numero del envio : ")        
        shipping.shippingSearch(Id)
        os.system ('pause')
    
    def listShipping(self):       
        Graphics.header("envio", self.__TableName)
        rows, columns=shipping.shippingList()
        Tables.design_table_columns(rows, columns)
        os.system ('pause')