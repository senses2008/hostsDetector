class Host:
    def __init__(self, line):
        line = line.strip()
        self.line = line
        self.URL = ""
        self.IP = ""
        if not line.startswith('#'):
            temp = line.split()
            if len(temp) == 2:
                self.URL = temp[1]
                self.IP = temp[0]

    def getLine(self):
        return self.line

    def getURL(self):
        return self.URL

    def getIP(self):
        return self.IP