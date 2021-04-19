# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 21:38:37 2021

@author: vaidik
"""

#ENVIRONMENT NAME: sentimental_analysis

import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns
import datetime as dt

currency = "CAD"
metric = "Close"

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

#crypto = ['BTC', 'ETH', 'LTC', 'XRP', 'DASH', 'SC', 'DOGE', 'BCH', 'NEO', 'MIOTA']
crypto = []
crypto1 = input("Enter the ticker of crypto 1: ")
crypto2 = input("Enter the ticker of crypto 2: ")
crypto.append(crypto1)
crypto.append(crypto2)
columns = []

first = True

for ticker in crypto:
    data = web.DataReader(f"{ticker}-{currency}", 'yahoo', start, end)
#    print(data.head(5))
    if first:
        combined = data[[metric]].copy()
        columns.append(ticker)
        combined.columns =  columns
        print(combined.head(5))
        first=False
        
    else:
        combined = combined.join(data[metric])
        columns.append(ticker)
        print(combined.head(5))
        combined.columns = columns
        
for ticker in crypto:
    plt.plot(combined[ticker], label=ticker)
    
combined = combined.pct_change().corr(method='pearson')

print(combined)
#sns.heatmap(combined, annot=True, cmap="coolwarm")
plt.legend(loc="upper right")
plt.show()
