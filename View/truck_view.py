import os, sys
from Controller.truck_controller import ControllerTruck
from View.design import Graphics
from Controller.write import Console
from View.list import Tables

# an object instance is created
obj = ControllerTruck("camion", "matricula")

# class of view sender controller CRUD results
class Truck:
    
    #constructr of the class
    def __init__(self, table):
        self.__TableName = table
         
    # methods register or insert
    def registerTruck(self):
        Graphics.header("registrar", self.__TableName)
        id = Console.inputNumber('ingrese el documento del coductor : ')
        if obj.truckInsert(id) == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
            
     # methods delete result bool true or false        
    def deleteTruck(self):        
        Graphics.header("eliminar", self.__TableName)
        Id = input('Ingrese la matricula : ')
        if obj.truckDelete(Id) == True:
            print(self.__TableName + " ha sido eliminado")
            os.system ('pause')
        else:
            print(self.__TableName + " no sido eliminado")
            os.system ('pause')
            
    # methods update recipient boo true or False       
    def updateTruck(self):        
        Graphics.header("actualizar", self.__TableName)
        Id = input("ingrese la matricula : ")
        if obj.truckUpdate(Id) == True:
            print( self.__TableName + " se ha actualizado")
            os.system ('pause')
        else:
            print(self.__TableName + " No se ha actualizado")
            os.system ('pause')
            
    # methods search and show search results  
    def searchTruck(self):        
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese la matricula : ")
        rows, columns =obj.truckSearch(Id)
        Tables.table_vertical(self.__TableName, rows, columns)
        obj.optionPDF()
        os.system ('pause')
        
    # methods lists recipient
    def listTruck(self):       
        Graphics.header("lista",self.__TableName)
        rows, columns = obj.truckList()
        Tables.design_table_columns(rows, columns)
        os.system ('pause')     
       