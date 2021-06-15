from sys import path
from jinja2 import Environment, FileSystemLoader
import pdfkit

class CreatePdf:
    def excutePdf(elements):
        try:
            env = Environment(loader=FileSystemLoader("templates"))
            template = env.get_template("index.html")            
            html = template.render(dict_item = elements)
            #f = open('nuevo.html', 'w')
            #f.write(html)
            #f.close()
            #config = pdfkit.configuration(wkhtmltopdf='/opt/bin/wkhtmltopdf')
            exe = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
            config = pdfkit.configuration(wkhtmltopdf=exe)
            salida = "D:/base de datos/Framework/Controller/PDF/nuevo.pdf"
            pdfkit.from_string(html, salida, configuration=config)
            print("generado")
            return True
        except Exception:
            print("Error para crear pdf")
            return False