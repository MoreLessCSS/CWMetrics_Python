import loadConfig
from CWMetricWriter import CWMetricWriter
import sys

try:
    config = loadConfig.getConfigFile()
    client = CWMetricWriter(config['region'])
    InstanceMetaData=client._get_instance_metadata()
    dimensions = {'Instance_Id': InstanceMetaData[0],
                  'Instance_Type': InstanceMetaData[1],
                  'Hostname': InstanceMetaData[2]}

    for metric in config['metrics']:
        for moduleConfig in metric:
            moduleName = metric[moduleConfig]['module']
            mod = __import__(moduleName, fromlist=[moduleName])
            module = getattr(mod, moduleName)
            var = module(metric[moduleConfig], moduleName)
            metricValue = var.getMetric()
            units = var.getUnit()
            client = CWMetricWriter(config['region'])
            value = client.send_metrics(metric[moduleConfig]['namespace'],
                                       'instanceId',
                                       'instanceType',
                                       moduleConfig,
                                       metricValue,
                                       units,
                                       dimensions)
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
