import os, sys
from Controller.router_to_deliver_controller import RouteSetting
from View.design import Graphics
from View.list import Tables

Route = RouteSetting("ruta_entrega_paquete", "id_ruta")

class RouterToDeliver:
    def __init__(self, table):
        self.__TableName = table   

    def registerRouterToDeliver(self):
        Graphics.header("registrar", self.__TableName)
        if Route.routeInsert() == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
        
    def deleteRouterToDeliver(self):        
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese codigo ruta : ')
        if Route.routeUpdate(Id) == True:
            print("ruta ha sido eliminado")
            os.system ('pause')
        else:
            print("ruta no sido eliminado")
            os.system ('pause')  
        
    def searchRouterToDeliver(self):        
        Graphics.header("Buscar", self.__TableName)
        Id = input("ingrese el codigo camionero para la ruta : ")
        rows, columns =Route.routeSearch(Id)
        Tables.table_vertical(self.__TableName, rows, columns)
        os.system ('pause')    

    def updateRouterToDeliver(self):           
            Graphics.header("actualizar", self.__TableName)
            Id = input("ingrese el cedula del conductor de la ruta : ")
            if Route.routeUpdate(Id) == True:
                print("Registro actualizado")
                os.system ('pause')
            else:
                print("Registro no actualizado")
                os.system ('pause')

    def listRouterToDeliver(self):           
            Graphics.header("lista", self.__TableName)
            rows, columns = Route.routeList()
            Tables.design_table_columns(rows, columns)
            os.system ('pause')
            
            
    