# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 03:44:57 2017

@author: humphreysb
"""



import plotly
plotly.__version__


import plotly.plotly as py  
import plotly.tools as tls   
import plotly.graph_objs as go
import numpy as np  

# Let's get at least two streaming tokens for this task.

stream_tokens = tls.get_credentials_file()['stream_ids']
#token_1 = stream_tokens[-1]   # I'm getting my stream tokens from the end to ensure I'm not reusing tokens
#token_2 = stream_tokens[-2]   
token_1 = "ms3k61zd5j"
token_2 = "4510lf88te"

print token_1
print token_2

# Now let's create some stream id objects for each token.

stream_id1 = dict(token=token_1, maxpoints=60)
stream_id2 = dict(token=token_2, maxpoints=60)

"""
The set up of this plot will contain one pie chart on the left and a bar chart on the right that will display the same information. This is possible because they are both charts that display "counts" for categroical variables.
We will have three categories, which are brilliantly named 'one', 'two', and 'three'. Later we'll randomly generate count data and stream it to our plot.
"""

import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Bar(
    x=['one', 'two', 'three'],
    y=[4, 3, 2],
    xaxis='x2',
    yaxis='y2',
    marker=dict(color="maroon"),
    name='Random Numbers',
    stream=stream_id2,
    showlegend=False
)
trace2 = go.Pie(
    labels=['one','two','three'],
    values=[20,50,100],
    domain=dict(x=[0, 0.45]),
    text=['one', 'two', 'three'],
    stream=stream_id1,
    sort=False,

)
data = [trace1, trace2]
layout = go.Layout(
    xaxis2=dict(
        domain=[0.5, 0.95],
        anchor='y2'
    ),
    yaxis2=dict(
        domain=[0, 1],
        anchor='x2'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='simple-inset-stream')

#Now let's set up some stream link objects and start streaming some data to our plot

s_1 = py.Stream(stream_id=token_1)
s_2 = py.Stream(stream_id=token_2)

# Start Streaming

s_1.open()
s_2.open()

import time
import datetime
import numpy as np

while True:
    nums = np.random.random_integers(0,10, size=(3))
    s_1.write(dict(labels=['one', 'two', 'three'], values=nums, type='pie'))
    s_2.write(dict(x=['one', 'two', 'three'], y=nums, type='bar', marker=dict(color=["blue", "orange", "green"])))
    time.sleep(0.8)
s_1.close()
s_2.close()

# You can see this stream live below:
tls.embed('streaming-demos','122')