import os, sys
from Controller.validation import Validar
from Controller import help
from Controller.write import Console
from Model import query_extend

class Decorador:
    def __init__(self, table, idcolumns):
        self.__tablename = table
        self.__columna = idcolumns    
        
    def recipientInput(self,column):
        msg = "Ingrese"
        val = Validar(self.__tablename)
        array = self.__convertArray(column)
        lista = []
        for i in range(0,len(array)):
            if i is 0:
                id = Console.inputNumber(msg +" "+array[0] + " : ")                
                if val.Register_validation(id, self.__columna) == True:
                    print("ya se encuentra registrado")
                    os.system("pause")
                    break
                else:
                    lista.append(id)                                       
            if i is 3:                        
                tel = Console.inputNumber(msg+" "+array[3]+ " : ")
                lista.append(tel)                
            elif i is 5:
                city = Console.inputString(msg+" "+array[5]+ " : ")
                lista.append(self.__inputCity(city))                              
            elif i >= 1:
                name = Console.inputString(msg +" " +array[i]+ " : ")
                lista.append(name)                
        return lista
    
    def recipientInputUpdate(self,colum,id): 
        msg = "Ingrese"       
        arary = self.__convertArray(colum)
        sql = query_extend.extend_addressee() + " where " + self.__columna + " = " + "'" + id + "'"
        crt = Validar(self.__tablename)      
        data = crt.searchData(self.__columna,sql)
        if data:                        
            for i in range(0, len(arary)):                
                print(i, ". "+ "Columna : " + str(arary[i])  + " = " + data[i])
                print("\n")
            option = Console.inputNumber("selecione la columna : ")
            for i in range(0, len(arary)):
                if option == 0:
                    position = arary[0]
                    edit = Console.inputNumber(msg +" "+arary[0]+ " : ")
                    update = (self.__tablename, position, edit, self.__columna, id )
                    break                            
                elif option == 3:
                    position = arary[3]
                    edit = Console.inputNumber(msg +" "+arary[3] + " : ")
                    update = (self.__tablename, position, edit, self.__columna, id )
                    break 
                elif option == 5:                    
                    position = arary[5]
                    edit = Console.inputString(msg +" "+arary[5]+ " : ")
                    edit = self.__inputCity(edit)                                  
                    update = (self.__tablename, position, edit, self.__columna, id)                                        
                    break                    
                elif option == i:
                    position = arary[option]
                    edit = Console.inputString(msg +" "+arary[option] + " : ")
                    update = (self.__tablename, position, edit, self.__columna, id)
                                        
        else:
            print("No se encuentra la informacion")            
            os.system("pause")
        return update    
                    
    def __convertArray(self,array):
        lista= []
        for i in range(len(array)):
            for j in range(len(array[i])):
                lista.append(array[i][j])
        return lista
    
    def __inputCity(self, name):
        village = 0       
        if Validar.controller_city(name) == False:                        
            print("este municipio no se encuentra")
            os.system("pause")
        else:
            village = help.convert_city(name)
        return village
            
    
        
                
                            
        
          
        
                       
              
                
            
                
            
            
        
        
                       
                
                    
                    
            
    
        
             