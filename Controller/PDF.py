from jinja2 import Environment, FileSystemLoader
import datetime
import pdfkit

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
        exe = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=exe)
        salida = "D:/base de datos/Framework/Controller/PDF"+elements[column]+".pdf"       
        pdfkit.from_string(html, salida, configuration=config)
        print("generado")
        
    def excutePdfReport(document,elements, title):
        date = datetime.date.today()               
        env = Environment(loader=FileSystemLoader("Controller/templates"))
        template = env.get_template(document)           
        html = template.render(lista = dict(elements), Title=title)
        #print(html)      
        f = open('nuevo.html', 'w')
        f.write(html)
        f.close()
        #config = pdfkit.configuration(wkhtmltopdf='/opt/bin/wkhtmltopdf')
        #exe = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        #config = pdfkit.configuration(wkhtmltopdf=exe)
        #salida = "D:/base de datos/Framework/Controller/PDF/reportes/vehiculos"+ str(date) +".pdf"       
        #pdfkit.from_string(html, salida, configuration=config)
        #print("generado")



        