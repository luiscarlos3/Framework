import os, sys
from Controller.truck_driver_controller import ControllerDriver
from View.design import Graphics
from View.list import Tables

# an object instance is created
driver = ControllerDriver("camionero", "documento")

# class of view sender controller CRUD results
class truckDriver:
    
    #constructr of the class
    def __init__(self, table):
        self.__TableName = table
           
     # methods register or insert
    def registerTruckDriver(self):
        Graphics.header("Registrar", self.__TableName)
        if driver.truckDriverInsert() == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("Datos no han sido ingresados")
            os.system ('pause')
            
            
    # methods delete result bool true or false    
    def deleteTruckDriver(self):        
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese numero del documento : ')
        if driver.TruckDriverDelete(Id) == True:
            print( self.__TableName + " ha sido eliminado")
            os.system ('pause')
        else:
            print( self.__TableName + " no sido eliminado")
            os.system ('pause')
            
    # methods update recipient boo true or False    
    def updateTruckDriver(self):        
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        if driver.truckDriverUpdate(Id) == True:
            print(  self.__TableName + " se ha actualizado")
            os.system ('pause')
        else:
            print( self.__TableName +" No se ha actualizado")
            os.system ('pause')
            
    # methods search and show search results    
    def searchTruckDriver(self):        
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        status, rows, columns= driver.truckDriverSearch(Id)
        if status == True:
            Tables.table_vertical(rows, columns)
        else:
            print("No se encontro camionero")
        os.system ('pause')
    # methods lists recipient  
    def listTruckDriver(self):       
        Graphics.header("lista", self.__TableName)
        rows, columns = driver.listTruckDriver()
        Tables.design_table_columns(rows, columns)
        os.system ('pause')