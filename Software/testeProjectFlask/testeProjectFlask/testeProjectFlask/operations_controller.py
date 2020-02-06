import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
from  testeProjectFlask.file_controller import file_controller
from scipy.fftpack import fft
from scipy import signal

class operations_controller(object):
    """description of class"""
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def GeraEquacaoDeDiferencas(self,x,y):
        df = np.zeros_like(x)       # df/dx
        dx = x[1] - x[0]
        # Internal mesh points
        for i in range(1, len(x) - 1):
            df[i] = (y[i + 1] - y[i - 1]) / (2 * dx)
        # End points
        df[0] = (y[1] - y[0]) / dx
        df[-1] = (y[-1] - y[-2]) / dx
        return df

    def create_plot(self,measure):


        x = measure['x']
        y = measure['y']
        df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


        data = [#go.Bar(
            #    x=df['x'], # assign x as the dataframe column 'x'
            #    y=df['y']
            #)
            go.Scatter(x = df['x'],
                        y = df['y'],
                        mode = 'markers')]

        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

        return graphJSON


    def create_derivate_plot(self, measure):


        x = measure['x']
        y = measure['y']
        x = list(map(float, x))
        y = list(map(float, y))
        dy = self.GeraEquacaoDeDiferencas(x,y)
        dy2 = self.GeraEquacaoDeDiferencas(x,dy)
        dy2 = dy2[3:-2]
        dx2 = x[3:-2]

        data = [{
            'x': dx2,
            'y': dy2,
            'type': 'scatter',
            'name': 'Segunda Derivada'
            },{
              'x': x,
              'y': dy,
              'xaxis': 'x2',
              'yaxis': 'y2',
              'type': 'scatter',
              'name': 'Primeira Derivada'
            },{
              'x': x,
              'y': y,
              'xaxis': 'x3',
              'yaxis': 'y3',
              'type': 'scatter',
              'name': 'Original'
            }]

        layout = {
                'grid': {
                'rows': 3,
                'columns': 1,
                'pattern': 'independent',
                'roworder': 'bottom to top'}
            }

        data = {
            'data': data,
            'layout': layout
        }

        graphJSON = json.dumps(data, cls = plotly.utils.PlotlyJSONEncoder)

        return graphJSON


    def create_random_plot(self):

        N = 40
        x = np.linspace(0, 1, N)
        y = np.random.randn(N)
        df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


        data = [#go.Bar(
            #    x=df['x'], # assign x as the dataframe column 'x'
            #    y=df['y']
            #)
            go.Scatter(x = df['x'],
                        y = df['y'],
                        #mode = 'markers'
                    )]

        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

        return graphJSON

    def create_fft_plot(self, measure):

        x = measure['x']
        y = measure['y']
        x = list(map(float, x))
        y = list(map(float, y))
        yf = fft(y)
        T = 0.05
        N = int(x[-1]/T)
        xf = list(np.linspace(0.0, 1.0 / (2.0 * T), N // 2))
        yfp = 2.0 / N * np.abs(yf[0:N // 2])

        #df = pd.DataFrame({'x': xf, 'y': yfp}) # creating a sample dataframe


        #data = [
        #    go.Scatter(x = df['x'],
        #                y = df['y'],
        #            )]
        data = [{
            'x': xf,
            'y': yfp,
            'type': 'scatter',
            'name': 'Segunda Derivada'
            }]

        layout = {}

        data = {
            'data': data,
            'layout': layout
        }


        graphJSON = json.dumps(data, cls = plotly.utils.PlotlyJSONEncoder)

        return graphJSON




