import matplotlib.pyplot as plt
import matplotlib.dates as dt
import numpy as np
import datetime
import scipy.interpolate as interpolate
from sympy import symbols
import os

class TimePoint:

    def __init__(self,hours,minutes,seconds,milliseconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds 
        self.milliseconds = milliseconds 

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

def GerarGraficosDerivadas(x,interpolate, derivate, derivate2,paciente,nomeDoArquivo):

    titulo = 'Medição Respiratória Paciente: ' + paciente
    plt.figure()

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
    plt.close

def GerarGráficosDeEquacaoDeDiferencas(x,y, df, df2,paciente,nomeDoArquivo):

    titulo = 'Medição Respiratória Paciente: ' + paciente
    plt.figure()

    ax1 = plt.subplot(311)
    plt.title(titulo)
    plt.ylabel('Interpolação')
    plt.grid(True)
    plt.plot(x,y,color='black')    
    plt.setp(ax1.get_xticklabels(), visible=False)

    ax2 = plt.subplot(312, sharex=ax1)
    plt.grid(True)
    plt.ylabel('Derivada 1')
    plt.plot(x,df, color='blue')
    plt.setp(ax2.get_xticklabels(), visible=False)

    ax3 = plt.subplot(313, sharex=ax1)
    plt.ylabel('Derivada 2')
    plt.xlabel('Tempo (s)')
    plt.grid(True)
    plt.plot(x,df2, color='red')
    plt.setp(ax3.get_xticklabels())

    plt.savefig(nomeDoArquivo)


def GeraEquacaoDeDiferencas(x,y):
    df =  np.zeros_like(x)       # df/dx
    dx = x[1] - x[0]
    # Internal mesh points
    for i in range(1, len(x) - 1):
        df[i] = (y[i+1] - y[i-1])/(2*dx)
    # End points
    df[0]  = (y[1]  - y[0]) /dx
    df[-1] = (y[-1] - y[-2])/dx
    return df


def CriarNovoDiretorio(path):
    try:
        os.makedirs(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)


filename = "teste.png"
datas = ['22:00:24.509','22:00:25.527','22:00:26.512','22:00:27.526','22:00:28.511','22:00:29.529','22:00:30.515','22:00:31.532','22:00:32.519','22:00:33.536','22:00:34.520','22:00:35.538','22:00:36.526','22:00:37.548','22:00:38.530','22:00:39.547','22:00:40.533','22:00:41.555','22:00:42.538','22:00:43.560','22:00:44.548','22:00:45.568','22:00:46.555','22:00:47.542','22:00:48.559','22:00:49.572','22:00:50.561','22:00:51.573','22:00:52.554']
y = [1023,1023,1022,1023,1023,1023,1023,1022,1023,1022,1023,1023,997,1007,1022,1009,1006,1016,1023,1012,997,1003,1013,1003,985,993,1008,1018,1023]
delta = GetDeltaTime(datas)
x = ConvertListOfDeltaToListOfSeconds(delta)

#função de teste
x = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
y = []
for i in x:    
    y.append(pow(i,3))  

#Condições iniciais
print('Digite o nome do Paciente:')
paciente = input()
subpasta = os.getcwd() + "\\" + "Medições" + "\\" + paciente + "\\" + datetime.datetime.now().strftime("%y-%m-%d - %H%M%S") + "\\"
print(subpasta)
if not os.path.exists(subpasta):
    CriarNovoDiretorio(subpasta)
plt.figure()
plt.plot(x,y,'b^')
plt.savefig(subpasta + 'Função original')

#Interpolador de Lagrange
lagrangeinterpolate = interpolate.lagrange(x,y)
lagrangeDerivate = lagrangeinterpolate.deriv()
lagrangeDerivate2 = lagrangeDerivate.deriv()
GerarGraficosDerivadas(x,lagrangeinterpolate, lagrangeDerivate, lagrangeDerivate2,paciente, subpasta +  "Interpolação por Lagrange")

#derivando por equaçaõ de diferenças  
df = GeraEquacaoDeDiferencas(x,y)
df2 = GeraEquacaoDeDiferencas(x,df)
GerarGráficosDeEquacaoDeDiferencas(x,y, df, df2,paciente,subpasta + 'Equações de Diferenças')

#UnivariateSpline
UnivariateSplineInterpolate = interpolate.UnivariateSpline(x,y)
UnivariateSplineDerivate = UnivariateSplineInterpolate.derivative()
UnivariateSplineDerivate2 = UnivariateSplineInterpolate.derivative(2)
GerarGraficosDerivadas(x,UnivariateSplineInterpolate, UnivariateSplineDerivate, UnivariateSplineDerivate2,paciente,subpasta + "Interpolação por UnivariateSpline")