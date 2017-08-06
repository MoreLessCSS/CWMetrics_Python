from boto.ec2 import cloudwatch
from boto.utils import get_instance_metadata
from datetime import *
import pprint


class CWMetricWriter(object):
    CW_NAMESPACE='test'

    def __init__(self, region):
        self.connection = cloudwatch.connect_to_region(
            'eu-central-1',
            aws_access_key_id='1AKIAICPDUK5NKKB3XLIQ',
            aws_secret_access_key='UZduH/vO4YgmcUHuYWps3m2D8eSBSyriq0meFdg5'
            )


    def example_send_metric(self):
        metrics = {'AverageGetRequestDuration': 1.2,
                   'AveragePostRequestDuration': 2.2}
        self.send_metrics('string1', 'metadata', metrics, "Milliseconds")

    def send_metrics(self, instance_id, instance_type, metrics, unit):
        self.connection.put_metric_data(self.CW_NAMESPACE, metrics.keys(), metrics.values(), unit=unit, dimensions={"InstanceType": instance_type, "InstanceId": instance_id})


