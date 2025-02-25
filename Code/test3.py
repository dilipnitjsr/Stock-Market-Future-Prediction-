from finta import TA
import pandas as pd
import numpy as np
np.random.seed(42)
date_range = pd.date_range(start='2025-01-01 9:15:00', periods=100, freq='H')
print(date_range)

initial_price = 100 
close_price = initial_price + np.cumsum( np.random.uniform(-2,2,size=100))

open_price = np.roll(close_price,1)
open_price[0]= initial_price
high_price = open_price+ np.random.uniform(0,10,size=100)

low_price = open_price- np.random.uniform(0,10,size=100)

#close_price =  np.random.uniform(low_price,high_price)
df = pd.DataFrame ({
'date' : date_range,
'open' : open_price,
'high' : high_price,
'low': low_price,
'close' : close_price,})
x={"close": [100, 102, 101, 103, 105],"open": [100, 102, 101, 103, 105],"high": [100, 102, 101, 103, 105],"low": [100, 102, 101, 103, 105]}

#df = pd.DataFrame(x)
df["RSI"] = TA.RSI(df)
print(df)
