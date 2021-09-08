from django.shortcuts import render
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go
import pyEX as p

# Create your views here.
df = pd.read_json(r'Stock_List.json')


def home(request):
    return render(request, 'home.html')


def get_data(request):
    name = request.POST['name']
    c = p.Client(api_token='pk_ec2f6c0bc76c4cf1a67577c72fd3f5a0', version='stable')
    info = c.quote(symbol=name)
    print(df)
    print('info:', info)

    data = df[df['symbol'] == name]
    print(data)
    layout = go.Layout(
        xaxis={'title': 'day'},
        yaxis={'title': 'price'},
    )
    fig = go.Figure(data=[go.Ohlc(x=data['date'],
                                  open=data['open'],
                                  close=data['close'],
                                  high=data['high'],
                                  low=data['low']
                                  )], layout=layout)
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1d",
                         step="day",
                         stepmode="backward"),
                    dict(count=2,
                         label="2d",
                         step="day",
                         stepmode="backward"),
                    dict(count=3,
                         label="3d",
                         step="day",
                         stepmode="backward"),
                    dict(count=5,
                         label="5d",
                         step="day",
                         stepmode="backward"),
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    plot1 = plot(fig, output_type='div')

    fig2 = go.Figure(data=[go.Candlestick(x=data['date'],
                                          open=data['open'],
                                          close=data['close'],
                                          high=data['high'],
                                          low=data['low']
                                          )], layout=layout)
    fig2.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1d",
                         step="day",
                         stepmode="backward"),
                    dict(count=2,
                         label="2d",
                         step="day",
                         stepmode="backward"),
                    dict(count=3,
                         label="3d",
                         step="day",
                         stepmode="backward"),
                    dict(count=5,
                         label="5d",
                         step="day",
                         stepmode="backward"),
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    plot2 = plot(fig2, output_type='div')
    return render(request, 'plots.html', {
        'plot1': plot1,
        'plot2': plot2,
        'info': info
    })
