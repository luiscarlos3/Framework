import os, sys
from Controller import truck_controller
from View.design import Graphics

class Truck:
    def __init__(self, table):
        self.__TableName = table    

    def registerTruck(self):
        Graphics.header("registrar", self.__TableName)
        id = input('ingrese el documento del coductor : ')
        if truck_controller.sql_Truck_Insert(self.__TableName, id) == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
        
    def deleteTruck(self):        
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese numero del documento : ')
        if truck_controller.sql_Truck_Delete(Id) == True:
            print(self.__TableName + " ha sido eliminado")
            os.system ('pause')
        else:
            print(self.__TableName + " no sido eliminado")
            os.system ('pause')

    def updateTruck(self):        
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        if truck_controller.sql_Truck_Update(self.__TableName, Id, 'matricula') == True:
            print( self.__TableName + " se ha actualizado")
            os.system ('pause')
        else:
            print(self.__TableName + " No se ha actualizado")
            os.system ('pause')
        
    def searchTruck(self):        
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese el numero del documento : ")
        truck_controller.sql_Truck_Search(self.__TableName,'matricula',Id)
        os.system ('pause')
    
    def listTruck(self):       
        Graphics.header("lista",self.__TableName)
        truck_controller.sql_Truck_List()
        os.system ('pause')