import yfinance as yf
from datetime import date

today=date.today()
d1 = today.strftime("%m/%Y/%d")
print("d1 =", d1)

df = yf.download('BTC-USD',start='2018-01-01', end = '2020-04-29')