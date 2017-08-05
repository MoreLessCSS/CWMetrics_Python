from abc import ABCMeta, abstractmethod

class MetricSignature(object):

    __metaclass__ = ABCMeta

    def __init__(self, config):
        self.config = config


    @abstractmethod
    def getMetric(self):

        pass

    @abstractmethod
    def getUnit(self):

        pass

    @abstractmethod
    def getAlarms(self):

        pass

    getMetricName(self):
      return self.name