import os, sys
from Controller import router_to_deliver_controller
from View.design import Graphics

class RouterToDeliver:
    def __init__(self, table):
        self.__TableName = table   

    def registerRouterToDeliver(self):
        Graphics.header("registrar", self.__TableName)
        if router_to_deliver_controller.sql_Router_To_Deliver_Insert(self.__TableName) == True:
            print("Datos han sido ingresados")
            os.system ('pause')        
        else:
            print("datos no han sido ingresados")
            os.system ('pause')
        
    def deleteRouterToDeliver(self):        
        Graphics.header("eliminar", self.__TableName)
        Id = input('ingrese codigo ruta : ')
        if router_to_deliver_controller.sql_Router_To_Deliver_Delete(Id) == True:
            print("ruta ha sido eliminado")
            os.system ('pause')
        else:
            print("ruta no sido eliminado")
            os.system ('pause')  
        
    def searchRouterToDeliver(self):        
        Graphics.header("buscar", self.__TableName)
        Id = input("ingrese el codigo ruta : ")
        router_to_deliver_controller.sql_Router_To_Deliver_Search(self.__TableName,'id_ruta', Id)
        os.system ('pause')    

    def updateRouterToDeliver(self):           
            Graphics.header("actualizar", self.__TableName)
            Id = input("ingrese el codigo de la ruta : ")
            if router_to_deliver_controller.sql_Router_To_Deliver_Update(self.__TableName, Id ,'id_ruta') == True:
                print("Registro actualizado")
                os.system ('pause')
            else:
                print("Registro no actualizado")
                os.system ('pause')

    def listRouterToDeliver(self):           
            Graphics.header("lista", self.__TableName)
            router_to_deliver_controller.sql_Router_To_Deliver_List()
            os.system ('pause')
    