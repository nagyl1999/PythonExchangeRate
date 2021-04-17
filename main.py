''' globális importok '''
import os
import sys
import datetime
import configparser

''' lokális importok '''
import modulok.mail as mail
import modulok.rate as rate
import modulok.config as config

''' statikus adatok '''
path = os.path.abspath(os.path.dirname(__file__))
config_filename = path + '/config.conf'
lofile_filename = path + '/log.log'

def logMessage(lofile_filename, message):
    ''' Log mentése '''
    file = open(lofile_filename, 'a')
    file.write('{}: {}\n'.format(datetime.datetime.now(), message))
    file.close()

def alreadySent(lofile_filename):
    ''' Küldtünk-e már levelet, (terrible algo, might change later) '''
    file = open(lofile_filename, 'r')
    for row in file:
        row = ':'.join(row.strip().split(':')[:-1]).split('.')[0]
        date = datetime.datetime.strptime(row, '%Y-%m-%d %H:%M:%S')
        if abs((date - datetime.datetime.now()).total_seconds()) < 3600: sys.exit()
    file.close()
    return False

def getPrice(conf, exchange, message):
    ''' Árfolyam lekérése és összehasonlítás '''
    coins = conf.get('coins').get('coins')
    for coin in coins:
        rate = exchange.get_coin(coin)
        if rate >= coins[coin]:
            message.add(coin, rate)

def main():
    ''' Főprogramrész '''
    if alreadySent(lofile_filename): sys.exit()
    conf = config.readConfig(config_filename)
    message = mail.Email(conf)
    exchange = rate.Exchange(conf)
    getPrice(conf, exchange, message)
    if message.length > 0: message.send()
    logMessage(lofile_filename, 'sent')

main()
