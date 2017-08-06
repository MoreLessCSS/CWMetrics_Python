from datetime import *
import loadConfig
import time
from inspect import getmembers
from pprint import pprint
from boto.ec2 import cloudwatch
from boto.utils import get_instance_metadata

config = loadConfig.getConfigFile()

def connect(region):
    connection = cloudwatch.connect_to_region(
        'eu-central-1',
        aws_access_key_id='AKIAICPDUK5NKKB3XLIQ',
        aws_secret_access_key='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'
        )



def send_metrics(varNamespace, instanceId, instanceType, varMetric, varValue, unit, dimensions):
       client = connect('eu-central-1')
       client.put_metric_data(varNamespace, varMetric, varValue, unit=unit, dimensions=dimensions)

for metric in config['metrics']:
    # print ("METRIC:\n" + config['metrics'] + "\n")
    for moduleConfig in metric:
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

        value = send_metrics('varNamespace', 'instanceId', 'instanceType', metric[moduleConfig]['module'], metricValue, units, dimensions)




        #metric[moduleConfig]['namespace'], MetricData