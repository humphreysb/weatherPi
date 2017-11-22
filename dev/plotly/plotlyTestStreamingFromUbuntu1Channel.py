# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 04:09:04 2017

@author: humphreysb
"""


# From: https://plot.ly/python/streaming-tutorial/
# Single plot, streamed from Ubuntu



#Check which version is installed on your machine and please upgrade if needed.

import plotly
plotly.__version__



import numpy as np
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go


# stream ids
#stream_ids = tls.get_credentials_file()['stream_ids']
stream_ids = ["ms3k61zd5j"]


print stream_ids


# Get stream id from stream id list 
stream_id = stream_ids[0]


stream_1 = dict(token=stream_id, maxpoints=60)


# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1         # (!) embed stream id, 1 per trace
)

data = go.Data([trace1])



# Add title to layout object
layout = go.Layout(title='Time Series')

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# Send fig to Plotly, initialize streaming plot, open new tab
py.iplot(fig, filename='python-streaming')



# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s = py.Stream(stream_id)

# We then open a connection
s.open()


# (*) Import module keep track and format current time
import datetime
import time

i = 0    # a counter
k = 5    # some shape parameter

# Delay start of stream by 5 sec (time to switch tabs)
#time.sleep(5)

while True:

    # Current time on x-axis, random numbers on y-axis
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    y = (np.cos(k*i/50.)*np.cos(i/50.)+np.random.randn(1))[0]

    # Send data to your plot
    stat = s.write(dict(x=x, y=y))

    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot

    time.sleep(1)  # plot a point every second    
# Close the stream when done plotting
s.close()