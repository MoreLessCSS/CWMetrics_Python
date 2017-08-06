import json
from sys import *
import os


def getConfigFile():
    try:
         appDir = os.path.dirname(os.path.abspath(__file__))
         filename = os.path.join(appDir, 'config/MasterNode/config.json')
         with open(filename) as data_file:
                data = json.load(data_file)
    except IOError as (errno, strerror):
         print "I/O error({0}): {1}".format(errno, strerror)
    except:
         print "Unexpected error:", sys.exc_info()[0]
         raise
    else:
         return data