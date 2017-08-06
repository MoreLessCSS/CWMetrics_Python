from datetime import *
import loadConfig
import time
import CWMetricWriter
from inspect import getmembers
from pprint import pprint
from boto.ec2 import cloudwatch
from boto.utils import get_instance_metadata

config = loadConfig.getConfigFile()
client = CWMetricWriter(config['region'])
InstanceMetaData=client._get_instance_metadata()

dimensions = {'InstanceId': InstanceMetaData[0],
           'InstanceType': InstanceMetaData[1]}

for metric in config['metrics']:
    print (metric)
    for moduleConfig in metric:

        moduleName = metric[moduleConfig]['module']
        module = __import__(moduleName)
        var = module.PortMonitor(metric[moduleConfig], moduleName)
        metricValue = var.getMetric()
        units = var.getUnit()
        #print ("\n")
        #pprint (config['metrics'])


        value = client.send_metrics('varNamespace', 'instanceId', 'instanceType', moduleConfig, metricValue, units, dimensions)




        #metric[moduleConfig]['namespace'], MetricData