import os, sys
from Controller import shipping_controller
from View.design import Graphics

class Shipping:
    def __init__(self, table):
        self.__TableName = table

    def registerShipping(self):        
        Graphics.header("registrar", self.__TableName)
        if shipping_controller.sql_Shipping_Insert('envio') == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
        
    def Deleteshipping(self):      
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese codigo del envio :')
        if shipping_controller.sql_Shipping_Delete(Id) == True:
            print("envio ha sido eliminado")
            os.system ('pause')
        else:
            print("envio no sido eliminado")
            os.system ('pause')
        
    def updateShipping(self):       
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese el numero del envio : ")
        if shipping_controller.sql_Shipping_Update(self.__TableName, Id ,'id_envio') == True:
            print("Registro actualizado")
            os.system ('pause')
        else:
            print("Registro no actualizado")
            os.system ('pause')
        
    def searchShipping(self):
        Graphics.header("buscar", self.__TableName)     
        Id = input("ingrese el numero del envio : ")        
        shipping_controller.sql_Search_Shipping(self.__TableName,'id_envio', Id)
        os.system ('pause')
    
    def listShipping(self):       
        Graphics.header("envio", self.__TableName)
        shipping_controller.sql_Shipping_List()
        os.system ('pause')