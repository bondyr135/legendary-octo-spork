
import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json


def send_mail(message):
    with open('vars.json') as f:
        keys = json.load(f)

        server = smtplib.SMTP_SSL(keys['SMTPSERVER'], keys['SMTPPORT'])
        server.login(keys['YAHOO'], keys['YAHOOPSWD'])

        msg = MIMEMultipart()
        msg['Subject'] = 'Update from iHerb'
        msg['from'] = formataddr(('Ravid Bondy scraper', keys['YAHOO']))
        msg['To'] = keys['GMAIL']

        msg.attach(MIMEText(message, 'plain'))

        server.send_message(msg)
        server.quit()
