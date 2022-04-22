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