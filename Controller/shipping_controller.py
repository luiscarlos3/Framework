import pymysql
from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller import help
from Controller.list_controller import Tables
from Controller.utilis import utilidades
from Controller.write import Console

obj = Query.Sql()

class controllerShipping():
    
    def __init__(self, table, idcolumns):        
        self.__table = table
        self.__idcolumns = idcolumns    

    def shippingInsert(self):
        status = False    
        column = obj.columns(self.__table)
        tupl = tuple(self.__shippingInput(column))
        if not tupl:
            status = False
        else:
            if Sql.insert(self.__table, tupl):
                status = True
            else: 
                status = False            
        return status

    def shippingDelete(self, id):        
        return Sql.delete(self.__table, self.__idcolumns, id)          

    def shippingSearch(self,id):
        conn = Database().conexion()
        consulta = conn.cursor()    
        sql =  query_extend.extend_shipping_search() + " where "+ self.__idcolumns+ " = "+"'" + id + "'"     
        consulta.execute(sql)    
        data = consulta.fetchone()
        if data:         
            Tables.table_vertical(self.__table, data, utilidades.columnsShippings())   
        else:
            print("no se encontro el envio ")    

    def shippingUpdate(self, id):
        status = False
        herdears = obj.columns(self.__table)
        column = help.convertArray(herdears)
        tupl = self.__inputUpdate(column, id)
        if not tupl:
            status = False
        else:
            if Sql.update(tupl) == True:
                status = True
            else:
                status = False
        return status

    def shippingList(self):
        cs = query_extend.extend_shipping()
        columns = ["codigo_envio", "estado", "direccion","cedula destinatario", "cedula remitente","codigo paquete"]
        Tables.design_table_columns(cs, columns)

#----------------------------------------------------------------------*
# help methods avoid overload
#----------------------------------------------------------------------*
    def __inputUpdate(self, column, id):
        status = False   
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        # arreglar esta consulta cuando regrese 
        sql = "select * from " + self.__table+ " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchone()
        if data:
            self.__inputCondition(column, data, id)
        else:
            print("No se encuentra")
              
    def __inputCondition(self, columns, data, id):
        update = tuple()
        print("\n")
        for i in range(0, len(columns)):                               
            print(i, " columna :" ,columns[i], " = ", data[i])
            print("\n")
        option = Console.inputNumber("selecione la columna : ")           
        update = self.__inputTwoo(columns, option, id)           
        return update
    
    def __inputTwoo(self, columns, option, id):
        update = tuple()
        msg = "Ingrese"
        if option >= 1 and option <= 4:
            position = columns[option]
            edit = Console.inputNumber(msg +" "+ columns[option] + " : ")
            update = (self.__table, position, edit, self.__idcolumns, id)
        elif option is 5:
            position = columns[option]
            edit = Console.inputString(msg +" "+ columns[option] + " : ")
            update = (self.__table, position, edit, self.__idcolumns, id)
        elif option is 6:
            position = columns[option]
            edit = self.__selection()
            update = (self.__table, position, edit, self.__idcolumns, id)
        else:
            print("Las fecha de envio y el codigo del envio no se puede cambiar")         
        return update    
        
    def __shippingInput(self, column):
        msg = "Ingrese"
        array = help.convertArray(column)
        lista = []
        for i in range(0, len(array)):
            if i is 0:
                cod = help.codigoShipper()               
                print(array[i] +" : ", cod)
                lista.append(cod)
            elif i>=1 and i<=4:
                var = Console.inputNumber(msg + ' ' + array[i] + " : ")
                lista.append(var)
            elif i is 5:
                string = Console.inputString(msg + ' ' + array[i] + " : ")
                lista.append(string)
            else:
                val = self.__condition(array, i)
                lista.append(val)                     
        return lista
    
    def __condition(self, array, i):
        if i is 6:                 
            var = self.__selection()
            return var                         
        elif i is 7:
            Time = help.currentdate()
            print(array[i] + " : " + Time)
            return Time                                 
        elif i is 8:                
            date = help.fecha()            
            print(array[i] + " " +date)
            return date
                   
    def __selection(self):      
        print("1 -- enviando")
        print("2 -- entregado")
        print("3 -- salida")
        print("\n")
        num =int(input("seleccione el estado ")) 
        if  num == 1 :
            return "Enviado"
        elif num == 2:
            return "Entregado"
        elif num == 3:
            return "Salida"
              
            
                
               
                
    
            
                 
                
                
        
        


