import loadConfig
from CWMetricWriter import *

config = loadConfig.getConfigFile()
client = CWMetricWriter(config['region'])
InstanceMetaData=client._get_instance_metadata()

dimensions = {'InstanceId': InstanceMetaData[0],
           'InstanceType': InstanceMetaData[1],
           'InstanceHostname': InstanceMetaData[2]}

for metric in config['metrics']:
    for moduleConfig in metric:
        moduleName = metric[moduleConfig]['module']
        mod = __import__(moduleName, fromlist=[moduleName])
        module = getattr(mod, moduleName)
        var = module(metric[moduleConfig], moduleName)
        metricValue = var.getMetric()
        units = var.getUnit()
        client = CWMetricWriter(config['region'])
        value = client.send_metrics('varNamespace', 'instanceId', 'instanceType', moduleConfig, metricValue, units, dimensions)

        #metric[moduleConfig]['namespace'], MetricData
