class utilidades:
    
    @staticmethod
    def columnsTruck():
        columns =[
        "matricula",
        "modelo",
        "tipo",
        "potencia",
        "cedula",
        "nombre",
        "apellido",
        "telefono",
        "ciudad del vehiculo"        
        ]
        return columns
    
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
    def columnsShippings():
        colums = ["codigo_envio", 
            "estado", 
            "direccion",
            "cedula destinatario",
            "nombre destinatario",
            "apellido destinatario",
            "cedula remitente",
            "nombre remitente",
            "apellido remitente",
            "codigo paquete",
            "descripcion",
            "peso kg",
            "fecha de envio",
            "fecha de llegada"                
            ]
        return colums
        
    


