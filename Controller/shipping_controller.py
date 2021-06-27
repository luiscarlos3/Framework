from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller import help
from Controller.PDF import CreatePdf


from Controller.write import Console

obj = Query.Sql()

class controllerShipping(object):
    
    def __init__(self, table, idcolumns, columns):        
        self.__table = table
        self.__idcolumns = idcolumns
        self.__columns = columns  

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
        status = False
        conn = Database().conexion()
        consulta = conn.cursor()    
        sql =  query_extend.extend_shipping_search() + " where "+  self.__idcolumns +" = "+ "'" + id + "'"+" or " + self.__columns + " = " +"'" +id + "'"
        consulta.execute(sql)    
        data = consulta.fetchone()               
        if data:
            status = True                               
            return status, data, help.getTitles(consulta.description)            
        else:
            status = False
            return status, None, None
        
    def __generationPdf(self,Id):       
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.QueryShipments() + " where " + self.__idcolumns + " = "+ "'" +  Id + "'" +" or " + self.__columns + " = " +"'"+ Id + "'"
        consulta.execute(sql)
        data = consulta.fetchall()
        if data:                        
            info = help.testResultList(data, help.getTitles(consulta.description))            
            CreatePdf.excutePdfshipping("Reportes.html",info,"Envios realizados")
        return " "   
    
    def optionPDF(self,id):
        print("¿ Desea generar reporte general de los envios ?")
        print("Si >> y")
        print("No >> n")
        op = Console.inputString("selecione una opcion ")
        if op == "y":
           self.__generationPdf(id)                             
        return" "            

    def shippingUpdate(self, id):
        status = False        
        tupl = self.__inputUpdate(id)
        if not tupl:
            status = False
        else:
            if Sql.update(tupl) == True:
                status = True
            else:
                status = False
        return status

    def shippingList(self):
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.extend_shipping()  
        consulta.execute(sql)
        rows = consulta.fetchall()
        return rows, help.getTitles(consulta.description)
#----------------------------------------------------------------------*
# help methods avoid overload
#----------------------------------------------------------------------*
    def __inputUpdate(self,id):          
        Conn =  Database.conexion()
        consulta = Conn.cursor()
        lista = []     
        sql = "select estado, fecha_entrega from " + self.__table + " where " + self.__idcolumns+ " = "+ "'"+  id +"'" +" or " + self.__columns + " = "+"'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchone()
        if data:
           lista = self.__optionsUpdate(help.getTitles(consulta.description), data, id)
        else:
            print("No se encuentra")
        return lista
              
    def __optionsUpdate(self, columns, data, id):
        update = []
        print("\n")
        for i in range(0, len(columns)):                               
            print(i, " columna :" ,columns[i], " = ", data[i])
            print("\n")
        option = Console.inputNumber("selecione la columna : ")           
        update = self.__inputTwoo(columns, option, id)           
        return update
    
    def __inputTwoo(self, columns, option, id):       
        lista = []         
        if option == 0:
            position = columns[option]
            edit = help.selection()                     
        elif option == 1:
            position = columns[option]
            edit = help.currentdate()
            print(columns[option] + " : " + edit)                                                    
        elif option > len(columns):
            return None            
        lista = help.checkElements([self.__table, position, edit, self.__idcolumns, id])
        return lista    
        
    def __shippingInput(self, column):
        msg = "Ingrese"
        array = help.convertArray(column)
        lista = []
        for i in range(0, len(array)):
            if i == 0:
                cod = help.codigoShipper()               
                print(array[i] +" : ", cod)
                lista.append(cod)
            elif i>=1 and i<=3:
                var = Console.inputNumber(msg + ' ' + array[i] + " : ")
                lista.append(var)
            elif i == 4:
                var = help.selection()
                lista.append(var)               
            else:
                val = self.__condition(array, i)
                lista.append(val)                          
        return lista
    
    def __condition(self, array, i):                               
        if i == 5:
            Time = help.currentdate()
            print(array[i] + " : " + Time)
            return Time                                 
        elif i == 6:                
            date = help.fecha()            
            print(array[i] + " " +date)
            return date
    
    
                   
    
            
              
            
                
               
                
    
            
                 
                
                
        
        


