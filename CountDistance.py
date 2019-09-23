import pandas as pd

df = pd.read_csv('輸出1.csv', encoding='big5')
# df1 = pd.read_csv('測站資訊.csv', encoding='big5')
print(df['測站'].unique())
# res = pd.merge(df, df1, on=['測站', '測站'])
# print(res['測站編號'].unique())