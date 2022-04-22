import pandas as pd 
import numpy as np
import yfinance as fy
import datetime as dt
from pandas_datareader import data as pdr
### using yahoo finance to get the data for the stocks
fy.pdr_override()
### The user chooses a stock
stock=input("Enter the ticker of the company you would like to screen:")

### selected start date of analysis 
startyear=2021
startmonth=1
startday=1

### established time date object
start=dt.datetime(startyear,startmonth,startday)

now=dt.datetime.now()

df=pdr.get_data_yahoo(stock,start,now)
print(df)

### taking a moving average 
ma=30
### leaving the string open if i deside to change how long the average is 
smaString="Sma_"+str(ma)

df[smaString]=df.iloc[:,4].rolling(window=ma).mean()
print(df)
