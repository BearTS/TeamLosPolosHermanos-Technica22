import yfinance as yf
from datetime import date

today=date.today()
d1 = today.strftime("%Y-%m-%d")
d2 = 
d=str(d1)

df = yf.download('BTC-USD',start=, end = d)