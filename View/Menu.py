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
    draw.Appearance()
    print("0 salir \n")
    num = int(input("seleccione una opcion : "))   
    if num == 0:           
        print("salir del programa")
        exit()
    else:        
        switch = {
            1:lambda E='camion':options(num, E),
            2:lambda E='camionero':options(num, E),
            3:lambda E='destinatario':options(num, E),
            4:lambda E='envio': options(num, E),
            5:lambda E='paquete': options(num, E),
            6:lambda E='remitente': options(num, E),
            7:lambda E='ruta entrega paquete': options(num, E)
        }                    
        op = switch.get(num, None)
        if op is None:
            print("No se ha reconocido la opcion %s" % num)            
            os.system("pause")
            presetation()
        else:
            op()
        
       
def options(num, table):
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
            print(num)
            switch = {  
                1: lambda E=num : Truck(E),                   
                3: lambda E=num : bodyRecipient(E)      
                
            }
            op = switch.get(num, None)
            if op is None:
                print("No se ha reconocido la opcion %s" % num)            
                os.system("pause")
                presetation()
            else:
                op()
            
            
        
def bodyShipping(num):
    obj = Shipping("envio")
    pass
    
def bodyTruck(num):
    obj = Truck("camion")
    pass
    
                
def bodyTruckDriver(num):
    person = truckDriver("camionero")   
    pass
    

def bodyRecipient(num):
    person = RecipientView('destinatario')    
    switch = {
        1:person.registerRecipient,
        2:person.searchRecipient,
        3:person.deleteRecipient,
        4:person.updateRecipient,
        5:person.listRecipient,
    }
    recipient = switch.get(num, lambda default: print("No se ha reconocido la opcion %s" % num))
    recipient()
        
def bodyPackage(num):
    obj = Package('paquete')
    pass
    
def bodySender(num):
    person = Sender("remitente")
    pass
   
        
def bodyRouterToDeliver(num):    
    route = RouterToDeliver('ruta_entrega_paquete')
    pass
    
    
        
        
        
            
      
    
        
    
    
        


