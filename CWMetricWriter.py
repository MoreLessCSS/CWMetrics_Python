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
            aws_secret_access_key='UZduH/vO4YgmcUHuYWps3m2D8eSBSyriq0meFdg5'
            )


    def example_send_metric(self):
        metrics = {'AverageGetRequestDuration': '1.1',
                   'AveragePostRequestDuration': '1.2'}
        self.send_metrics('string1', 'metadata', metrics, "Milliseconds")

    def send_metrics(self, varNamespace, varMetrics):
        pprint (send_metrics.varMetrics)
        self.connection.put_metric_data(varNamespace, varMetrics)


