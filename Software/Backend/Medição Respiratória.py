import matplotlib.pyplot as plt
import matplotlib.dates as dt
import numpy as np
import datetime
import scipy.interpolate as interpolate
from sympy import symbols


class TimePoint:

    def __init__(self,hours,minutes,seconds,milliseconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds 
        self.milliseconds = milliseconds 



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


def ConvertListOfStringDatesToNums(dates):        
    list_of_datetimes = [datetime.datetime.strptime(date, '%H:%M:%S.%f') for date in dates]
    list_of_datetimes = dt.date2num(list_of_datetimes)       
    return list_of_datetimes

def ConvertListOfStringDatesToTimeDelta(dates):
    list_of_times = []
    for time in dates:
        (hours,minutes,seconds) =  time.split(':')
        (seconds,milliseconds) = seconds.split('.')
        list_of_times.append(TimePoint(hours,minutes,seconds,milliseconds))
    return list_of_times


def GetDeltaTime(dates):
    list_of_deltas = []
    list_of_datetimes = [datetime.datetime.strptime(date, '%H:%M:%S.%f') for date in dates]
    for time in list_of_datetimes:
        delta = time - list_of_datetimes[0]
        list_of_deltas.append(delta)
    return list_of_deltas

def ConvertListOfDeltaToListOfSeconds(deltas):
    list_of_deltaseconds = []
    for deltasecond in deltas:
        list_of_deltaseconds.append(deltasecond.seconds + deltasecond.microseconds*0.00001) 
    return list_of_deltaseconds

def GetContinuousFunction(x,y):
    xfine = np.linspace(0,30)    
    yinterp = np.interp(xfine,x,y)    
    return yinterp


def PlotInterpolateAnd2Derivates(x,interpolate, derivate, derivate2,paciente,nomeDoArquivo):

    titulo = 'Medição Respiratória Paciente: ' + paciente

    ax1 = plt.subplot(311)
    plt.title(titulo)
    plt.ylabel('Interpolação')
    plt.grid(True)
    plt.plot(interpolate(x),color='black')    
    plt.setp(ax1.get_xticklabels(), visible=False)

    ax2 = plt.subplot(312, sharex=ax1)
    plt.grid(True)
    plt.ylabel('Derivada 1')
    plt.plot(derivate(x), color='blue')
    plt.setp(ax2.get_xticklabels(), visible=False)

    ax3 = plt.subplot(313, sharex=ax1)
    plt.ylabel('Derivada 2')
    plt.xlabel('Tempo (s)')
    plt.grid(True)
    plt.plot(derivate2(x), color='red')
    plt.setp(ax3.get_xticklabels())

    plt.savefig(nomeDoArquivo)

filename = "teste.png"
datas = ['22:00:24.509','22:00:25.527','22:00:26.512','22:00:27.526','22:00:28.511','22:00:29.529','22:00:30.515','22:00:31.532','22:00:32.519','22:00:33.536','22:00:34.520','22:00:35.538','22:00:36.526','22:00:37.548','22:00:38.530','22:00:39.547','22:00:40.533','22:00:41.555','22:00:42.538','22:00:43.560','22:00:44.548','22:00:45.568','22:00:46.555','22:00:47.542','22:00:48.559','22:00:49.572','22:00:50.561','22:00:51.573','22:00:52.554']
values = [1023,1023,1022,1023,1023,1023,1023,1022,1023,1022,1023,1023,997,1007,1022,1009,1006,1016,1023,1012,997,1003,1013,1003,985,993,1008,1018,1023]
delta = GetDeltaTime(datas)
delta = ConvertListOfDeltaToListOfSeconds(delta)
fy = GetContinuousFunction(delta,values)



#função de teste
paciente = 'Bruno'
x = np.arange(-100,100,1)
y = pow(x,3)
print(y)
plt.plot(x,y,'b^')
plt.savefig('Função original')

#Interpolador de Lagrange
lagrangeinterpolate = interpolate.lagrange(x,y)
lagrangeDerivate = lagrangeinterpolate.deriv()
lagrangeDerivate2 = lagrangeDerivate.deriv()
print(lagrangeinterpolate)
PlotInterpolateAnd2Derivates(x,lagrangeinterpolate, lagrangeDerivate, lagrangeDerivate2,paciente,"Interpolação por Lagrange")

#tentando derivar de outra maneira


#UnivariateSpline
UnivariateSplineInterpolate = interpolate.UnivariateSpline(x,y)
print(UnivariateSplineInterpolate)
UnivariateSplineDerivate = UnivariateSplineInterpolate.derivative()
UnivariateSplineDerivate2 = UnivariateSplineInterpolate.derivative(2)
PlotInterpolateAnd2Derivates(x,lagrangeinterpolate, lagrangeDerivate, lagrangeDerivate2,paciente,"Interpolação por UnivariateSpline")