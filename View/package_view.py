import os, sys
from Controller.package_controller import ControllerPackage
from View.design import Graphics
from View.list import Tables

pack = ControllerPackage('paquete', 'codigo')

class Package:
    def __init__(self, table):
        self.__TableName = table
    
    def registerPackage(self):
        Graphics.header("registrar", self.__TableName)
        if pack.packageInsert() == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
        
    def searchPackage(self):       
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese el codigo del paquete : ")
        rows, columns = pack.packageSearch(Id)
        Tables.table_vertical(self.__TableName, rows, columns)
        os.system ('pause')
    
    def deletePackage(self):        
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese el codigo del paquete : ')
        if pack.packageDelete(Id) == True:
            print("paquete ha sido eliminado")
            os.system ('pause')
        else:
            print("paquete  no sido eliminado")
            os.system ('pause')
        
    def updatePackage(self):        
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese el codigo del paquete : ")
        if pack.packageUpdate(Id) == True:
            print("Registro actualizado")
            os.system ('pause')
        else:
            print("Registro no actualizado")
            os.system ('pause')
            
    def listPackage(self):
        Graphics.header("lista", self.__TableName)
        rows, columns = pack.packageList()
        print("\n")
        Tables.design_table_columns(rows, columns)
        os.system ('pause')
       