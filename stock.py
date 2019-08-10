import tushare as ts
import json
import matplotlib.pyplot as plt

df = ts.get_hist_data('000002')
df.to_json('股票数据.json',orient='records')

filename = '股票数据.json'
with open(filename) as f:
    btc_data = json.load(f)  # 1

openprice = []
months = []
weeks = []
weekdays = []
close = []

# 打印每一天的信息
for btc_dict in btc_data:

    open = float(btc_dict['open'])
    high = float(btc_dict['high'])
    close = float(btc_dict['close'])
    low = float(btc_dict['low'])
    openprice.append(open)

    print("开盘价{}，收盘价{}，最高价{}, 最低价{}".format(
        open, close, high, low))
plt.plot(openprice)  # ①
plt.show()
print('HI')
version 4.1
