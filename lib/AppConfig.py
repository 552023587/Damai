import configparser
import os 
from lib import Global

configPath = os.path.join(Global.APP_PATH, "config.ini")

def readConfig(inikey,inivaluse):
     config = configparser.ConfigParser()
     config.read(configPath)
     convaluse=config.get(inikey,inivaluse)
     return convaluse   