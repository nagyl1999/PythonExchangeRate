''' globális importok '''
import sys
import configparser

''' lokális importok '''
import modulok.config as config

''' statikus adatok '''
config_filename = 'config.conf'

def main():
    ''' Főprogramrész '''
    conf = config.readConfig(config_filename)

main()
