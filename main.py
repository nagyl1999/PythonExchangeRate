''' globális importok '''
import sys
import configparser

''' lokális importok '''
import modulok.mail as mail
import modulok.rate as rate
import modulok.config as config

''' statikus adatok '''
config_filename = 'config.conf'

def getPrice(conf, message):
    ''' Árfolyam lekérése és összehasonlítás '''
    x = rate.Exchange(conf)
    coins = conf.get('coins').get('coins')
    for coin in coins:
        rate = x.get_coin(coin)
        if rate >= coins[coin]:
            message.add(coin, rate)

def main():
    ''' Főprogramrész '''
    conf = config.readConfig(config_filename)
    message = mail.Email(conf)
    getPrice(conf, message)
    if message.length > 0: message.send()

main()
