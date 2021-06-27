from Model.connection import Database
from Model import Query, query_extend
from Model.Query import Sql
from Controller.write import Console
from Controller import help
from Controller.PDF import CreatePdf

#The class is called where the connection to the database
# and the different methods to perform the
# CRUD operations are Query.Sql()

obj = Query.Sql()

# the route configuration class controls the crud and
# queries fetched from the database 
# and organize the information

class RouteSetting:
    def __init__(self, table, idcolumns):        
        self.__table = table
        self.__idcolumns = idcolumns

    def routeInsert(self):
        status = False        
        column = obj.columns(self.__table)  
        tupl = tuple(self.__inputTheRoute(column))      
        if not tupl:
            status = False      
        else:
            if Sql.insert(self.__table, tupl) == True:
                status = True       
            else:
                status = False    
        return status
    # methods controller of delet
    def routeDelete(self,id):            
        return Sql.delete(self.__table, self.__idcolumns, id) 
                   
    # methods controller of search 
    def routeSearch(self,id):
        status = False
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.queryRouteSearch() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)    
        data = consulta.fetchone()                     
        if data:
            conn.close()
            status = True             
            return status, data, help.getTitles(consulta.description)      
        else:
            status = False
            return status, None, None,
                    
        
    # method controller update     
    def routeUpdate(self, id):
        status = False        
        tupl = tuple(self.__inputUpdateTheRoute(id))  # method handles updating threads in an organized way returns a tuple
        if not tupl:
            status = False
        else:
            if Sql.update(tupl) == True:
                status = True
            else:
                status = False              
        return status
    
    def optionPDF(self, id):
        print("¿ Desea generar reporte general de rutas ?")
        print("Si >> y")
        print("No >> n")
        op = Console.inputString("selecione una opcion ")
        if op == "y":
            self.__generaPdfRoute(id)
        return " "
    
    def __generaPdfRoute(self, id):                   
        conn = Database().conexion()
        consulta = conn.cursor()
        sql = query_extend.queryRouteSearch() + " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchall()
        titulos = help.getTitles(consulta.description)             
        if data:
            data = help.testResultList(data, titulos)
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
        msg = "Ingrese "
        array = help.convertArray(column)
        lista = []        
        for i in range(0, len(array)):             
            if i == 0:
                cod = help.codigoShipper()               
                print(array[i] +" : ", cod)
                lista.append(cod)
            elif i <= 2:
                var = Console.inputNumber(msg + array[i] + " : ")
                lista.append(var)            
            elif i == 3 :
                option = help.selection()
                lista.append(option)            
            else:
                lista.append(self.__subConditionInputRoute(array, i))
        lista = help.checkElements(lista)
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
        
    def __inputUpdateTheRoute(self,id):
        lista = []
        Conn =  Database.conexion()        
        consulta = Conn.cursor()   
        sql = query_extend.extendRouteUpdate()+ " where " + self.__idcolumns + " = " + "'" + id + "'"
        consulta.execute(sql)
        data = consulta.fetchone()        
        if data:
            lista = self.__upgradeOptions(help.getTitles(consulta.description), data, id)
        else:
            print("No se encuentra")
        return lista
            
    def __upgradeOptions(self, columns, data, id):
        lista = []
        print("\n")
        for i in range(0, len(columns)):                               
            print(i, " columna :" ,columns[i], " = ", data[i])
            print("\n")
        option = Console.inputNumber("selecione la columna : ")           
        lista = self.__changeDataRoute(columns, option, id)           
        return lista
    
    def __changeDataRoute(self,columns, option, id):
        lista = []
        msg = "Ingrese "        
        if option == 0 or option == 1:
            position = columns[option]
            edit = Console.inputNumber(msg + columns[option] + " : ")                      
        elif option == 2:
            edit = help.selection()
            position = columns[option]            
        elif option == 3:
            position = columns[option] 
            var = Console.inputString(msg + columns[option] + " : ")             
            if help.v(var) == True:
                print("No esta el municipio")                
            else:
                edit = help.v(var)
        elif option > len(columns):
            return None     
        lista = help.checkElements([self.__table, position, edit, self.__idcolumns, id])                       
        return lista
       
            

        
        
        
        
        
        
        
            
            
            
            
        
        
                
                
                
                
                
                
    
    
    
                
                
            
            
            
            
        

          
