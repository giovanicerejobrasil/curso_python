"""
Enviando E-mail SMTP com Python
"""
import os
import pathlib
import smtplib
from dotenv import load_dotenv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

# Caminho arquivo HTML
HTML_FILE_PATH = pathlib.Path(__file__).parent / 'aula_188.html'

# Dados do remetente e destinatário
sender = os.getenv('SMTP_EMAIL', '')
reciver = os.getenv('EMAIL_RECIVER_EXAMPLE', '')

# Configurações SMTP
smtp_server = os.getenv('SMTP_SERVER', '')
smtp_port = os.getenv('SMTP_PORT', '')
smtp_username = os.getenv('SMTP_EMAIL', '')
smtp_password = os.getenv('SMTP_PASSWORD', '')

# Mensagem de texto
with open(HTML_FILE_PATH, 'r') as file:
    file_text = file.read()
    template = Template(file_text)
    email_text = template.substitute(
        sender_="Giovani C. Brasil", reciver_="Giovani")

# Transformar mensagem em MIMEMultiPart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = sender
mime_multipart['to'] = reciver
mime_multipart['subject'] = 'Assunto do E-mail'

email_body = MIMEText(email_text, 'html', 'utf-8')
mime_multipart.attach(email_body)

# Abrir conexão
with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)

    print('E-mail enviado com sucesso!')
