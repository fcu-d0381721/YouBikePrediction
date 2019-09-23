import pandas as pd
import plotly.graph_objects as go

site = pd.read_csv('./dataset/行政區各年齡層人口數.csv', encoding='utf-8')
# print(site)
y = site[site['性別 ']=='計'].reset_index(drop=True)
# print(y)
# print(y.columns)
matching = [s for s in y.columns if "合計_" in s]
# print(matching)
# print(y[matching])
age = ['0~9歲', '10~19歲', '20~29歲', '30~39歲', '40~49歲', '50~59歲', '60~69歲', '70~79歲', '80~89歲', '90~99歲']
count = 0
for i in range(0, len(matching), 2):
    y[age[count]] = y[matching[i]] + y[matching[i+1]]
    count += 1
# print(y)
col = ['區 域 別', '0~9歲', '10~19歲', '20~29歲', '30~39歲', '40~49歲', '50~59歲', '60~69歲', '70~79歲', '80~89歲', '90~99歲']
print(y[col])
for j in range(0, 12):
    u = y[col].iloc[j, :].tolist()
    t = u[0]
    del u[0]
    print(u)
    fig = go.Figure(
        data=[go.Bar(x=age, y=u, text=u, textposition='outside', marker_color='lightsalmon')],
        layout_title_text= t + "各年齡層人口總數"
    )
    fig.show()
# county = site['行政區'].unique()
# for i in county:
#     tt = site[site['行政區'] == i].reset_index(drop=True)
#     fig = go.Figure(
#         data=[go.Bar(x=tt['站牌名稱'], y=tt['總數'], text=tt['總數'], textposition='outside',
#                      marker_color='lightsalmon')],
#         layout_title_text= i + '各站點車位總數'
#     )
#     fig.show()

# print(site)
# temp = site.groupby('sarea')['snc'].count()
# n = pd.DataFrame(dict(features=temp.index, count=temp.values))
# print(n)

# fig = go.Figure()
# fig.add_trace(go.Bar(
#     x=site['行政區'],
#     y=site['收入'],
#     name='收入',
#     marker_color='indianred',
#     text=site['收入'],
#     textposition='outside'
# ))
# fig.add_trace(go.Bar(
#     x=site['行政區'],
#     y=site['家庭戶數'],
#     name='家庭戶數',
#     marker_color='lightsalmon',
#     text=site['家庭戶數'],
#     textposition='outside'
# ))
# fig.add_trace(go.Bar(
#     x=site['學校校名'],
#     y=site['女生數'],
#     name='女生數',
#     marker_color='lightsalmon'
# ))
# Here we modify the tickangle of the xaxis, resulting in rotated labels.
# fig.update_layout(title="台北市各行政區收入", barmode='group', xaxis_tickangle=-45)
# fig.show()

#
# fig = go.Figure(
#     data=[go.Bar(x=age, y=u, text=u, textposition='outside', marker_color='lightsalmon')],
#     layout_title_text="松山區各年齡層人口總數"
# )
# fig.show()