import os, sys
from Model.connection import Database
from Model.Query import Sql
from terminaltables import AsciiTable
from Controller import help
graph = Sql()

class Tables: 
        
    @staticmethod
    def design_table_columns(rows, columns):
        os.system("cls")        
        fil = rows
                      
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
        
               
            
       
        
        
            
            
          
        
            