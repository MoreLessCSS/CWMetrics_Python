from datetime import *
import loadConfig
import time
from CWMetricWriter import  *
from inspect import getmembers
from pprint import pprint

config = loadConfig.getConfigFile()


pushMetrics = []
for metric in config['metrics']:
    for moduleConfig in metric:
        moduleName = metric[moduleConfig]['module']
        module = __import__(moduleName)
        var = module.PortMonitor(metric[moduleConfig], moduleName)
        metrics = var.getMetric()
        units = var.getUnit()
        print ("\n")
        pushMetrics.append({
                           'Unit' : var.getUnit(),
                           'MetricName' : var.name,
                           'Value'      : metrics,
                           'Timestamp'  : datetime.now(),
                           'Dimensions' : [{'Name' : 'InstanceId', 'Value' : "instanceId",
                                            'Name' : 'Instance Name', 'Value' : "instanceName"}]

                          })
        MetricData=[
                {
                    'MetricName': 'Manual_Metric',
                    'Dimensions': [
                        {
                            'Name' : 'InstanceId', 'Value' : "instanceId",
                            'Name' : 'Instance Name', 'Value' : "instanceName"
                        },
                    ],
                    'Timestamp': datetime.now(),
                    'Value': 123.0,
                    'StatisticValues': {
                        'SampleCount': 123.0,
                        'Sum': 123.0,
                        'Minimum': 123.0,
                        'Maximum': 123.0
                    },
                    'Unit': var.getUnit(),
                    'StorageResolution': 123
                },
            ]
        pprint(pushMetrics)


        client = CWMetricWriter(config['region'])
        value = client.send_metrics(metric[moduleConfig]['namespace'], MetricData)

        #metric[moduleConfig]['namespace'], MetricData