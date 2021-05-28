import os, sys
from View.truck_view import Truck
from View.recipient_view import RecipientView
from View.package_view import Package
from View.sender_view import Sender
from View.shipping_view import Shipping
from View.router_to_deliver_view import RouterToDeliver
from View.truckdriver_view import truckDriver
from View import design

draw = design.Graphics()
def presetation():   
    os.system("cls")   
    draw.headerMenu()
    #draw.AppearanceTwoo('camion', 'camionero', 'destinatario', 'envio', 'paquete', 'remitente', 'ruta_entrega_paquete')
    draw.Appearance()
    print("0 salir \n")
    num = int(input("seleccione una opcion : "))   
    if num == 0:           
        print("salir del programa")
        exit()
    else:
        switch = {
            1:lambda E='camion':bodyTruck(E),
            2:lambda E='camionero':bodyTruckDriver(E),
            3:lambda E='destinatario':bodyRecipient(E),
            4:lambda E='envio': bodyShipping(E),
            5:lambda E='paquete': bodyPackage(E),
            6:lambda E='remitente': bodySender(E),
            7:lambda E='ruta entrega paquete': bodyRouterToDeliver(E)
        }                    
        op = switch.get(num, None)
        if op is None:
            print("No se ha reconocido la opcion %s" % num)            
            os.system("pause")
            presetation()
        else:
            op()
                      
       
def options(table):
    Quit = False
    while Quit == False:
        os.system("cls")  
        draw.designToCrud(table)
        print("0 - volver al menu \n")
        num = int(input("seleccione una opcion : "))
        if num == 0 :            
            Quit == True
            presetation()
        else:
           return num           

       
def bodyShipping(table):
    Quit = False    
    while Quit == False:
        obj = Shipping(table)
        op = options(table)
        switch = {
            1: obj.registerShipping,
            2: obj.searchShipping,
            3: obj.Deleteshipping,
            4: obj.updateShipping,
            5: obj.listShipping           
        }
        var = switch.get(op, lambda: "opcion invalida")
        if op == 0:
            Quit = True
        else:
            var()
    
    
def bodyTruck(table):
    Quit = False 
    while Quit == False:           
        obj = Truck(table)    
        op = options(table)    
        switch = {
            1:obj.registerTruck,
            2:obj.searchTruck,
            3:obj.deleteTruck,
            4:obj.updateTruck,
            5:obj.listTruck        
        }
        var = switch.get(op, lambda: "opcion invalida")
        if op == 0:
            Quit = True                        
        else:
            var()
   
                
def bodyTruckDriver(table):
    Quit = False    
    while Quit == False:
        person = truckDriver(table) 
        op = options(table)
        switch = {
         1: person.registerTruckDriver,
         2: person.searchTruckDriver,
         3: person.deleteTruckDriver,
         4: person.updateTruckDriver,
         5: person.listTruckDriver        
        } 
        var = switch.get(op, lambda: "opcion invalida")
        if op == 0:
            Quit = True
        else:
            var()        
    

def bodyRecipient(table):
    Quit = False
    while Quit == False:
        person = RecipientView(table)
        op = options(table)    
        switch = {
            1:person.registerRecipient,
            2:person.searchRecipient,
            3:person.deleteRecipient,
            4:person.updateRecipient,
            5:person.listRecipient
        }
        recipient = switch.get(op, lambda: "opcion invalida")
        if op == 0:
            Quit = True
        else:
            recipient()    
        
def bodyPackage(table):
    Quit = False
    while Quit == False:
        obj = Package(table)
        op = options(table)
        switch = {
            1: obj.registerPackage,
            2: obj.searchPackage,
            3: obj.deletePackage,
            4: obj.updatePackage,
            5: obj.listPackage
        }
        var = switch.get(op, lambda: "opcion invalida")
        if op == 0:
            Quit = True
        else:
            var()    
    
def bodySender(table):
    Quit = False
    while Quit == False:
        person = Sender(table)
        op = options(table)
        switch = {
            1: person.registerSender,
            2: person.searchSender,
            3: person.deleteSender,
            4: person.updateSender,
            5: person.listSender
        }
        var = switch.get(op, lambda: "opcion invalida")
        if op == 0:
            Quit = True
        else:
            var()
                   
def bodyRouterToDeliver(table):
    Quit = False
    while Quit == False:
        route = RouterToDeliver(table)
        op = options(table)
        switch = {
            1: route.registerRouterToDeliver,
            2: route.searchRouterToDeliver,
            3: route.deleteRouterToDeliver,
            4: route.updateRouterToDeliver,
            5: route.listRouterToDeliver
            }
        var = switch.get(op, lambda: "opcion invalida")
        if op == 0:
            Quit = True
        else:
            var()
        
        
    
    
    
        
        
        
            
      
    
        
    
    
        


