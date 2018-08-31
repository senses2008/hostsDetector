from detector.strategy.IStrategy import IStrategy

class MutilIP(IStrategy):
    def __init__(self):
        self.hit = 0
        self.ipCount = {}
        self.IP_COUNT_LIMIT = 2
        
    def notify(self, host):
        if host.getIP() == "":
            return
        if host.getIP() in self.ipCount:
            self.ipCount[host.getIP()] += 1
        else:
            self.ipCount[host.getIP()] = 1
        if self.ipCount[host.getIP()] > self.IP_COUNT_LIMIT:
            self.hit = 1

    def isHit(self):
        return self.hit

    def print(self):
        print('    是否1个IP对应多个URL: ' + str(self.hit))