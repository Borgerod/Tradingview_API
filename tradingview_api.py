from tradingview_ta import TA_Handler, Interval, Exchange
from tradingview_ta import *
import time
i=0
while i<=10:
    df = TA_Handler(
        symbol="BTCUSDT",
        screener="crypto",
        exchange="BINANCE",
        interval=Interval.INTERVAL_15_MINUTES,
    )


    print(df.get_analysis().indicators["RSI"])
#________________________________________________________________________


# # Store the last order.
# last_order = "sell"

# handler=df

# # Repeat forever.
# while True:
#     # Retrieve recommendation.
#     rec = handler.get_analysis().indicators["RECOMMENDATION"]

#     # Create a buy order if the recommendation is "BUY" or "STRONG_BUY" and the last order is "sell".
#     # Create a sell order if the recommendation is "SELL" or "STRONG_SELL" and the last order is "buy".
#     if "BUY" in rec and last_order == "sell":
#         # REPLACE COMMENT: Create a buy order using your exchange's API.

#         last_order = "buy"
#     elif "SELL" in rec and last_order == "buy":
#         # REPLACE COMMENT: Create a sell order using your exchange's API.

#         last_order = "sell"

#     # Wait for x seconds before retrieving new analysis.
#     # The time should be the same as the interval.
#     time.sleep(x)



## https://steemit.com/python/@marketstack/how-to-download-historical-price-data-from-binance-with-python###

# import requests 
# import json 
# import pandas as pd 
# import numpy as np  
# import datetime as dt  

# frequency = input("Please enter the frequency (1m/5m/30m/.../1h/6h/1d/ :  ")

# def get_bars(symbol, interval=frequency):
#     root_url = 'https://api.binance.com/api/v1/klines'
#     url = root_url + '?symbol=' + symbol + '&interval=' + interval
#     data = json.loads(requests.get(url).text)
#     df = pd.DataFrame(data)
#     df.columns = ['open_time',
#                   'o', 'h', 'l', 'c', 'v',
#                   'close_time', 'qav', 'num_trades',
#                   'taker_base_vol', 'taker_quote_vol', 'ignore']
#     df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
#     return df

# btcusdt = get_bars('BTCUSDT')
# ethusdt = get_bars('ETHUSDT')


# df0=pd.DataFrame(btcusdt)
# df0.to_csv('_btcusdt.csv')

# df1=pd.DataFrame(ethusdt)
# df1.to_csv('_ethusdt.csv')




# import os
# from binance.client import Client
# import pandas as pd
# import datetime, time

# def GetHistoricalData(self, howLong):
#     self.howLong = howLong
#     # Calculate the timestamps for the binance api function
#     self.untilThisDate = datetime.datetime.now()
#     self.sinceThisDate = self.untilThisDate - datetime.timedelta(days = self.howLong)
#     # Execute the query from binance - timestamps must be converted to strings !
#     self.candle = self.client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, str(self.sinceThisDate), str(self.untilThisDate))

#     # Create a dataframe to label all the columns returned by binance so we work with them later.
#     self.df = pd.DataFrame(self.candle, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
#     # as timestamp is returned in ms, let us convert this back to proper timestamps.
#     self.df.dateTime = pd.to_datetime(self.df.dateTime, unit='ms').dt.strftime(Constants.DateTimeFormat)
#     self.df.set_index('dateTime', inplace=True)

#     # Get rid of columns we do not need
#     self.df = self.df.drop(['closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol','takerBuyQuoteVol', 'ignore'], axis=1)

#     print(self.df)
# GetHistoricalData(self, howLong)




# https://steemit.com/python/@marketstack/how-to-download-historical-price-data-from-binance-with-python###




# import requests 
# import json 
# import pandas as pd 
# import numpy as np  
# import datetime as dt  

# # pd.set_option('display.max_colwidth', None)
# # pd.set_option('display.max_columns', None)
# # pd.set_option('display.width', None)


# frequency = "15m"

# def get_bars(symbol, interval=frequency):
#     root_url = 'https://api.binance.com/api/v1/klines'
#     url = root_url + '?symbol=' + symbol + '&interval=' + interval
#     data = json.loads(requests.get(url).text)
#     df = pd.DataFrame(data)
#     df.columns = ['open_time',
#                   'Open', 'High', 'Low', 'Close', 'Volume',
#                   'close_time', 'qav', 'num_trades',
#                   'taker_base_vol', 'taker_quote_vol', 'ignore']
#     df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
#     return df

# btcusdt = get_bars('BTCUSDT')
# ethusdt = get_bars('ETHUSDT')

# def rma(x, n, y0):
# 	a = (n-1) / n
# 	ak = a**np.arange(len(x)-1, -1, -1)
# 	return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1)]

# df=pd.DataFrame(btcusdt)
# df = df.iloc[:, 1:6]
# df.index.name='Datetime'
# df=df.reset_index()
# df['Datetime']=df['Datetime'].dt.strftime('%Y-%m-%d %H:%M')
# df['Close'] = df['Close'].astype(float)


# n = 14
# df['change'] = df['Close'].diff()
# df['gain'] = df.change.mask(df.change < 0, 0.0)
# df['loss'] = -df.change.mask(df.change > 0, -0.0)
# df['avg_gain'] = rma(df.gain[n+1:].to_numpy(), n, np.nansum(df.gain.to_numpy()[:n+1])/n)
# df['avg_loss'] = rma(df.loss[n+1:].to_numpy(), n, np.nansum(df.loss.to_numpy()[:n+1])/n)
# df['rs'] = df.avg_gain / df.avg_loss
# df['rsi_14'] = 100 - (100 / (1 + df.rs))
# print(df)
