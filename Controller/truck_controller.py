import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.validation import  Validar
from Controller import help

from Controller.write import Console
from Controller.PDF import CreatePdf

obj = Query.Sql()
class ControllerTruck:
    
    def __init__(self, table, idcolumns):        
        self.__table = table
        self.__idcolumns = idcolumns
        
    def truckInsert(self,id):
        status = False
        column = obj.columns(self.__table)
        tupl = tuple(self.__truckInput(id,column))
        if not tupl:
            status = False
        else:
            if obj.insert(self.__table, tupl) == True:
                status = True
            else:
                status = False
        return status 

    def truckDelete(self,id):        
        return Sql.delete(self.__table, self.__idcolumns, id) 
    
    def truckUpdate(self, id):
        status = False
        herdears = obj.columns(self.__table)
        columns = help.convertArray(herdears)
        tupl = self.__truckInputUpdate(columns, id)
        if not tupl:
            status = False
        else:
            if Sql.update(tupl) == True:
                status = True
            else:
                status = False
        return status 
    
    def truckSearch(self,id):         
        conn = Database().conexion()
        consulta = conn.cursor()        
        sql = query_extend.extendTruckSearch() + " where " + self.__idcolumns +" = '" + id + "'"     
        consulta.execute(sql)       
        data = consulta.fetchone()    
        if data:
            return data, help.getTitles(consulta.description)                       
        else:
            print("no se encontro el camion")
       
            
    def optionPDF(self):
        print("¿ Desea generar reporte general de vehiculos ?")
        print("Si >> y")
        print("No >> n")
        op = Console.inputString("selecione una opcion ")
        if op == "y":
            self.__generaPdfTruck()
        return " "
    
    def __testResultList(self,valor, titulos):        
        if not valor:
           print("Error al cargar los datos")
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
            
    def __generaPdfTruck(self):                   
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extendTruckSearch()       
        consulta.execute(sql)
        data = consulta.fetchall()                    
        if data:
            data = self.__testResultList(data, help.getTitles(consulta.description) )
            CreatePdf.excutePdfReport("Reportes.html",data,"vehiculos")
        return" "        
        
    def truckList(self):
        conn = Database().conexion()
        consulta = conn.cursor()        
        sql =  query_extend.extend_truck()
        consulta.execute(sql)
        rows = consulta.fetchall()
        return rows, help.getTitles(consulta.description)
        
    def __driverValidation(self, id):       
        return Validar.validation_truck_driver("camionero",id, "documento") == True
    
    #----------------------------------------------------------------------*
    # help methods avoid overload
    #----------------------------------------------------------------------*       
         
    def __truckInput(self,id,column):
        msg = "Ingrese"        
        array = help.convertArray(column)
        lista = []       
        if self.__driverValidation(id):
             lista = self.__ConditionInput(array,lista, id)# toco pasar mas 3 argumentos               
        else:
            print("No se encuentra registrado")
        return lista
    
    def __truckInputUpdate(self,column, id):         
        Conn =  Database.conexion()
        update = tuple()
        consulta = Conn.cursor()
        sql = query_extend.extend_truck() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchone()
        if data:
            update = self.__conditionOne(column, data, id)
        else:
            print("No se encuentra el vehiculo ")           
        return update  
    
    def __ConditionInput(self,column,lista, id):
        lista = []
        msg = "ingrese"
        val = Validar(self.__table)                       
        register = input(msg +" "+column[0] + " : ")
        if val.Register_validation(register, self.__idcolumns) == True:                    
            print("Ya se encuentra registrado")                    
        else:
            lista.append(register)
            modelo = Console.inputNumber(msg +" "+column[1]+ " : ")
            lista.append(modelo)
            value = Console.inputString(msg +" " +column[2] + " : ")
            lista.append(value)
            potencia = Console.inputNumber(msg +" "+column[3]+ " : ")
            lista.append(potencia)
            lista.append(id)
            city = Console.inputString(msg +" "+column[5] + " : ")                   
            lista.append(help.inputCity(city))         
        return lista
    
    def __conditionOne(self, columns, data, id):
        msg = "ingrese"
        update = tuple()
        print("\n")        
        for i in range(0, len(columns)):                    
            print(i, " columna :" ,columns[i], " = ", data[i])
            print("\n")
        option = Console.inputNumber("selecione la columna : ")                   
        if option == 0:
            position = columns[0]
            edit = input(msg +" "+columns[0] + " : ")
            update = (self.__table, position, edit,self.__idcolumns, id)
                           
        elif option == 1:
            position = columns[1]
            edit = Console.inputNumber(msg +' '+ columns[1] + " : ")
            update = (self.__table, position, edit, self.__idcolumns, id)
                
        elif option == 2:
            position = columns[2]
            edit = Console.inputNumber(msg+ ' ' + columns[2] + " : ")
            update = (self.__table, position, edit, self.__idcolumns, id)
        else:
            update = self.__conditionTwoo(option, columns, id)             
        return update
    
    def __conditionTwoo(self,option, columns, id):
        msg = "ingrese"
        update = tuple()           
        if option == 3:
            position = columns[option]
            edit = Console.inputNumber(msg + " " +columns[3] + " : ")
            update = (self.__table, position, edit, self.__idcolumns, id)            
        elif option == 4:
            position = columns[option]
            edit = Console.inputNumber(msg + " " +columns[4] + " : ")
            update = (self.__table, position, edit, self.__idcolumns, id)
        elif option == 5:
            position = columns[option]
            edit = Console.inputString(msg + " "+columns[5] + " : ")           
            if help.v(edit) == True:
                print("No esta el municipio")
            else:
                edit = help.v(edit)
                update = (self.__table, position, edit, self.__idcolumns, id)
        else:
            print(" Opcion invalida ")   
        return update
    
        
        
        
    
              
        
    
        
        
        
    
   