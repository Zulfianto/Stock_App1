import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import pandas_ta as ta
from datetime import timedelta
import warnings
from dash_auth import BasicAuth
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
from dash.exceptions import PreventUpdate

def data_frame(input_value):
    df = yf.download(tickers=input_value, period="4d", interval='1m')
    df['SMA20'] = df.ta.sma(length=20)
    df['SMA12'] = df.ta.sma(length=12)
    df['EMA8'] = df.ta.ema(length=8)
    df['BBL_20_2.0'] = df.ta.bbands(length=20)['BBL_20_2.0']
    df['BBU_20_2.0'] = df.ta.bbands(length=20)['BBU_20_2.0']
    df['RSI'] = df.ta.rsi(length=14)
    df['RSISMA'] = ta.sma(df.RSI, length=50)
    df['MACD_12_26_9'] = df.ta.macd(fast=12, slow=21, signal=9)['MACD_12_21_9']
    df['MACDh_12_26_9'] = df.ta.macd(fast=12, slow=21, signal=9)['MACDh_12_21_9']
    df['MACDs_12_26_9'] = df.ta.macd(fast=12, slow=21, signal=9)['MACDs_12_21_9']
    df['SUPERTl_7_3.0'] = df.ta.supertrend(length=7, multiplier=3)['SUPERTl_7_3.0']
    df['SUPERTs_7_3.0'] = df.ta.supertrend(length=7, multiplier=3)['SUPERTs_7_3.0']
    df['SUPERTl_14_5.0'] = df.ta.supertrend(length=14, multiplier=5)['SUPERTl_14_5.0']
    df['SUPERTs_14_5.0'] = df.ta.supertrend(length=14, multiplier=5)['SUPERTs_14_5.0']
    df['SUPERTl_14_4.5'] = df.ta.supertrend(length=14, multiplier=4.5)['SUPERTl_14_4.5']
    df['SUPERTs_14_4.5'] = df.ta.supertrend(length=14, multiplier=4.5)['SUPERTs_14_4.5']
    #df['VWAP_D'] = df.ta.vwap()
    df['PSARl_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARl_0.02_0.2']
    df['PSARs_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARs_0.02_0.2']
    df['STOCHk_14_3_3'] = df.ta.stoch(k=14, d=3, smooth_k=3)['STOCHk_14_3_3']
    df['STOCHd_14_3_3'] = df.ta.stoch(k=14, d=3, smooth_k=3)['STOCHd_14_3_3']
    df['Last_Close'] = df.Close[-1].round(decimals=2)
    return df


def data_frame1(input_value):
    df = yf.download(tickers=input_value, period="4d", interval='5m')
    df['SMA20'] = df.ta.sma(length=20)
    df['SMA12'] = df.ta.sma(length=12)
    df['EMA8'] = df.ta.ema(length=8)
    df['BBL_20_2.0'] = df.ta.bbands(length=20)['BBL_20_2.0']
    df['BBU_20_2.0'] = df.ta.bbands(length=20)['BBU_20_2.0']
    df['RSI'] = df.ta.rsi(length=14)
    df['RSISMA'] = ta.sma(df.RSI, length=50)
    df['MACD_12_26_9'] = df.ta.macd(fast=12, slow=21, signal=9)['MACD_12_21_9']
    df['MACDh_12_26_9'] = df.ta.macd(fast=12, slow=21, signal=9)['MACDh_12_21_9']
    df['MACDs_12_26_9'] = df.ta.macd(fast=12, slow=21, signal=9)['MACDs_12_21_9']
    df['SUPERTl_7_3.0'] = df.ta.supertrend(length=7, multiplier=3)['SUPERTl_7_3.0']
    df['SUPERTs_7_3.0'] = df.ta.supertrend(length=7, multiplier=3)['SUPERTs_7_3.0']
    df['SUPERTl_14_5.0'] = df.ta.supertrend(length=14, multiplier=5)['SUPERTl_14_5.0']
    df['SUPERTs_14_5.0'] = df.ta.supertrend(length=14, multiplier=5)['SUPERTs_14_5.0']
    df['SUPERTl_14_4.5'] = df.ta.supertrend(length=14, multiplier=4.5)['SUPERTl_14_4.5']
    df['SUPERTs_14_4.5'] = df.ta.supertrend(length=14, multiplier=4.5)['SUPERTs_14_4.5']
    #df['VWAP_D'] = df.ta.vwap()
    df['PSARl_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARl_0.02_0.2']
    df['PSARs_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARs_0.02_0.2']
    df['STOCHk_14_3_3'] = df.ta.stoch(k=14, d=3, smooth_k=3)['STOCHk_14_3_3']
    df['STOCHd_14_3_3'] = df.ta.stoch(k=14, d=3, smooth_k=3)['STOCHd_14_3_3']
    df['Last_Close'] = df.Close[-1].round(decimals=2)
    return df


