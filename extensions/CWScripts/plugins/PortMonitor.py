import socket
from contextlib import closing
from inspect import getmembers
from pprint import pprint

class PortMonitor (MetricSignature)

    domain=None
    port=None

    def __INIT__(self, config, name):
        self->config = config
        self->name = name
        self->domain = self->config->domain
        self->port = self->config->port

    def getMetric():

        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(2)
            if sock.connect_ex((self->domain, self->port)) == 0:
                print "Port is open"
                return 0
            else:
                print "Port is not open"
                return 1

    def getUnit():
       return None

    def getAlarms():

        result array([
                      array("ComparisonOperator" => "LessThanThreshold",
                            "Threshold" => 1,
                            "Name" => self->name)
                    ])

        pprint(getmembers(result))
        return result