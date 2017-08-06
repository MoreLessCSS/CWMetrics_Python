import json
import sys

def getConfigFile():
    try:
        with open("config.json") as data_file:
                data = json.load(data_file)
    except IOError as (errno, strerror):
         print "I/O error({0}): {1}".format(errno, strerror)
     except:
         print "Unexpected error:", sys.exc_info()[0]
         raise
    else:
        return data