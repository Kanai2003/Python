import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta



app = dash.Dash()

df = pd.read_csv('../data/ETH-USD.csv');

app.layout = html.Div([
    # go.Figure(data=[go.Candlestick(x=df['Date'],
    #             open=df['Open'],
    #             high=df['High'],
    #             low=df['Low'],
    #             close=df['Close'])])

    html.H1(children= 'Ethereum ETH-USD'),
    html.H2(df.iloc[-1]['Close']),

    dcc.Graph(
        id='stock-visualizer',
        figure = {
            'data' : [
                go.Candlestick(x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close']
                )
            ],
            'layout' : go.Layout(
                yaxis=dict(
                    autorange = True,
                    fixedrange= False,
                    label = "Price $",
                ),
                title = 'Etherium ETH',
                xaxis=dict(
                    autorange = True,
                    label = "Time",
                    rangeselector=dict(
                        buttons=list([
                            dict(count=7,
                                label="1w",
                                step="day",
                                stepmode="backward"
                            ),
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=6,
                                label="6m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="YTD",
                                step="year",
                                stepmode="todate"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ])
                    ),
                    rangeslider=dict(
                        visible=True
                    ),
                    type="date"
                ),
            )
                        
        },
        style={'width': '95vw', 'height': '95vh'}
    ),
])

if __name__ == "__main__": 
    app.run_server(port = 4050)