def data_frame2(input_value):
    df = yf.download(tickers=input_value, period="4d", interval='15m')
    df['BBL_20_2.0'] = df.ta.bbands(length=20)['BBL_20_2.0']
    df['BBU_20_2.0'] = df.ta.bbands(length=20)['BBU_20_2.0']
    df['RSI'] = df.ta.rsi(length=14)
    df['PSARl_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARl_0.02_0.2']
    df['PSARs_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARs_0.02_0.2']
    return df

#def data_frame3(input_value):
    #df = yf.download(tickers=input_value, period="5d", interval='30m')
    #df['BBL_20_2.0'] = df.ta.bbands(length=20)['BBL_20_2.0']
    #df['BBU_20_2.0'] = df.ta.bbands(length=20)['BBU_20_2.0']
    #df['RSI'] = df.ta.rsi(length=14)
    #df['PSARl_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARl_0.02_0.2']
    #df['PSARs_0.02_0.2'] = df.ta.psar(af0=0.02, af=0.02, max_af=0.2)['PSARs_0.02_0.2']
    #return df

warnings.simplefilter('ignore', UserWarning)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server
auth = BasicAuth(app, {'zulfianto@yahoo.co.id': '070786'})


app.layout = html.Div([
    html.Div([
        dbc.Input(id="stock-input", placeholder="Search for a Symbol...", type="text", value='NFLX', style={'width': '200px', 'float': 'left', 'position': 'relative',
                    'left': '100px', 'top': '7px'}),
        dbc.Button(id="submit-button", n_clicks=0, children="Search", color="primary", className="me-1", style={'width': '100px', 'position': 'relative',
                    'float': 'left', 'left': '105px', 'top': '7px' }),
        html.H2("ZULFIANTO Stock App", style={'color': 'black', 'position': 'relative', 'float': 'left', 'left': '300px',
                                              'top': '5px', 'padding-top': '1px', 'margin-left': '2%', 'display': 'inline-block'}),
        html.Img(src="/assets/stock-icon.png", style={'position': 'relative', 'float': 'right', 'right': '20px', 'height': '50px'},)
        ],
        style={'height': '50px', 'margin': '0px 0px 10px', 'background-color': 'rgb(66,196,247)','border-radius': '2px' }),


    html.Div([
        dbc.Row([
            dbc.Col([html.Div([
                #dcc.Graph(figure=data)
                dcc.Graph(id="graph1", animate=False, config={"displaylogo": False}),
                dcc.Interval(id="graph-update1", disabled=False, interval=5*1000, max_intervals=-1, n_intervals=0)
                ],
                style={'margin': '0px 0px 0px 0px', 'width': '98%'}),]),
            dbc.Col([html.Div([
                #dcc.Graph(figure=data1)
                dcc.Graph(id="graph", animate=False, config={"displaylogo": False}),
                dcc.Interval(id="graph-update", disabled=False, interval=5*1000, max_intervals=-1, n_intervals=0)
                ],
                style={'margin': '0px 0px 0px 0px', 'width': '98%'}),])
        ], className="g-0")
        ])
    ])


@app.callback(
    Output(component_id="graph", component_property="figure"),
    [Input(component_id="submit-button", component_property="n_clicks"),
    Input(component_id="graph-update", component_property="n_intervals")],
    [State(component_id="stock-input", component_property="value")],
    prevent_initial_call=True)
