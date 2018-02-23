import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
##start = dt.datetime(2000,1,1)
##end = dt.datetime(2018,1,27)
##
##df = web.get_data_yahoo('TSLA', start, end)
##df.to_csv('tsla.csv')
##df[['Adj Close', "Close", "High", "Open"]].plot()
##plt.show()
##print(df[["Adj Close", "Close", "Open", "High", "Low"]])

style.use('ggplot')

df = pd.read_csv('BTC_USD.csv', parse_dates = True, index_col = 0)
#df["100ma"] = df["Adj Close"].rolling(window = 100, min_periods = 0).mean()

df_ohlc = df['close'].resample("10D").ohlc()
df_volume = df["volume"].resample("10D").sum()

df_ohlc.reset_index(inplace=True)

df_ohlc["date"] = df_ohlc["date"].map(mdates.date2num)

#print(df_ohlc.head())



ax1 = plt.subplot2grid((6, 1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6, 1), (5,0), rowspan = 1, colspan = 1, sharex = ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width = 2, colorup = "g")
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()


