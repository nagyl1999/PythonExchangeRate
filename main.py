''' globális importok '''
import sys
import configparser

''' lokális importok '''
import modulok.mail as mail
import modulok.rate as rate
import modulok.config as config

''' statikus adatok '''
config_filename = 'config.conf'

def getPrice(conf, exchange, message):
    ''' Árfolyam lekérése és összehasonlítás '''
    coins = conf.get('coins').get('coins')
    for coin in coins:
        rate = exchange.get_coin(coin)
        if rate >= coins[coin]:
            message.add(coin, rate)

def main():
    ''' Főprogramrész '''
    conf = config.readConfig(config_filename)
    message = mail.Email(conf)
    exchange = rate.Exchange(conf)
    getPrice(conf, exchange, message)
    if message.length > 0: message.send()

main()
