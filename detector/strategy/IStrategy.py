from abc import ABCMeta, abstractmethod

class IStrategy(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def notify(self, host):
        pass

    @abstractmethod
    def isHit(self):
        pass

    @abstractmethod
    def print(self):
        pass