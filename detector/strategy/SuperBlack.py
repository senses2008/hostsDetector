import mysql.connector
from detector.strategy.IStrategy import IStrategy

class SuperBlack(IStrategy):
    def __init__(self):
        self.hit = False
        self.IS_DETECT_URL = False
        self.connectDB()

    def connectDB(self):
        self.conn = None
        if self.IS_DETECT_URL:
            self.conn = mysql.connector.connect(user='test', password='123456', database='test')

    def notify(self, host):
        if host.getURL() and self.IS_DETECT_URL and self.conn:
            sql = "SELECT * FROM advanced_black_list WHERE url = '%s'" % (host.getURL())
            cursor = self.conn.cursor()
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                if len(results):
                    self.hit = True
            except:
                self.hit = False

    def isHit(self):
        return self.hit

    def print(self):
        print("    监测是否URL在高级白数据库里:" + str(self.hit))