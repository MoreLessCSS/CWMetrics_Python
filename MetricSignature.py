from abc import ABCMeta, abstractmethod

class MetricSignature(object):

    __metaclass__ = ABCMeta

    def __init__(self, config, name):
        self.config = config
        self.name = name


    @abstractmethod
    def getMetric(self):

        pass

    @abstractmethod
    def getUnit(self):

        pass

    @abstractmethod
    def getAlarms(self):

        pass

    def getMetricName(self):
      return self.name