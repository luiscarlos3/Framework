from Model.Query import Sql
import os, sys
from Controller.truck_controller import ControllerTruck
from View.design import Graphics

obj = ControllerTruck("camion", "matricula")
class Truck:
    def __init__(self, table):
        self.__TableName = table    

    def registerTruck(self):
        Graphics.header("registrar", self.__TableName)
        id = input('ingrese el documento del coductor : ')
        if obj.truckInsert(id) == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
        
    def deleteTruck(self):        
        Graphics.header("eliminar", self.__TableName)
        Id = input('Ingrese la matricula : ')
        if obj.truckDelete(Id) == True:
            print(self.__TableName + " ha sido eliminado")
            os.system ('pause')
        else:
            print(self.__TableName + " no sido eliminado")
            os.system ('pause')
            
    def updateTruck(self):        
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese la matricula : ")
        if obj.truckUpdate(Id) == True:
            print( self.__TableName + " se ha actualizado")
            os.system ('pause')
        else:
            print(self.__TableName + " No se ha actualizado")
            os.system ('pause')
        
    def searchTruck(self):        
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese la matricula : ")
        obj.truckSearch(Id)
        os.system ('pause')
    
    def listTruck(self):       
        Graphics.header("lista",self.__TableName)        
        obj.truckList()
        os.system ('pause')