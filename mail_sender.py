
import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json


def send_mail(message):

    server = smtplib.SMTP_SSL(process.env.SMTPSERVER, process.env.SMTPPORT)
    server.login(process.env.YAHOO, process.env.YAHOOPSWD)

    msg = MIMEMultipart()
    msg['Subject'] = 'Update from iHerb'
    msg['from'] = formataddr(('Ravid Bondy scraper', process.env.YAHOO))
    msg['To'] = process.env.GMAIL

    msg.attach(MIMEText(message, 'plain'))

    server.send_message(msg)
    server.quit()
