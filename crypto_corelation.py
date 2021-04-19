# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:50:30 2021

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

crypto = ['BTC', 'ETH', 'LTC', 'XRP', 'DASH', 'SC', 'DOGE', 'BCH', 'NEO', 'MIOTA']
columns = []

first = True

for ticker in crypto:
    data = web.DataReader(f"{ticker}-{currency}", 'yahoo', start, end)
    if first:
        combined = data[[metric]].copy()
        columns.append(ticker)
        combined.columns =  columns
        first=False
        
    else:
        combined = combined.join(data[metric])
        columns.append(ticker)
        combined.columns = columns
        
for ticker in crypto:
    plt.plot(combined[ticker], label=ticker)
    
combined = combined.pct_change().corr(method='pearson')

sns.heatmap(combined, annot=True, cmap="coolwarm")
plt.legend(loc="upper right")
plt.show()