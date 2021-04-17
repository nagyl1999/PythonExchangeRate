''' globális importok '''
import sys
import requests

class Exchange:
    ''' Átváltás lekérdező '''
    BASE_URL = 'https://api.coingecko.com/api/v3'

    def __init__(self, config):
        ''' Konstruktor '''
        self.config = config

    def get(self, url):
        ''' Lekérdezés '''
        return requests.get(url).json()

    def get_url(self, url, param):
        ''' URL konstruktor '''
        return '{}/{}/{}'.format(Exchange.BASE_URL, url, param)

    def get_coin(self, name):
        ''' Coin átváltás, keresett pénznemmel visszatérés '''
        return self.get(self.get_url('coins', name))['market_data']['current_price'][self.config.get('coins').get('base_fiat').lower()]