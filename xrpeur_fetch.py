# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:35:49 2018

@author: Andrea Luca Lampart
"""

import datetime
import requests as rq
import matplotlib.pyplot as plt
import pandas_datareader as dr
from matplotlib import style

#style.use('fivethirtyeight')
#test
# Request HTTP API data from Bitstamp (Max. allowed Rate before IP gets blocked is 1 request/sec)
def fetchData():
    response = rq.get('https://www.bitstamp.net/api/v2/ticker/xrpeur/')
    
    # Create JSON
    data = response.json()    
   
    # Return data
    return {'price' : float(data['last']), 'time' : datetime.datetime.fromtimestamp(int(data['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')}

# Create dynamic arrays
fig = plt.figure()

ax1 = fig.add_subplot(1,1,1)

plt.ion()
plt.suptitle('XRP EUR [10 sec chart]')

i = 0
x = []
y = []

# Ping the HTTP server of bitstamp all second and update the plot
while True:
    try:
        fetched = fetchData()
        
        print(fetched)
        x.append(i)#fetched['time'])
        y.append(fetched['price'])
        
        # Clear the old frame
        ax1.clear()
        ax1.plot(x, y)
        plt.axis([min(x), max(x), min(y), max(y)])
        plt.xlabel('Date')
        plt.ylabel('Price (XRPEUR)')
        i+=1
        plt.pause(10.0)            
                      
    except KeyboardInterrupt:
        break
