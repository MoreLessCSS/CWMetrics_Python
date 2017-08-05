from boto.ec2 import cloudwatch
from boto.utils import get_instance_metadata
from datetime import *


class CWMetricWriter(object):
    CW_NAMESPACE='test'
    def __init__(self, region):
        self.connection = cloudwatch.connect_to_region(
            'eu-central-1',
            aws_access_key_id='AKIAICPDUK5NKKB3XLIQ',
            aws_secret_access_key='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'
            )

    def _get_instance_metadata(self):
            metadata = get_instance_metadata()
            return metadata['instance-id'], metadata['instance-type']

    def send_metrics_old(self):
            MetricData=[
                        {
                            'MetricName': 'Metrik',
                            'Dimensions': [
                                {
                                    'Name': 'string1',
                                    'Value': 'what ever'
                                },
                            ],
                            'Value': '1',
                            'Statistics': 'Average',
                            'Unit': 'None'
                        },
                    ]
            metrics = {'AverageGetRequestDuration': 1.2,
                        'AveragePostRequestDuration': 2.2}

            print(metrics.keys())
            metadata = get_instance_metadata()
            response = self.connection.put_metric_data(self.CW_NAMESPACE, metrics.keys(),
                           metrics.values(),
                           unit="Milliseconds",
                           dimensions={"InstanceType": "instance_type", "InstanceId": "instance_id"})
            print(response)
            pprint(response)

    #             resp=self.connection.put_metric_data('MyName', 'MyData', metrics, "Milliseconds")


    def send_metrics(self, instance_id, instance_type, metrics, unit):
        self.connection.put_metric_data(self.CW_NAMESPACE, metrics.keys(),
                            metrics.values(), unit=unit,
                            dimensions={"InstanceType": instance_type, "InstanceId": instance_id})

    def example_send_metric(self):
        metadata = self._get_instance_metadata()
        metrics = {'AverageGetRequestDuration': 1.2,
                   'AveragePostRequestDuration': 2.2}
        self.send_metrics(metadata[0], metadata[1], metrics, "Milliseconds")