def display_candlestick(n_clicks, input_data, input_value):
    df = data_frame(input_value)
    df1 = data_frame1(input_value)
    data = go.Figure()

    data.add_trace(go.Candlestick(
        x=df.index[-80:],
        open=df.Open[-80:],
        high=df.High[-80:],
        low=df.Low[-80:],
        close=df.Close[-80:],
        name='candlestick', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-16:],
        y=df1.SMA20[-16:],
        name='SMA20',
        mode='lines',
        line=dict(color='orange', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df.SMA12[-80:],
        name='SMA12',
        mode='lines',
        line=dict(color='red', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df.EMA8[-80:],
        name='EMA8',
        mode='lines',
        line=dict(color='blue', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['BBL_20_2.0'][-80:],
        name='BBL',
        mode='lines',
        line=dict(color='black', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['BBU_20_2.0'][-80:],
        name='BBU',
        mode='lines',
        line=dict(color='black', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-16:],
        y=df1['BBL_20_2.0'][-16:],
        name='BBL',
        mode='lines',
        line=dict(color='orange', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-16:],
        y=df1['BBU_20_2.0'][-16:],
        name='BBU',
        mode='lines',
        line=dict(color='orange', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['PSARl_0.02_0.2'][-80:],
        name='PSARL',
        mode='markers', marker=dict(
            color="black", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['PSARs_0.02_0.2'][-80:],
        name='PSARS',
        mode='markers', marker=dict(
            color="black", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-16:],
        y=df1['PSARl_0.02_0.2'][-16:],
        name='PSARL',
        mode='markers', marker=dict(
            color="green", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-16:],
        y=df1['PSARs_0.02_0.2'][-16:],
        name='PSARS',
        mode='markers', marker=dict(
            color="red", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    #data.add_trace(go.Scatter(
        #x=df.index[-80:],
        #y=df['VWAP_D'][-80:],
        #name='VWAP',
        #mode='lines',
        #line=dict(color='purple', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['SUPERTl_7_3.0'][-80:],
        name='SUPERTl',
        mode='lines',
        line=dict(color='green', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['SUPERTs_7_3.0'][-80:],
        name='SUPERTs',
        mode='lines',
        line=dict(color='red', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['SUPERTl_14_5.0'][-80:],
        name='SUPERTl',
        mode='lines',
        line=dict(color='green', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['SUPERTs_14_5.0'][-80:],
        name='SUPERTs',
        mode='lines',
        line=dict(color='red', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['RSI'][-80:],
        name='RSI',
        mode='lines',
        line=dict(color='black', width=3), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['RSISMA'][-80:],
        name='RSISMA',
        mode='lines',
        line=dict(color='gray', width=2), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['STOCHk_14_3_3'][-80:],
        name='STOCHk_14_3_3',
        mode='lines',
        line=dict(color='blue', width=2), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['STOCHd_14_3_3'][-80:],
        name='STOCHd_14_3_3',
        mode='lines',
        line=dict(color='red', width=2), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['MACD_12_26_9'][-80:],
        name='mACD',
        mode='lines',
        line=dict(color='blue', width=3), yaxis="y1"))

    inc = df['MACDh_12_26_9'][-80:] > 0
    dec = df['MACDh_12_26_9'][-80:] < 0

    data.add_trace(go.Bar(
        x=df.index[-80:][inc],
        y=df['MACDh_12_26_9'][-80:][inc],
        name='MACDh', marker={'color': 'green'},
        yaxis="y1"))

    data.add_trace(go.Bar(
        x=df.index[-80:][dec],
        y=df['MACDh_12_26_9'][-80:][dec],
        name='MACDh', marker={'color': 'red'},
        yaxis="y1"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['MACDs_12_26_9'][-80:],
        name='MACDs',
        mode='lines',
        line=dict(color='red', width=3), yaxis="y1"))

    data.add_shape(type='line', x0=df.index[-80], y0=df['Close'][-1],
                   x1=df.index[-1], y1=df['Close'][-1], line=dict(color='green', width=0.5, dash='dot'),
                   xref="x",
                   yref='y3')

    data.add_shape(type="rect", x0=df.index[-80], y0=70, x1=df.index[-1], y1=100, fillcolor="red",
                   opacity=0.2,
                   xref="x", yref='y2')
    data.add_shape(type="rect", x0=df.index[-80], y0=30, x1=df.index[-1], y1=70, fillcolor="blue",
                   opacity=0.2,
                   xref="x", yref='y2')
    data.add_shape(type="rect", x0=df.index[-80], y0=0, x1=df.index[-1], y1=30, fillcolor="green",
                   opacity=0.2,
                   xref="x", yref='y2')
    data.add_shape(type='line', x0=df.index[-80], y0=50,
                   x1=df.index[-1], y1=50, line=dict(color='black', width=0.5, dash='dot'), xref="x",
                   yref='y2')

    data.add_annotation(
        x=df.index[-1],
        y=df['Close'][-1],
        xref="x",
        yref="y3",
        text=df['Last_Close'][-1],
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=11,
            color="#ffffff"
        ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=30,
        ay=0,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="green",
        opacity=0.8, )

    data.update_layout(
        autosize=True,
        # width=1500,
        paper_bgcolor='#F5F5F5',
        plot_bgcolor='white',
        height=690,
        margin=dict(t=30, l=0, r=0, b=0),
        xaxis=dict(range=[df.index[-80], df.index[-1] + timedelta(minutes=6)], rangeslider_visible=False,
                   rangebreaks=[
                       dict(bounds=["sat", "mon"]),
                       dict(bounds=[16, 9.5], pattern="hour"),
                       # dict(values=["2021-11-25", ])
                   ]),
        yaxis1=dict(domain=[0, 0.2], side='right', linecolor='grey', linewidth=0.01, gridwidth=0.001,
                    gridcolor='grey', ),
        yaxis2=dict(domain=[0.2, 0.4], side='right', linecolor='grey', linewidth=0.01, ),
        yaxis3=dict(domain=[0.4, 1], side='right', showgrid=True,
                    gridwidth=0.001, gridcolor='grey', linecolor='grey', linewidth=0.01), showlegend=False,
        title=(f'{input_value} 1 Min'), title_x=0.5,
    )
    return data

@app.callback(
    Output(component_id="graph1", component_property="figure"),
    [Input(component_id="submit-button", component_property="n_clicks"),
    Input(component_id="graph-update1", component_property="n_intervals")],
    [State(component_id="stock-input", component_property="value")],
    prevent_initial_call=True)
def display_candlestick(n_clicks, input_data, input_value):
    df = data_frame1(input_value)
    df1 = data_frame2(input_value)
    #df2 = data_frame3(input_value)
    data = go.Figure()

    data.add_trace(go.Candlestick(
        x=df.index[-60:],
        open=df.Open[-60:],
        high=df.High[-60:],
        low=df.Low[-60:],
        close=df.Close[-60:],
        name='candlestick', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df.SMA20[-60:],
        name='SMA20',
        mode='lines',
        line=dict(color='orange', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df.SMA12[-60:],
        name='SMA12',
        mode='lines',
        line=dict(color='red', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df.EMA8[-60:],
        name='EMA8',
        mode='lines',
        line=dict(color='blue', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['BBL_20_2.0'][-60:],
        name='BBL',
        mode='lines',
        line=dict(color='black', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['BBU_20_2.0'][-60:],
        name='BBU',
        mode='lines',
        line=dict(color='black', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-20:],
        y=df1['BBL_20_2.0'][-20:],
        name='BBL',
        mode='lines',
        line=dict(color='orange', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-20:],
        y=df1['BBU_20_2.0'][-20:],
        name='BBU',
        mode='lines',
        line=dict(color='orange', width=3), hoverinfo='none', yaxis="y3"))
    
    #data.add_trace(go.Scatter(
        #x=df2.index[-10:],
        #y=df2['BBL_20_2.0'][-10:],
        #name='BBL',
        #mode='lines',
        #line=dict(color='red', width=3), hoverinfo='none', yaxis="y3"))

    #data.add_trace(go.Scatter(
        #x=df2.index[-10:],
        #y=df2['BBU_20_2.0'][-10:],
        #name='BBU',
        #mode='lines',
        #line=dict(color='red', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['PSARl_0.02_0.2'][-60:],
        name='PSARL',
        mode='markers', marker=dict(
            color="black", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['PSARs_0.02_0.2'][-60:],
        name='PSARS',
        mode='markers', marker=dict(
            color="black", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-20:],
        y=df1['PSARl_0.02_0.2'][-20:],
        name='PSARL',
        mode='markers', marker=dict(
            color="green", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df1.index[-20:],
        y=df1['PSARs_0.02_0.2'][-20:],
        name='PSARS',
        mode='markers', marker=dict(
            color="red", opacity=1,
            size=6), hoverinfo='none', yaxis="y3"))

    #data.add_trace(go.Scatter(
        #x=df.index[-60:],
        #y=df['VWAP_D'][-60:],
        #name='VWAP',
        #mode='lines',
        #line=dict(color='purple', width=3), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['SUPERTl_7_3.0'][-60:],
        name='SUPERTl',
        mode='lines',
        line=dict(color='green', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['SUPERTs_7_3.0'][-60:],
        name='SUPERTs',
        mode='lines',
        line=dict(color='red', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['SUPERTl_14_5.0'][-60:],
        name='SUPERTl',
        mode='lines',
        line=dict(color='green', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['SUPERTs_14_5.0'][-60:],
        name='SUPERTs',
        mode='lines',
        line=dict(color='red', width=2), hoverinfo='none', yaxis="y3"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['RSI'][-60:],
        name='RSI',
        mode='lines',
        line=dict(color='black', width=3), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-80:],
        y=df['RSISMA'][-80:],
        name='RSISMA',
        mode='lines',
        line=dict(color='gray', width=2), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['STOCHk_14_3_3'][-60:],
        name='STOCHk_14_3_3',
        mode='lines',
        line=dict(color='blue', width=2), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['STOCHd_14_3_3'][-60:],
        name='STOCHd_14_3_3',
        mode='lines',
        line=dict(color='red', width=2), yaxis="y2"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['MACD_12_26_9'][-60:],
        name='mACD',
        mode='lines',
        line=dict(color='blue', width=3), yaxis="y1"))

    inc = df['MACDh_12_26_9'][-60:] > 0
    dec = df['MACDh_12_26_9'][-60:] < 0

    data.add_trace(go.Bar(
        x=df.index[-60:][inc],
        y=df['MACDh_12_26_9'][-60:][inc],
        name='MACDh', marker={'color': 'green'},
        yaxis="y1"))

    data.add_trace(go.Bar(
        x=df.index[-60:][dec],
        y=df['MACDh_12_26_9'][-60:][dec],
        name='MACDh', marker={'color': 'red'},
        yaxis="y1"))

    data.add_trace(go.Scatter(
        x=df.index[-60:],
        y=df['MACDs_12_26_9'][-60:],
        name='MACDs',
        mode='lines',
        line=dict(color='red', width=3), yaxis="y1"))

    data.add_shape(type='line', x0=df.index[-60], y0=df['Close'][-1],
                   x1=df.index[-1], y1=df['Close'][-1], line=dict(color='green', width=0.5, dash='dot'),
                   xref="x",
                   yref='y3')

    data.add_shape(type="rect", x0=df.index[-60], y0=70, x1=df.index[-1], y1=100, fillcolor="red",
                   opacity=0.2,
                   xref="x", yref='y2')
    data.add_shape(type="rect", x0=df.index[-60], y0=30, x1=df.index[-1], y1=70, fillcolor="blue",
                   opacity=0.2,
                   xref="x", yref='y2')
    data.add_shape(type="rect", x0=df.index[-60], y0=0, x1=df.index[-1], y1=30, fillcolor="green",
                   opacity=0.2,
                   xref="x", yref='y2')
    data.add_shape(type='line', x0=df.index[-60], y0=50,
                   x1=df.index[-1], y1=50, line=dict(color='black', width=0.5, dash='dot'), xref="x",
                   yref='y2')

    data.add_annotation(
        x=df.index[-1],
        y=df['Close'][-1],
        xref="x",
        yref="y3",
        text=df['Last_Close'][-1],
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=11,
            color="#ffffff"
        ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=30,
        ay=0,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="green",
        opacity=0.8, )

    data.update_layout(
        autosize=True,
        # width=1500,
        paper_bgcolor='#F5F5F5',
        plot_bgcolor='white',
        height=690,
        margin=dict(t=30, l=0, r=0, b=0),
        xaxis=dict(range=[df.index[-60], df.index[-1] + timedelta(minutes=22)], rangeslider_visible=False,
                   rangebreaks=[
                       dict(bounds=["sat", "mon"]),
                       dict(bounds=[16, 9.5], pattern="hour"),
                       # dict(values=["2021-11-25", ])
                   ]),
        yaxis1=dict(domain=[0, 0.2], side='right', linecolor='grey', linewidth=0.01, gridwidth=0.001,
                    gridcolor='grey', ),
        yaxis2=dict(domain=[0.2, 0.4], side='right', linecolor='grey', linewidth=0.01, ),
        yaxis3=dict(domain=[0.4, 1], side='right', showgrid=True,
                    gridwidth=0.001, gridcolor='grey', linecolor='grey', linewidth=0.01), showlegend=False,
        title=(f'{input_value} 5 Min'), title_x=0.5,
    )
    return data



if __name__ == '__main__':
    app.run_server(debug=False)
