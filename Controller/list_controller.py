import os, sys
from Model.connection import Database
from Model.Query import Sql
from terminaltables import AsciiTable
from Controller import help
graph = Sql('transporte')
class Tables:     
    @staticmethod
    def design_table(table,Query):
        os.system("cls")    
        col = graph.columns(table)
        fil = Sql.lits_Select_Table_Extend(Query)
        #Convierte la tupla mal formateada en un array
        head = []
        for item in col:
            head.extend(item)
                
        table_data = [ head, ]
        
        #Convierte la tupla mal formateada en un array por iteracion
        for item in fil:
            row = []
            row.extend(item)
            table_data.append(row)
        
        #Imprime la tabla en pantalla
        table = AsciiTable(table_data)
        print (table.table)
        
    @staticmethod
    def design_table_columns(Query, columns):
        os.system("cls")        
        fil = Sql.lits_Select_Table_Extend(Query)
              
        head = []
        for item in columns:
            head.extend(item)          
       
        table_data = [ columns, ]
        
        for item in fil:
            row = []
            row.extend(item)
            table_data.append(row)           
                   
        table = AsciiTable(table_data)
        print (table.table)      
        
        
    @staticmethod
    def table_vertical(name,data,COLUMNS):
        os.system("cls")        
        print("--------------"+ name +" --------------------")
        for x in range(0, len(COLUMNS)):
            print(str(COLUMNS[x]).replace("'", "").replace(",","").strip("('").strip("',)") + " : " , data[x] )            
        print("-------------------------------------------")     
        
               
            
       
        
        
            
            
          
        
            