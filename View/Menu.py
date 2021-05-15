import os, sys
from View.truck_view import Truck
from View.recipient_view import RecipientView
from View.package_view import Package
from View.sender_view import Sender
from View.shipping_view import Shipping
from View.router_to_deliver_view import RouterToDeliver
from View.truckdriver_view import truckDriver
from View import design
from switchlang import switch


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
            1:lambda E='camion':bodyTruck(E),
            2:lambda E='camionero':options(E),
            3:lambda E='destinatario':options(E),
            4:lambda E='envio': options(E),
            5:lambda E='paquete': options(E),
            6:lambda E='remitente': options(E),
            7:lambda E='ruta entrega paquete': options(E)
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
            
        
def bodyShipping(num):
    obj = Shipping("envio")
    pass
    
def bodyTruck(table):
    Quit = False 
    while Quit == False:           
        obj = Truck(table)    
        op = options(table)    
        switch = {
            5:obj.listTruck            
       
        }
        var = switch.get(op, lambda default: print("No se ha reconocido la opcion %s" % op))
        if op == 0:
            break
        else:
            var()
   
                
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
    
    
        
        
        
            
      
    
        
    
    
        


