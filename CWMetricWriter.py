from boto.ec2 import cloudwatch
from boto.utils import get_instance_metadata

class CWMetricWriter(object):

    def __init__(self, region):
        try:
            self.connection = cloudwatch.connect_to_region(region)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        return result

    def _get_instance_metadata(self):
        try:
            metadata = get_instance_metadata()
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        else:
            return metadata['instance-id'], metadata['instance-type'], metadata['hostname']

    def send_metrics(self, varNamespace, instanceId, instanceType, varMetric, varValue, unit, dimensions):
        try:
            self.connection.put_metric_data(varNamespace,
                                                    varMetric,
                                                    varValue,
                                                    unit=unit,
                                                    dimensions=dimensions)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        return result

