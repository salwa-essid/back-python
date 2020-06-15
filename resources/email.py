import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from flask_restful import Resource
class Email(Resource):
    def post(self):
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        username = 'barhoumirahma0@gmail.com'
        password = 'rahma@barhoumi'
        sender = 'barhoumirahma0@gmail.com'
        targets = ['salwa.essid@gmail.com','anis.hajlaoui.ensit@gmail.com']

        msg = MIMEText("bonjour,votre compte est valide")
        msg['Subject'] = 'unknown route'
        msg['From'] = sender
        msg['To'] = ', '.join(targets)

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(sender, targets, msg.as_string())
        server.quit()
        return {'id': "Enseignant"}, 200