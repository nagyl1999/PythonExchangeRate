''' globális importok '''
import sys
import smtplib

class Email:
    ''' Üzenetet reprezentáló osztály '''
    def __init__(self, config):
        ''' Konstruktor '''
        self.config = config
        self.length = 0
        self.message = []

    def add(self, coin, rate):
        ''' Coin hozzáfűzése '''
        self.message.append('{}: {}{}'.format(coin.capitalize(), rate, self.config.get('coins').get('base_fiat').upper()))

    def send(self):
        ''' Levél küldése '''
        pass