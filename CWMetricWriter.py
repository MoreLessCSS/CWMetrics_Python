from boto.ec2 import cloudwatch
from boto.utils import get_instance_metadata
from datetime import *
import pprint


class CWMetricWriter(object):
    CW_NAMESPACE='test'

    def __init__(self, region):
        self.connection = cloudwatch.connect_to_region(
            'eu-central-1',
            aws_access_key_id='AKIAICPDUK5NKKB3XLIQ',
            aws_secret_access_key='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'
            )


    def send_metrics(self, varNamespace, instanceId, instanceType, varMetric, varValue, unit, dimensions):
        self.connection.put_metric_data(varNamespace, varMetric,
                                    varValue, unit=unit,
                                    dimensions=dimensions)


    def _get_instance_metadata(self):
        metadata = get_instance_metadata()
        return metadata['instance-id'], metadata['instance-type', metadata['instance-name']

