from tradingview_ta import TA_Handler, Interval, Exchange
from tradingview_ta import *
import time
# i=0
# while i<=10:


def Get_RSI():
    return TA_Handler(
        symbol="BTCUSDT",
        screener="crypto",
        exchange="BINANCE",
        interval=Interval.INTERVAL_15_MINUTES)

def main():
    print(Get_RSI().get_analysis().indicators["RSI"])

if __name__ == '__main__':
    for _ in infinity():
        main()

