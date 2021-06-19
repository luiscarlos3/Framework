import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.write import Console
from Controller import help
from Controller.list_controller import Tables
from Controller.utilis import utilidades
from Controller.PDF import CreatePdf

obj = Query.Sql()
class RouteSetting:
    def __init__(self, table, idcolumns):        
        self.__table = table
        self.__idcolumns = idcolumns

    def routeInsert(self):
        status = False        
        column = obj.columns(self.__table)  
        tupl = tuple(self.__inputTheRoute(column))  
        print(tupl)
        if not tupl:
            status = False      
        else:
            if Sql.insert(self.__table, tupl) == True:
                status = True       
            else:
                status = False    
        return status

    def routeDelete(self,id):            
        return Sql.delete(self.__table, self.__idcolumns, id)             

    def routeSearch(self,id):
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extend_router_to_deliver_search() + " where " + " cedula_camionero " + " = " + "'" + id + "'"
        consulta.execute(sql)    
        data = consulta.fetchall()        
        if data:
            Title = help.getTitles(consulta.description)                     
            Tables.table_vertical(self.__table, data, Title)
            self.__optionPDF()
        else:
            print("no se encontro la ruta ")

    def routeUpdate(self, id):
        status = False        
        columns = ["cedula_camionero", "envio_ruta", "estado", "ciudad"]
        tupl = self.__inputUpdateTheRoute(columns, id)
        if not tupl:
            status = False
        else:
            if Sql.update(tupl) == True:
                status = True
            else:
                status = False              
        return status
    
    def __optionPDF(self):
        print("¿ Desea generar reporte general de vehiculos ?")
        print("Si >> y")
        print("No >> n")
        op = Console.inputString("selecione una opcion ")
        if op == "y":
            self.__generaPdfRoute()
        return " "
    
    def __testResultList(self,valor, titulos):        
        if not valor:
            valor = ( ('atx234', 1997, 'volqueta', '255', '3445', 'luis', 'silva', '12345', 'Corozal'),
            ('ijq24d', 2007, 'turbo', '255', '3445', 'luis', 'silva', '12345', 'bogota'))    
        registros = {} # opcional
        lista = [] # recursividad fila 
        valores_lista = list(valor)# 
        #titulos = list(valor)[0]
        #titulos = ['matricula', 'modelo', 'tipo', 'potencia', 'doc_camionero', 'nombre_camionero', 'apellido_camionero', 'telefono','municipio']
        registros["titulos"] = titulos
        for x in range(0, len(valores_lista)): 
            lista = list(valores_lista[x])
            registros[x+1] = lista
        return registros
    
    def __generaPdfRoute(self):                   
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extend_router_to_deliver_search()    
        consulta.execute(sql)
        data = consulta.fetchall()
        titulos = help.getTitles(consulta.description)             
        if data:
            data = self.__testResultList(data, titulos)
            CreatePdf.excutePdfReport("Reportes.html",data,"Rutas de envio")
        return" "  

    def routeList(self):
        conn = Database().conexion()
        consulta = conn.cursor()        
        sql =  query_extend.extend_router_to_deliver()  
        consulta.execute(sql)
        rows = consulta.fetchall()             
        return rows, help.getTitles(consulta.description)
    
#----------------------------------------------------------------------*
# help methods avoid overload
#----------------------------------------------------------------------*
    def __inputTheRoute(self,column):
        msg = "Ingrese"
        array = help.convertArray(column)
        lista = []        
        for i in range(0, len(array)):             
            if i == 0:
                cod = help.codigoShipper()               
                print(array[i] +" : ", cod)
                lista.append(cod)
            elif i <= 2:
                var = Console.inputNumber(msg + ' ' + array[i] + " : ")
                lista.append(var)            
            elif i == 3 :
                option = help.selection()
                lista.append(option)            
            else:
                lista.append(self.__subConditionInputRoute(array, i))
        return lista    
                
    def __subConditionInputRoute(self, column, i):                     
        if i<=5:
            Time = help.currentdate()
            print(column[i] + " : " + Time)
            return Time
        if i == 6 :      
            var = Console.inputString("ingrese " +column[6] + " : ")
            return var             
        else:
            city  = Console.inputString("ingrese " +column[7] + " : ")            
            return help.inputCity(city)  
        
    def __inputUpdateTheRoute(self, column,id):
        Conn =  Database.conexion()
        update = tuple()
        consulta = Conn.cursor()   
        sql = query_extend.extendRouteUpdate()+ " where " + "cedula_camionero" + " = " + "'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchone()        
        if data:
            update = self.__upgradeOptions(column, data, id)
        else:
            print("No se encuentra")
        return update
            
    def __upgradeOptions(self, columns, data, id):
        update = tuple()
        print("\n")
        for i in range(0, len(columns)):                               
            print(i, " columna :" ,columns[i], " = ", data[i])
            print("\n")
        option = Console.inputNumber("selecione la columna : ")           
        update = self.__changeDataRoute(columns, option, id)           
        return update
    
    def __changeDataRoute(self,columns, option, id):
        update = tuple()
        msg = "Ingrese"
        idcolumns= "cedula_camionero"
        if option == 0 or option == 1:
            position = columns[option]
            edit = Console.inputNumber(msg +" "+ columns[option] + " : ")
            update = (self.__table, position, edit, idcolumns, id)            
        elif option == 2:
            edit = help.selection()
            position = columns[option]
            update = (self.__table, position, edit,idcolumns , id)
        elif option == 3:
            position = columns[option] 
            edit = Console.inputString(msg +" "+ columns[option] + " : ")             
            if help.v(edit) == True:
                print("No esta el municipio")                
            else:
                cod = help.v(edit)
                update = (self.__table, position, cod, idcolumns, id)                        
        return update
       
            

        
        
        
        
        
        
        
            
            
            
            
        
        
                
                
                
                
                
                
    
    
    
                
                
            
            
            
            
        

          
