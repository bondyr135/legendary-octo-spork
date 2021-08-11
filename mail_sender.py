
import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json


def send_mail(message):

    with open('vars.json') as f:
        vars = json.loads(f.read())

        server = smtplib.SMTP_SSL(vars['SMTPSERVER'], vars['SMTPPORT'])
        server.login(vars['YAHOO'], vars['YAHOOPSWD'])

        msg = MIMEMultipart()
        msg['Subject'] = 'Update from iHerb'
        msg['from'] = formataddr(('Ravid Bondy scraper', vars['YAHOO']))
        msg['To'] = vars['GMAIL']

        msg.attach(MIMEText(message, 'plain'))

        server.send_message(msg)
        server.quit()
