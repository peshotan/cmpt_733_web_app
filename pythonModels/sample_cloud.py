import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

import warnings
warnings.simplefilter("ignore")

df1 = pd.read_csv('./BC_pred_weather.csv',index_col=0)
df2 = pd.read_csv('./BC_without_weather.csv',index_col=0)

cities = df1['city'].unique()

c=cities[0]
newdf1 = df1[df1['city']==c]
df1a = newdf1[['date','city','actual']]
df1b = newdf1[['date','city','predict']]
newdf2 = df2[df2['city']==c]
df2b = newdf2[['date','city','predict']]
fig = go.Figure()
fig.add_trace(go.Scatter(x=df1a['date'],y=df1a['actual'],mode='lines',name='actual',visible=True))
fig.add_trace(go.Scatter(x=df1b['date'],y=df1b['predict'],mode='lines',name='predicted with weather',visible=True))
fig.add_trace(go.Scatter(x=df2b['date'],y=df2b['predict'],mode='lines',name='predicted without weather',visible=True))
fig.update_layout(title=c+' PREDICTIONS',template='plotly_dark',colorway=['rgb(247,104,161)','rgb(173,221,142)','rgb(65,182,196)'])

cities = np.delete(cities,0)

cities = cities[0:11]

for c in cities:
    newdf1 = df1[df1['city']==c]
    df1a = newdf1[['date','city','actual']]
    df1b = newdf1[['date','city','predict']]
    newdf2 = df2[df2['city']==c]
    df2b = newdf2[['date','city','predict']]
    fig.add_trace(go.Scatter(x=df1a['date'],y=df1a['actual'],mode='lines',name='actual',visible=False))
    fig.add_trace(go.Scatter(x=df1b['date'],y=df1b['predict'],mode='lines',name='predicted with weather',visible=False))
    fig.add_trace(go.Scatter(x=df2b['date'],y=df2b['predict'],mode='lines',name='predicted without weather',visible=False))


fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label='CAMPBELL RIVER',
                     method="update",
                     args=[{"visible": [True, True, True,
                                        False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                                        ]},
                           ]),
                dict(label=cities[0],
                     method="update",
                     args=[{"visible": [False,False, False,
                                        True, True, True,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,

                     ]},
                           ]),
                dict(label=cities[1],
                     method="update",
                     args=[{"visible": [False,False, False,
                                        False, False,False,
                                        True, True, True,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,

                     ]},
                           ]),
                dict(label=cities[2],
                     method="update",
                     args=[{"visible": [ False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        True, True, True,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                     ]},
                           ]),
                dict(label=cities[3],
                     method="update",
                     args=[{"visible": [ False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        True, True, True,
                                        False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,

                                       ]},
                           ]),
                dict(label=cities[4],
                     method="update",
                     args=[{"visible": [ False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        True, True, True,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                     ]},
                           ]),
                dict(label=cities[5],
                     method="update",
                     args=[{"visible": [ False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                                        True, True, True,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,

                     ]},
                           ]),
                dict(label=cities[6],
                     method="update",
                     args=[{"visible": [ False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        True, True, True,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,

                     ]},
                           ]),
                dict(label=cities[7],
                     method="update",
                     args=[{"visible": [ False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        True, True, True,
                                        False,False, False,
                                        False, False,False,

                     ]},
                           ]),
                dict(label=cities[8],
                     method="update",
                     args=[{"visible": [ False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        True, True, True,
                                        False, False,False,

                     ]},
                           ]),
                dict(label=cities[9],
                     method="update",
                     args=[{"visible": [ False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                                        False, False, False,
                                        False, False, False,
                                        False,False, False,
                                        False, False,False,
                                        True, True, True,
                                       ]},
                           ]),
            ]),
        )
    ])

fig.update_layout(title="Citywise Predictions")

fig.show()


#username
username = 'peshotan'
#API key
api_key = 'Your API KEY'

import chart_studio


chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

import chart_studio.plotly as py
import chart_studio.tools as tls

py.plot(fig, file_name='city_new_3', auto_open=True)