from jinja2 import Environment, FileSystemLoader
import datetime
import pdfkit
from Controller import help

class CreatePdf:
    
    @staticmethod
    def excutePdf(document,elements, column):                 
        env = Environment(loader=FileSystemLoader("Controller/templates"))
        template = env.get_template(document)           
        html = template.render(dict_item = elements)
            #f = open('nuevo.html', 'w')
            #f.write(html)
            #f.close()
            #config = pdfkit.configuration(wkhtmltopdf='/opt/bin/wkhtmltopdf')
        exe = "C:\\Program Files\wkhtmltopdf\\binwkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=exe)
        salida = "D:/base de datos/Framework/Controller/PDF/vehiculos/"+elements[column]+".pdf"       
        pdfkit.from_string(html, salida, configuration=config)
        print("generado")
        
    @staticmethod    
    def excutePdfReport(document,elements,title):
        date = datetime.date.today()               
        env = Environment(loader=FileSystemLoader("Controller/templates"))
        template = env.get_template(document)           
        html = template.render(lista = dict(elements), Title=title)
        #print(html)      
        #f = open('nuevo.html', 'w')
        #f.write(html)
        #f.close()       
        exe = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=exe)
        salida = "D:/base de datos/Framework/Controller/PDF/vehiculos/"+ str(date) +".pdf"       
        pdfkit.from_string(html, salida, configuration=config)
        print("generado")
        
    @staticmethod    
    def excutePdfshipping(document,elements,title):
        num = help.getID(elements,1,5)                                      
        env = Environment(loader=FileSystemLoader("Controller/templates"))
        template = env.get_template(document)           
        html = template.render(lista = dict(elements), Title=title)
        #print(html)      
        #f = open('nuevo.html', 'w')
        #f.write(html)
        #f.close()                 
        exe = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=exe)
        salida = "D:/base de datos\Framework\Controller\PDF/reportesEnvios/envios"+ str(num) +".pdf"       
        pdfkit.from_string(html, salida, configuration=config)
        print("generado")
        
    def excutePdfInvoice(document,elements, column):                
        env = Environment(loader=FileSystemLoader("Controller/templates"))
        template = env.get_template(document)           
        html = template.render(dict_item = elements)
            #f = open('nuevo.html', 'w')
            #f.write(html)
            #f.close()
            #config = pdfkit.configuration(wkhtmltopdf='/opt/bin/wkhtmltopdf')
        exe = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=exe)
        salida = "D:/base de datos/Framework/Controller/PDF/recibos/"+elements[column]+".pdf"       
        pdfkit.from_string(html, salida, configuration=config)
        print("generado")
    
    
    
        



        