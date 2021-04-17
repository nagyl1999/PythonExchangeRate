''' globális importok '''
import sys
import configparser

class Datas(list):
    ''' Adattárolók tárolása '''
    def get(self, name):
        ''' Adattároló név szerinti keresése '''
        for data in self:
            if data.name.lower() == name.lower():
                return data
        return None

class Data(dict):
    ''' Beállítások tárolására szolgáló osztály '''
    def __init__(self, name):
        ''' Típus beállítása '''
        self.name = name

    def add(self, key, value):
        ''' Kulcs - érték hozzáadása, típusválogatás '''
        if ',' in value:
            self[key] = [elem.strip() for elem in value.split(',')]
        elif value.isdigit():
            self[key] = float(value) if round(float(value)) - float(value) != 0 else int(value)
        else:
            self[key] = value

def classify(datas, config):
    ''' Adatszerkezetbe rendezés '''
    for key in config.sections():
        data = Data(key)
        for k in config[key]:
            data.add(k, config[key].get(k))
        datas.append(data)

def readConfig(filename):
    ''' Beállítások beolvasása, adatszerkezetbe rendezése '''
    config = configparser.ConfigParser()
    config.read(filename)
    datas = Datas()
    classify(datas, config)
    return datas