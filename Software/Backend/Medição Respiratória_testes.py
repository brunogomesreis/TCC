import matplotlib.pyplot as plt
import numpy as np
import datetime
import scipy.interpolate as interpolate
from sympy import symbols
import os
import time
import csv

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

def GerarGraficosDerivadas(x,xajust,interpolate, derivate, derivate2,paciente,nomeDoArquivo):

    titulo = 'Medição Respiratória Paciente: ' + paciente
    plt.figure()

    ax1 = plt.subplot(311)
    plt.title(titulo)
    plt.ylabel('Interpolação')
    plt.grid(True)
    plt.plot(interpolate(xajust),color='black')    
    plt.scatter(x,y,color='BLUE')    
    plt.setp(ax1.get_xticklabels(), visible=False)

    ax2 = plt.subplot(312, sharex=ax1)
    plt.grid(True)
    plt.ylabel('Derivada 1')
    plt.plot(derivate(xajust), color='blue')
    plt.setp(ax2.get_xticklabels(), visible=False)

    ax3 = plt.subplot(313, sharex=ax1)
    plt.ylabel('Derivada 2')
    plt.xlabel('Tempo (s)')
    plt.grid(True)
    plt.plot(derivate2(xajust), color='red')
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
xajust = []
for j in range(1,len(x)-1):
    xajust.append(x[j])


#Pegando os dados reais de uma respiração
with open('test_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    x0 = 0
    x = []
    y = []
    for row in csv_reader:
        if line_count == 0:
            x0 = int(row[0])
            print('o x0 é:')
            print(x0)
            x.append(0)
            y.append(float(row[1]))
        else:
            print(f'{", ".join(row)}')
            numero = int(row[0]) - x0
            x.append(numero) 
            y.append(float(row[1]))
        line_count += 1
    print (line_count)
    print(x)
    print(y)


#Condições iniciais
print('Digite o nome do Paciente:')
paciente = input()
subpasta = os.getcwd() + "\\" + "Medições" + "\\" + paciente + "\\" + datetime.datetime.now().strftime("%y-%m-%d - %H%M%S") + "\\"
pastaRegressao = "Regressão Polinomial\\"
print(subpasta)
if not os.path.exists(subpasta):
    CriarNovoDiretorio(subpasta)
    CriarNovoDiretorio(subpasta + pastaRegressao)


#Transformada de fourier


#Função original
plt.figure()
plt.plot(x,y,'b^')
plt.xlabel('Tempo (s)')
plt.ylabel('Sinal de entrada (int)')
plt.savefig(subpasta + 'Função original')

#Função automaticamente interpolada
plt.figure()
plt.plot(x,y,color='black')
plt.xlabel('Tempo (s)')
plt.ylabel('Sinal de entrada (int)')
plt.savefig(subpasta + 'Função original Interpolada')


#Interpolador de Lagrange
lagrangeinterpolate = interpolate.lagrange(x,y)
lagrangeDerivate = lagrangeinterpolate.deriv()
lagrangeDerivate2 = lagrangeDerivate.deriv()
GerarGraficosDerivadas(x,xajust,lagrangeinterpolate, lagrangeDerivate, lagrangeDerivate2,paciente, subpasta +  "Interpolação por Lagrange")

#Regressao polinomial

for i in range(0,100):
    a = np.polyfit(x,y, i)
    b = np.poly1d(a)
    deriv1 = b.deriv()
    deriv2 = deriv1.deriv()    
    GerarGraficosDerivadas(x,xajust,b, deriv1, deriv2,paciente, subpasta + pastaRegressao + "Regressão polinomial de grau " + str(i))
    

#derivando por equaçaõ de diferenças  
df = GeraEquacaoDeDiferencas(x,y)
df2 = GeraEquacaoDeDiferencas(x,df)
GerarGráficosDeEquacaoDeDiferencas(x,y, df, df2,paciente,subpasta + 'Equações de Diferenças')

#UnivariateSpline
UnivariateSplineInterpolate = interpolate.UnivariateSpline(x,y)
UnivariateSplineDerivate = UnivariateSplineInterpolate.derivative()
UnivariateSplineDerivate2 = UnivariateSplineInterpolate.derivative(2)
GerarGraficosDerivadas(x,xajust,UnivariateSplineInterpolate, UnivariateSplineDerivate, UnivariateSplineDerivate2,paciente,subpasta + "Interpolação por UnivariateSpline")