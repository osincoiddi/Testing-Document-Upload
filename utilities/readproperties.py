import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getapplicationurl():
        url=config.get('CommonInfo','url')
        return url

    @staticmethod
    def getfile():
        file=config.get('CommonInfo', 'file')
        return file
