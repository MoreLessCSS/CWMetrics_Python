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
InstanceMetaData=client._get_instance_metadata()

dimensions = {'InstanceId': InstanceMetaData[0],
           'InstanceType': InstanceMetaData[1],
           'InstanceHostname': InstanceMetaData[2]}

for metric in config['metrics']:
    for moduleConfig in metric:
        moduleName = metric[moduleConfig]['module']
        mod = __import__(moduleName, fromlist=['my_class'])
        module = getattr(mod, 'my_class')
        print (module)
        var= module()
        print (var)
        var = module.PortMonitor(metric[moduleConfig], moduleName)

        metricValue = var.getMetric()
        units = var.getUnit()
        #print ("\n")
        #pprint (config['metrics'])

        client = CWMetricWriter(config['region'])
        value = client.send_metrics('varNamespace', 'instanceId', 'instanceType', moduleConfig, metricValue, units, dimensions)




        #metric[moduleConfig]['namespace'], MetricData