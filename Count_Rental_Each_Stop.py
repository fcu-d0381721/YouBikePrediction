"""
    將每月份youbike租借量按照月日時區分計算
    建立class去做讀取檔案、新增欄位、計算兩日之間所有日期
    裡面的四個def:
    1.init 宣告一些初始值.
    2.readCSV 讀取檔案並把裡面為NULL值去除
    3.addColumn 把原始時間切割小時出來存成新的欄位
    4.getTwoday 呼叫class時已把開始跟結束時間assign好了，在這邊會直接輸出值
    5.count 計算每一個資料在各個時間點共有多少租借量
    55~58行為new class的動作
"""
import pandas as pd
from datetime import datetime, date, timedelta


class MergeData():
    def __init__(self, data, sdate, edate):
        self.sdate = sdate
        self.edate = edate
        self.data = data
        self.df = []
        self.day = []
        self.readCSV()

    def readCSV(self):
        self.df = pd.read_csv('YB/' + str(self.data) + '.csv', encoding='utf-8')
        self.df = self.df.dropna().reset_index(drop=True)

    def addColumn(self, column):
        self.df[column] = pd.to_datetime(self.df[column])
        self.df["date"] = [datetime.strftime(d, '%Y/%m/%d')for d in self.df[column]]
        self.df["hour"] = self.df[column].dt.hour
        self.df["date"] = pd.to_datetime(self.df["date"])

    def getTwoday(self):
        delta = self.edate - self.sdate  # as timedelta
        for i in range(delta.days + 1):
            self.day.append(self.sdate + timedelta(days=i))

    def count(self):
        site = pd.read_csv('dataset/site.csv', encoding='utf-8')
        stop = site['借車場站'].tolist()
        output = []
        for day in self.day:
            tempforday = self.df[self.df["date"] == day].reset_index(drop=True)
            for hour in range(0, 24):
                tempforhour = tempforday[tempforday["hour"] == hour].reset_index(drop=True)
                for eachstop in stop:
                    tempforstop = tempforhour[tempforhour["借車場站"] == eachstop].reset_index(drop=True)
                    output.append([eachstop, day, hour, len(tempforstop)])
        return output


year = ["10701", "10702", "10703", "10704", "10705", "10706"]
m = [1, 2, 3, 4, 5, 6]
d = [31, 28, 31, 30, 31, 30]
for i in range(0, 6):
    month = MergeData(year[i], date(2018, m[i], 1), date(2018, m[i], d[i]))
    month.addColumn("還車時間")
    month.getTwoday()
    output = month.count()

    t = pd.DataFrame(output, columns=['還車場站', '日期', '小時', '借車次數'])
    t.to_csv('./cleanupYBdata_2018/return' + str(m[i]) + '月借量.csv')