from datetime import *
import loadConfig
import time
from CWMetricWriter import  *
from inspect import getmembers
from pprint import pprint

config = loadConfig.getConfigFile()
client = CWMetricWriter(config['region'])

for metric in config['metrics']:
    for moduleConfig in metric:
        moduleName = metric[moduleConfig]['module']
        module = __import__(moduleName)
        var = module.PortMonitor(metric[moduleConfig], moduleName)
        metricValue = var.getMetric()
        units = var.getUnit()
        print ("\n")




        dimensions = {'Name': 'InstanceId',
                   'Name1': 'InstanceType'}
        value = client.send_metrics('varNamespace', 'instanceId', 'instanceType', metric, MetricValue, units, dimensions)


        #metric[moduleConfig]['namespace'], MetricData