def extend_shipping():    
    Querys = """
    select id_envio as codigo_envio, 
    estado,     
    direccion,
    envio_destinatario as cedula_destinatario,    
    envio.envio_remitente as cedula_remitente,    
    id_paquete as codigo_paquete    
    from envio    
    inner join destinatario on envio.envio_destinatario = destinatario.documento
    inner join remitente on envio.envio_remitente = remitente.documento
    inner join paquete on envio.id_paquete = paquete.codigo;
    """ 
    return Querys

def extend_truck():
    Querys = """
    select
	matricula, 
    modelo,
    tipo,
    potencia, 
    doc_camionero,  
    municipios.municipio
    from camion   
    inner join municipios on camion.registro_matricula = municipios.id_municipio   
    """
    return Querys

def extend_addressee():
    Querys = """
    select documento,
    nombre,
    apellido, 
    telefono, 
    direccion_destinatario,
    municipios.municipio as ciudad 
    from destinatario 
    inner join municipios on destinatario.ciudad = municipios.id_municipio
    """
    return Querys
def extend_sender():
    Querys = """ select documento,
    nombre, 
    apellido, 
    teléfono, 
    direccion_remitente,
    municipios.municipio as ciudad 
    from remitente 
    inner join municipios on remitente.ciudad = municipios.id_municipio    
    """
    return Querys

def extend_truck_driver():
    Querys = """ select documento,
    nombre_camionero, 
    apellido_camionero, 
    telefono, 
    direccion_camionero,
    salario, 
    fecha_nacimiento,
    municipios.municipio
    from camionero 
    inner join municipios on camionero.ciudad = municipios.id_municipio
    """ 
    return Querys

def extend_package():
    Querys= """
    select codigo, remitente.nombre as nombre_remitente,
    remitente.teléfono as telefono_remitente,
    destinatario.nombre as nombre_destinatario,
    destinatario.teléfono as telefono_destinatario
    from paquete 
    inner join remitente on paquete.cod_remitente = remitente.documento 
    inner join destinatario on paquete.cod_destinatario = destinatario.documento
    """
    return Querys

def extend_package_search():
    Querys= """
     select codigo,
    remitente.documento as cedula_remitente,
	remitente.nombre as nombre_remitente,
    remitente.apellido as apellido_remitente,
    remitente.teléfono as telefono_remitente,
    remitente.direccion_remitente as direccion_remitente,    
    destinatario.documento as cedula_destianatario,
    destinatario.nombre as nombre_destinatario,
    destinatario.apellido as apellido_destinatario,
    destinatario.teléfono as telefono_destinatario,
    destinatario.direccion_destinatario as direccion_destinatario,
    descripcion,
    peso_kg    
    from paquete 
    inner join remitente on paquete.cod_remitente = remitente.documento 
    inner join destinatario on paquete.cod_destinatario = destinatario.documento
    """
    return Querys
    

def extend_router_to_deliver():
    Querys= """ 
    SELECT
	departamento.nombre_departamento, 
	municipios.municipio, 
	ruta_entrega_paquete.id_ruta, 
	ruta_entrega_paquete.doc_camionero, 
	ruta_entrega_paquete.matricula_camion, 
	ruta_entrega_paquete.fec_ini_entrega, 
	ruta_entrega_paquete.fec_fin_entrega
FROM
	departamento
	INNER JOIN
	municipios
	ON 
		departamento.codigo = municipios.departamento_id
	INNER JOIN
	ruta_entrega_paquete
	ON 
		municipios.id_municipio = ruta_entrega_paquete.ciudad
    """
    return Querys

def extend_router_to_deliver_search():
    Querys = """ 
    select 
    id_ruta, 
    ruta_entrega_paquete.doc_camionero,
    camionero.nombre_camionero,
    camionero.apellido_camionero,
    camionero.telefono,
    matricula_camion,
    camion.tipo as tipo_camion,
    fec_ini_entrega, 
    fec_fin_entrega, 
    estado,
    municipios.municipio as ciudad, 
    envio_ruta
    from ruta_entrega_paquete
    inner join municipios on ruta_entrega_paquete.ciudad = municipios.id_municipio
    inner join camionero on ruta_entrega_paquete.doc_camionero = camionero.documento
    inner join camion on ruta_entrega_paquete.matricula_camion = camion.matricula    
    """
    return Querys

def extend_shipping_search():
    Querys = """ 
    select id_envio as codigo_envio, 
    estado,     
    direccion,
	envio_destinatario as cedula_destinatario,    
    destinatario.nombre as nombre_destinatario,
	destinatario.apellido as nombre_destinatario,
    envio.envio_remitente as cedula_remitente,
    remitente.nombre as nombre_remitente,
    remitente.apellido as apellido_remitente,    
    id_paquete as codigo_paquete,
    paquete.descripcion,
    paquete.peso_kg,
    fecha_envio,
    fecha_llegada
    from envio    
    inner join destinatario on envio.envio_destinatario = destinatario.documento
    inner join remitente on envio.envio_remitente = remitente.documento
    inner join paquete on envio.id_paquete = paquete.codigo   
    """
    return Querys


    
    