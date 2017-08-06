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
        metrics = var.getMetric()
        units = var.getUnit()
        print ("\n")

                           'Unit' : var.getUnit(),
                           'MetricName' : var.name,
                           'Value'      : metrics,
                           'Timestamp'  : datetime.now(),
                           'Dimensions' : [{'Name' : 'InstanceId', 'Value' : "instanceId",
                                            'Name' : 'Instance Name', 'Value' : "instanceName"}]


        dimensions = {'Name': 'InstanceId',
                   'Name1': 'InstanceType'}
        value = client.send_metrics('varNamespace', 'instanceId', 'instanceType', metrics, units, dimensions)


        #metric[moduleConfig]['namespace'], MetricData