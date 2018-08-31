from detector.strategy.IStrategy import IStrategy
from detector.Host import Host

class StrategyList:
    def __init__(self):
        self.observers = []

    def regist(self, observer:IStrategy):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to sub : {}').format(observer)
    
    def unRegist(self, observer:IStrategy):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to unsub : {}').format(observer)
    
    def notify(self, host:Host):
        [o.notify(host) for o in self.observers]

    def result(self):
        ret = 0
        for o in self.observers:
            ret = ret | o.isHit()

        return ret

    def print(self):
        for o in self.observers:
            o.print()