import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
from  testeProjectFlask.file_controller import file_controller


class operations_controller(object):
    """description of class"""

    def create_plot(measure):


        x = measure['x']
        y = measure['y']
        df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


        data = [#go.Bar(
            #    x=df['x'], # assign x as the dataframe column 'x'
            #    y=df['y']
            #)
            go.Scatter(x = df['x'],
                        y = df['y'],
                        mode = 'markers'
                    )]

        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

        return graphJSON


     def create_plot(measure):


        x = measure['x']
        y = measure['y']
        df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


        data = [#go.Bar(
            #    x=df['x'], # assign x as the dataframe column 'x'
            #    y=df['y']
            #)
            go.Scatter(x = df['x'],
                        y = df['y'],
                        mode = 'markers'
                    )]

        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

        return graphJSON


    def create_random_plot():

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

