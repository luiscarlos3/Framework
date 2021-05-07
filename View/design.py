from Model import Query

obj = Query.Sql("transporte")

class Graphics:    
    
    def headerMenu(self):
        print('----------------------------------------------------------------')
        print('\t------Administración de transporte--------\t')
        print('----------------------------------------------------------------')
        print('\n')
        
        
    def Appearance(self):          
        options = obj.name_Table()
        for i in range(0, len(options)):
            j = i + 1
            print(j , "Consultar " + str(options[i]).strip("('").strip("',)"))
        
    def designToCrud(self,table):
        print('----------------------------------------------------------------')
        print('\t------ estamos en el menu ' + table + ' ---------\t')
        print('----------------------------------------------------------------')
        print('\n')
        options = ["Registrar", "Buscar", "Eliminar", "Actualizar", "Lista"]
        for i in range(0, len(options)):            
            j = i+1
            print(j,". " + options[i] + " " + table)
            
    @staticmethod
    def header(name, table):
        print("-------------------------------")
        print("-----"+str(name).capitalize()+" "+str(table).capitalize()+"----\n")
        print("-------------------------------")
        
    def default():
        return "option Invalid"
    
       
        
        
        
        
        

    
    
    
   
    
           

           
     
    