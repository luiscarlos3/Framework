import os, sys
from Controller import truck_driver_controller
from View.design import Graphics

class truckDriver:
    def __init__(self, table):
        self.__TableName = table    

    def registerTruckDriver(self):
        Graphics.header("registrar", self.__TableName)
        if truck_driver_controller.sql_Truck_Driver_Insert(self.__TableName)== True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("Datos no han sido ingresados")
            os.system ('pause')
        
    def deleteTruckDriver(self):        
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese numero del documento : ')
        if truck_driver_controller.sql_Truck_Driver_Delete(Id) == True:
            print( self.__TableName + " ha sido eliminado")
            os.system ('pause')
        else:
            print( self.__TableName + " no sido eliminado")
            os.system ('pause')

    def updateTruckDriver(self):        
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        if truck_driver_controller.sql_Truck_Driver_Update('camionero', Id ,'documento') == True:
            print(  self.__TableName + " se ha actualizado")
            os.system ('pause')
        else:
            print( self.__TableName +" No se ha actualizado")
            os.system ('pause')
        
    def searchTruckDriver(self):        
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        truck_driver_controller.sql_Truck_Driver_Search("camionero",'documento', Id)
        os.system ('pause')
    
    def listTruckDriver(self):       
        Graphics.header("lista", self.__TableName)
        truck_driver_controller.sql_Truck_Driver_List()
        os.system ('pause')