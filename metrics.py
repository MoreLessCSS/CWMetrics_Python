from datetime import *
import loadConfig
import time
from CWMetricWriter import *
from inspect import getmembers
from pprint import pprint
from boto.ec2 import cloudwatch
from boto.utils import get_instance_metadata

config = loadConfig.getConfigFile()
client = CWMetricWriter(config['region'])

for metric in config['metrics']:
    print (metric)
    for moduleConfig in metric:
        print (moduleConfig)
        moduleName = metric[moduleConfig]['module']
        module = __import__(moduleName)
        var = module.PortMonitor(metric[moduleConfig], moduleName)
        metricValue = var.getMetric()
        units = var.getUnit()
        #print ("\n")
        #pprint (config['metrics'])
        dimensions = {'Name': 'InstanceId',
                   'Name1': 'InstanceType'}

        print (metric[moduleConfig]['module'])

       # value = client.send_metrics('varNamespace', 'instanceId', 'instanceType', metric[moduleConfig], metricValue, units, dimensions)




        #metric[moduleConfig]['namespace'], MetricData