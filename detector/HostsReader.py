import platform

class HostsReader:
    def __init__(self):
        if self.isWindowsPlatform():
            self.fileName = 'C:\Windows\System32\drivers\etc\hosts'
        else:
            self.fileName = '/etc/hosts'
        self.fp = open(self.fileName, 'r')
        
    def isWindowsPlatform(self):
        isWindowsPlatform = False
        if platform.platform().lower().find("windows") != -1:
            isWindowsPlatform = True
        return isWindowsPlatform

    def ReadLines(self):
        return self.fp.readlines()