from sys import path
from jinja2 import Environment, FileSystemLoader
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
        
        