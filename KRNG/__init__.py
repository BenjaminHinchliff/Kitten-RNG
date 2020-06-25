import configparser
import importlib_resources as res

__version__ = '1.1.0'

cfg = configparser.ConfigParser()
with res.path('KRNG', 'config.cfg') as cfgFile:
    cfg.read(str(cfgFile))
URL = cfg['KRNG']['url']
