import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_from, send_to, subject, text):

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    server = smtplib.SMTP('smtp.yandex.ru')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(send_from, '')
    # new_text = msg.as_string()
    server.sendmail(send_from, send_to, str(msg))
    server.quit()
