import pandas as pd
from datetime import datetime, date, timedelta
import time


def getTwoday(sdate, edate):
    day = []
    delta = edate - sdate  # as timedelta
    for i in range(delta.days + 1):
        day.append(sdate + timedelta(days=i))
    return day


# month = [6, 7, 8, 9, 10, 11, 12]
# day = [30, 31, 31, 30, 31, 30, 31]
month = [1, 2, 3, 4, 5, 6]
day = [31, 28, 31, 30, 31, 30]
air_station_name = ['信義', '內湖', '南港', '台北', '士林', '大直', '天母',  '文山',
                    '松山', '永和', '石牌', '社子',  '竹子湖', '關渡', '鞍部']
for stop in air_station_name:
    for m in range(len(month)):
        output = []
        rent_stop = pd.read_csv('./cleanupYBdata_2018/' + str(month[m]) + '月借量.csv', encoding='utf-8')
        return_stop = pd.read_csv('./cleanupYBdata_2018/return' + str(month[m]) + '月借量.csv', encoding='utf-8')
        del rent_stop['Unnamed: 0']
        del return_stop['Unnamed: 0']
        rent_return_combined = pd.merge(rent_stop, return_stop, left_on=['借車場站', '日期', '小時'], right_on=['還車場站', '日期', '小時'])
        rent_return_combined = rent_return_combined[['借車場站', '日期', '小時', '借車次數', '還車次數']]
        # print(rent_return_combined)

        airbox = pd.read_csv('輸出.csv', encoding='utf-8')
        airbox_combined = pd.merge(rent_return_combined, airbox, on=['借車場站', '借車場站'])
        airbox_combined = airbox_combined[['借車場站', '日期', '小時', '借車次數', '還車次數', '測站']]
        airbox_combined["日期"] = pd.to_datetime(airbox_combined["日期"])
        airbox_combined["date"] = [datetime.strftime(d, '%Y/%m/%d')for d in airbox_combined["日期"]]
        airbox_combined["date"] = pd.to_datetime(airbox_combined["date"])
        selected_bike_stop = airbox_combined[airbox_combined['測站'] == stop].reset_index(drop=True)

        air_station = pd.read_csv('./Rain/' + stop + '/2018-0' + str(month[m]) + '-' + str(day[m]) + '.csv', encoding='utf-8')
        air_station['日期'] = '2018-' + air_station['日期']
        air_station["日期"] = pd.to_datetime(air_station["日期"])

        twoday = getTwoday(pd.Timestamp(2018, month[m], 1), pd.Timestamp(2018, month[m], day[m]))
        for i in twoday:
            selected_air_station_temp = air_station[air_station['日期'] == i].reset_index(drop=True)  # 空品
            del selected_air_station_temp['Unnamed: 0']
            print(selected_air_station_temp)
            time.sleep(5)
            selected_bike_stop_temp = selected_bike_stop[selected_bike_stop['date'] == i].reset_index(drop=True)
            for h in range(0, 24):
                # if h < 10:
                #     h = '0' + str(h)
                #     print(h)
                temp = selected_air_station_temp[selected_air_station_temp['觀測時間'] == h+1].reset_index(drop=True)
                temp['測站'] = stop
                temp2 = selected_bike_stop_temp[selected_bike_stop_temp['小時'] == h].reset_index(drop=True)
                result = pd.merge(temp2, temp, on='測站')
                print(result)
                if len(output) == 0:
                    output = result
                else:
                    output = output.append(result).reset_index(drop=True)
        print(output)
        output.to_csv(stop + '站' + str(month[m]) + '月.csv')