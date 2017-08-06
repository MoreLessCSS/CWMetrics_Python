from boto.ec2 import cloudwatch
from boto.utils import get_instance_metadata

class CWMetricWriter(object):

    def __init__(self, region):
        self.connection = cloudwatch.connect_to_region(region))

    def _get_instance_metadata(self):
        metadata = get_instance_metadata()
        return metadata['instance-id'],
                        metadata['instance-type'],
                        metadata['hostname']

    def send_metrics(self, varNamespace, instanceId, instanceType, varMetric, varValue, unit, dimensions):
        self.connection.put_metric_data(varNamespace,
                                        varMetric,
                                        varValue,
                                        unit=unit,
                                        dimensions=dimensions)