"""
    取得youbike官網的每站點車位數
    利用selenium套件爬蟲，再利用BeautifulSoup解析
    10~12行為參數宣告，分別為計算每一個row長度的count_for_row、存放全部的站點資訊list、暫時存放各站點的list
    15~17行為爬蟲抓取
    20行為透過網頁html tag 取得需要抓的網頁位置
    25行 資料格式每4比一組
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

count_for_row = 0
all_Stop_sign = []
temp_Stop_sign = []

driver = webdriver.Chrome()
driver.get("http://wa.taipei.youbike.com.tw/station")
soup = BeautifulSoup(driver.page_source)

for ele in soup.select('#sationList_container #myTable #setarealist tr td'):
    temp_Stop_sign.append(ele.text.split()[0])
    count_for_row += 1

    if count_for_row == 4:
        all_Stop_sign.append(temp_Stop_sign)
        count_for_row = 0
        temp_Stop_sign = []
output = pd.DataFrame(all_Stop_sign, columns=['行政區', '站牌名稱', '可借車輛', '可停空位'])
output.to_csv("各站點車位數.csv")