''' globális importok '''
import sys
import smtplib
import email.utils

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email(MIMEMultipart):
    ''' Üzenetet reprezentáló osztály '''
    def __init__(self, config):
        ''' Konstruktor '''
        super().__init__('alternative')
        self.config = config
        self.length = 0
        self.message = []

    def construct(self):
        ''' Levél beállítása '''
        self["From"] = self.config.get('user').get('username')
        self["To"] = self.config.get('user').get('email')
        self["Subject"] = self.config.get('smtp').get('subject')
        self["Date"] = email.utils.formatdate()
        self.attach(MIMEText('\n'.join(self.message), "plain"))

    def add(self, coin, rate):
        ''' Coin hozzáfűzése '''
        self.message.append('{}: {}{}'.format(coin.capitalize(), rate, self.config.get('coins').get('base_fiat').upper()))
        self.length += 1

    def send(self):
        ''' Levél küldése '''
        try:
            self.construct()
            self.server = smtplib.SMTP_SSL(self.config.get('smtp').get('smtp_host'), self.config.get('smtp').get('smtp_port'))
            self.server.login(self.config.get('user').get('username'), self.config.get('user').get('password'))
            self.server.sendmail(self["From"], self["To"], self.as_string())
            self.server.quit()
        except Exception as e:
            pass