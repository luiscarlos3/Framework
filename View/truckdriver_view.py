import os, sys
from Controller.truck_driver_controller import ControllerDriver
from View.design import Graphics

driver = ControllerDriver("camionero", "documento")

class truckDriver:
    
    def __init__(self, table):
        self.__TableName = table    

    def registerTruckDriver(self):
        Graphics.header("Registrar", self.__TableName)
        if driver.truckDriverInsert() == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("Datos no han sido ingresados")
            os.system ('pause')
        
    def deleteTruckDriver(self):        
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese numero del documento : ')
        if driver.TruckDriverDelete(Id) == True:
            print( self.__TableName + " ha sido eliminado")
            os.system ('pause')
        else:
            print( self.__TableName + " no sido eliminado")
            os.system ('pause')

    def updateTruckDriver(self):        
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        if driver.truckDriverUpdate(Id) == True:
            print(  self.__TableName + " se ha actualizado")
            os.system ('pause')
        else:
            print( self.__TableName +" No se ha actualizado")
            os.system ('pause')
        
    def searchTruckDriver(self):        
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        driver.truckDriverSearch(Id)
        os.system ('pause')
    
    def listTruckDriver(self):       
        Graphics.header("lista", self.__TableName)
        driver.listTruckDriver()
        os.system ('pause')