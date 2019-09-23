import pandas as pd
from datetime import datetime, date, timedelta

df = pd.read_csv('./Rain/信義/2017-06-30.csv', encoding='utf-8')
del df['Unnamed: 0']
print(df['日期'])
df['日期'] = '2017-' + df['日期']
print(df)