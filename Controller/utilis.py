class utilidades:    
    
    
    @staticmethod    
    def columnsPacket():
        columns = [
        'codigo',
        'cedula remitente',
        'nombre remitente',
        'apellido remitente',
        'telefono remitente',
        'direccion remitente', 
        'cedula destinatario',
        'nombre destinatario',
        'apellido destinatario',
        'telefono destinatario',
        'direccion destinario',
        'descripcion',
        'peso kg'      
    ]
        return columns
    
    @staticmethod 
    def columnsPacketlist():
        columns = [
        "codigo",
        "descripcion",
        "nombre_remitente",
        "telefono_remitente",
        "nombre_destinatario",
        "telefono_destinatario"            
        ]
        return columns    
   
    
    @staticmethod
    def ColumnsShippingslist():
        columns = ["codigo_envio", 
                   "estado", 
                   "direccion",
                   "cedula destinatario",
                   "cedula remitente",
                   "correo",
                   "codigo paquete"]
        return columns
    
    @staticmethod
    def columnsSearchRoute():
        colums = ["codigo ruta",               
             "cedula camionero", 
             "nombre camionero",
             "apellido camionero",
             "telefono",
             "matricula vehiculo",
             "tipo de vehiculo",
             "fecha inicio de entrega", 
             "fecha final de entrega",
             "estado",
             "ciudad",
             "codigo de envio"]        
        return colums
    
    @staticmethod
    def columnsListRoute():
        columns = ["departamento", 
                   "ciudad", 
                   "codigo ruta",
                   "cedula camionero", 
                   "matricula", 
                   "fecha inicio entrega", 
                   "fecha fin entrega"]
        return columns
    
         
        
        
    


