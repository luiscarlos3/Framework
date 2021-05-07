import os, sys
from Controller import package_controller
from View.design import Graphics

class Package:
    def __init__(self, table):
        self.__TableName = table
    
    def registerPackage(self):
        Graphics.header("registrar", self.__TableName)
        if package_controller.sql_Package_Insert(self.__TableName) == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
        
    def searchPackage(self):       
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese el codigo del paquete : ")
        package_controller.sql_Package_Search(self.__TableName,'codigo',Id)
        os.system ('pause')
    
    def deletePackage(self):        
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese el codigo del paquete : ')
        if package_controller.sql_Package_Delete(Id) == True:
            print("paquete ha sido eliminado")
            os.system ('pause')
        else:
            print("paquete  no sido eliminado")
            os.system ('pause')
        
    def updatePackage(self):        
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese el codigo del paquete : ")
        if package_controller.sql_Package_Update(self.__TableName, Id ,'codigo') == True:
            print("Registro actualizado")
            os.system ('pause')
        else:
            print("Registro no actualizado")
            os.system ('pause')
            
    def listPackage(self):
        Graphics.header("lista", self.__TableName)
        package_controller.sql_Package_List()
        os.system ('pause')