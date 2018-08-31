from detector.strategy.IStrategy import IStrategy

class MutilReturn(IStrategy):
    def __init__(self):
        self.hit = 0
        self.returnTimes = 0
        self.MAX_RETURNS = 2

    def notify(self, host):
        if host.getLine() == "":
            self.returnTimes += 1
        else:
            self.returnTimes = 0
        if self.returnTimes > self.MAX_RETURNS:
            self.hit = 1
        
    def isHit(self):
        return self.hit

    def print(self):
        print('    是否存在连续回车:' + str(self.hit))