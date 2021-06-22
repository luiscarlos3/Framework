import os, sys
from Controller.router_to_deliver_controller import RouteSetting
from View.design import Graphics
from View.list import Tables
# an object instance is created
Route = RouteSetting("ruta_entrega_paquete", "cedula_camionero")
# class of view sender controller CRUD results

class RouterToDeliver:
    
    #constructr of the class
    def __init__(self, table):
        self.__TableName = table
         
     # methods register or insert 
    def registerRouterToDeliver(self):
        Graphics.header("registrar", self.__TableName)
        if Route.routeInsert() == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
            
     # methods delete result bool true or false     
    def deleteRouterToDeliver(self):        
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese codigo ruta : ')
        if Route.routeUpdate(Id) == True:
            print("ruta ha sido eliminado")
            os.system ('pause')
        else:
            print("ruta no sido eliminado")
            os.system ('pause')
              
    # methods update recipient boo true or False   
    def searchRouterToDeliver(self):        
        Graphics.header("Buscar", self.__TableName)
        Id = input("ingrese el codigo camionero para la ruta : ")
        rows, columns =Route.routeSearch(Id)
        Tables.table_vertical(self.__TableName, rows, columns)
        Route.optionPDF()
        os.system ('pause') 
           
    # methods search and show search results   
    def updateRouterToDeliver(self):           
            Graphics.header("actualizar", self.__TableName)
            Id = input("ingrese el cedula del conductor de la ruta : ")
            if Route.routeUpdate(Id) == True:
                print("Registro actualizado")
                os.system ('pause')
            else:
                print("Registro no actualizado")
                os.system ('pause')
                
    # methods lists recipient
    def listRouterToDeliver(self):           
            Graphics.header("lista", self.__TableName)
            rows, columns = Route.routeList()
            Tables.design_table_columns(rows, columns)
            os.system ('pause')
            
            
    