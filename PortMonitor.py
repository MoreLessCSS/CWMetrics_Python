import socket
from MetricSignature import *
from contextlib import closing
from inspect import getmembers
from pprint import pprint

class PortMonitor (MetricSignature):

    def __init__(self, config, name):
        self.config = config
        self.name = name
        self.domain = config['domain']
        self.port = config['port']
        print ("\n")
        print (self.domain + ":" + self.port)

    def getMetric(self):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(2)
            if sock.connect_ex((self.domain, int(self.port))) == 0:
                print ("Port is open")
                return 0
            else:
                print ("Port is not open")
                return 1

    def getUnit(self):
       return None

    def getAlarms(self):
        result =[
                      [{"ComparisonOperator" : "LessThanThreshold",
                            "Threshold" : 1,
                            "Name" : self.name}]
                    ]

        pprint(getmembers(result))
        return result