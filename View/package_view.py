import os, sys
from Controller.package_controller import ControllerPackage
from View.design import Graphics
from View.list import Tables

# an object instance is created
pack = ControllerPackage('paquete', 'codigo')
# class of view sender controller CRUD results

class Package:
    
    #constructr of the class 
    def __init__(self, table):
        self.__TableName = table
        
    # methods register or insert 
    def registerPackage(self):
        Graphics.header("registrar", self.__TableName)
        if pack.packageInsert() == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
            
    # methods search and show search results             
    def searchPackage(self):       
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese el codigo del paquete : ")
        status, rows, columns = pack.packageSearch(Id)
        if status == True:
            Tables.table_vertical(self.__TableName, rows, columns)
        else:
            print ("No se encontro el paquete")
        os.system ('pause')
        
    # methods delete result bool true or false 
    def deletePackage(self):        
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese el codigo del paquete : ')
        if pack.packageDelete(Id) == True:
            print("paquete ha sido eliminado")
            os.system ('pause')
        else:
            print("paquete  no sido eliminado")
            os.system ('pause')
            
    # methods update recipient boo true or False    
    def updatePackage(self):        
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese el codigo del paquete : ")
        if pack.packageUpdate(Id) == True:
            print("Registro actualizado")
            os.system ('pause')
        else:
            print("Registro no actualizado")
            os.system ('pause')
            
    # methods lists recipient       
    def listPackage(self):
        Graphics.header("lista", self.__TableName)
        rows, columns = pack.packageList()
        print("\n")
        Tables.design_table_columns(rows, columns)
        os.system ('pause')
       