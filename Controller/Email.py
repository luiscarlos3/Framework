import os.path
import smtplib
from email.message import Message
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

class SendEmail:
    @staticmethod
    def executeEmail(receiver, id ):           
        try :            
            body = '''
            Ahora si funciona correctamente
            el envio de adjuntos
            pendiente que cuando usas smtp debes
            reencodear los stream de datos en Base64
            para que quede como texto plano
            '''
            sender = 'lszondas@gmail.com'
            password = 'xxxxxxxxxxxxxxxxxx'
            #receiver = 'Stefany1995.duque22@gmail.com'

            #Se compone el correo
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = receiver
            message['Subject'] = 'Se adjunta un archivo PDF'
            pdfname = id+".pdf"                  
            ruta = 'd:/base de datos/Framework/Controller/PDF/'+pdfname     
                   
            
            message.attach(MIMEText(body, 'plain'))           
            binary_pdf = open(ruta,'rb')

            payload = MIMEBase('application', 'octate-stream', Name=pdfname)
            # payload = MIMEBase('application', 'pdf', Name=pdfname)
            payload.set_payload((binary_pdf).read())

            #Obligatorio reencodear el stream de datos para poder enviarlo como plaintext
            encoders.encode_base64(payload)

            # Se agrega el header con le nombre del pdf
            payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
            message.attach(payload)

            #usa el puerto smtp de gmail
            session = smtplib.SMTP('smtp.gmail.com', 587)

            #habilita la seguridad
            session.starttls()

            #ingresa con usuario y pass
            session.login(sender, password)

            text = message.as_string()
            session.sendmail(sender, receiver, text)
            session.quit()            
            return True
        except ValueError:            
            print("Error envar el correo ")
            return False        
#SendEmail.executeEmail()

        
