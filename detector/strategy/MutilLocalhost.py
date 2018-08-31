from detector.strategy.IStrategy import IStrategy

class MutilLocalhost(IStrategy):
    def __init__(self):
        self.hit = 0
        self.localCount = 0
        self.MAX_LOCAL = 2
    
    def notify(self, host):
        if host.getIP() == "127.0.0.1" or host.getIP() == "localhost":
            self.localCount += 1
        if self.localCount > self.MAX_LOCAL:
            self.hit = 1

    def isHit(self):
        return self.hit

    def print(self):
        print('    是否存在多个127.0.0.1: ' + str(self.hit))