import matplotlib.pyplot as plt
import matplotlib.dates as dt
import numpy as np
import datetime


class MedidorDeRespiracao:

    def ShowPlot(x,function):
        plt.plot(x,function)
        plt.show()        

    def SavePlot(x,function,filename):
        plt.plot(x,function)
        plt.savefig(filename, dpi=None, facecolor='w', edgecolor='black',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                frameon=None, metadata=None)

    def ShowPlotDate(x,function):
        plt.plot_date(x,function)
        plt.show()        

    def SavePlotDate(x,function,filename):
        plt.plot_date(x,function)
        plt.savefig(filename, dpi=None, facecolor='w', edgecolor='black',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                frameon=None, metadata=None)


    def ConvertListOfDatesToNums(dates):        
        list_of_datetimes = [datetime.datetime.strptime(date, '%H:%M:%S.%f') for date in dates]
        list_of_datetimes = dt.date2num(list_of_datetimes)
        return list_of_datetimes

# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# function = np.sin(x)
# fname = "teste.png"

# p1 = MedidorDeRespiracao(x,function)
# p1.showPlot()
# p1.savePlot(fname)

filename = "teste.png"
datas = ['22:00:24.509','22:00:25.527','22:00:26.512','22:00:27.526','22:00:28.511','22:00:29.529','22:00:30.515','22:00:31.532','22:00:32.519','22:00:33.536','22:00:34.520','22:00:35.538','22:00:36.526','22:00:37.548','22:00:38.530','22:00:39.547','22:00:40.533','22:00:41.555','22:00:42.538','22:00:43.560','22:00:44.548','22:00:45.568','22:00:46.555','22:00:47.542','22:00:48.559','22:00:49.572','22:00:50.561','22:00:51.573','22:00:52.554']
values = [1023,1023,1022,1023,1023,1023,1023,1022,1023,1022,1023,1023,997,1007,1022,1009,1006,1016,1023,1012,997,1003,1013,1003,985,993,1008,1018,1023]
x = MedidorDeRespiracao.ConvertListOfDatesToNums(datas)
MedidorDeRespiracao.SavePlotDate(x,values, filename)
MedidorDeRespiracao.ShowPlotDate(x,values)
