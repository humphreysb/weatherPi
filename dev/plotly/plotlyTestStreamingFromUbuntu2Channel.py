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
from plotly import tools


# stream ids
#stream_ids = tls.get_credentials_file()['stream_ids']
stream_ids = ["ms3k61zd5j","4510lf88te"]


print stream_ids


# Get stream id from stream id list 
stream_id1 = stream_ids[0]
stream_id2 = stream_ids[1]


stream_1 = dict(token=stream_id1, maxpoints=60)
stream_2 = dict(token=stream_id2, maxpoints=60)


# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1         # (!) embed stream id, 1 per trace
)

trace2 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_2         # (!) embed stream id, 1 per trace
)

data = go.Data([trace1,trace2])




layout = go.Layout(
    title='Double Y Axis Example',
    yaxis=dict(
        title='yaxis title'
    ),
    yaxis2=dict(
        title='yaxis2 title',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)


"""
fig = tools.make_subplots(rows=1, cols=2)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
"""

# Add title to layout object
#layout = go.Layout(title='Time Series')


#fig['layout'].update(height=600, width=600, title='Multiple Subplots')
                                               

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# Send fig to Plotly, initialize streaming plot, open new tab
#py.iplot(fig, filename='python-streaming')

py.iplot(fig, filename='make-subplots-multiple-with-titles')

# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s1 = py.Stream(stream_id1)
s2 = py.Stream(stream_id2)

# We then open a connection
s1.open()
s2.open()

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
    s1.write(dict(x=x, y=y))
    s2.write(dict(x=x, y=1.0))

    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot

    time.sleep(1)  # plot a point every second    
# Close the stream when done plotting
s1.close()
s2.close()