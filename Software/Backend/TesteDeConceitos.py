# Esse programa deverá percorrer as seguintes etapas:
#     1- Ler os dados de uma porta serial via usb que serão enviados por um arduíno
#     2- Criar uma pastas com o nome e horário das medições para o armazenamento dos arquivos
#     3- Salvar os dados em um arquivo .csv     
#     4- Ler os dados do arquivo csv e realizar as seguintes operações:
#         4.1- Plotar diretamente
#         4.2- Plotar uma interpolação
#         4.3- Calcular a derivada primeira e segunda e plotar
#         4.4- Fazer uma FFT e plotar
#     5- Ler o arquivo csv, passar por um filtro passa baixas, salvar um novo csv e realizar as seguintes operações:
#         5.1- Plotar diretamente
#         5.2- Plotar uma interpolação
#         5.3- Calcular a derivada primeira e segunda e plotar
#         5.4- Fazer uma FFT e plotar


import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import datetime
from scipy.fftpack import fft

# Simulando a etapa 1
#Gerando um sinal padrão para testes
N = 600                 #Numero de pontos
T = 0.05                #Taxa de amostragem
x = np.linspace(0.0, N*T, N)
y = np.sin(0.15 * 2.0*np.pi*x)  + 0.8*np.sin(np.pi/2 + 0.3 * 2.0*np.pi*x) + 0.1*np.sin(np.pi/2 + 30 * 2.0*np.pi*x)


#Etapa 2
def CriarNovoDiretorio(path):
    try:
        os.makedirs(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

print('Digite o nome do Paciente:')
paciente = input()
subpasta = os.getcwd() + "\\" + "Medições" + "\\" + paciente + "\\" + datetime.datetime.now().strftime("%y-%m-%d - %H%M%S") + "\\"
pastaOriginal = "Sinal Original\\"
pastaFiltrado = "Sinal Filtrado\\"
print(subpasta)
if not os.path.exists(subpasta):
    CriarNovoDiretorio(subpasta)
    CriarNovoDiretorio(subpasta + pastaOriginal)
    CriarNovoDiretorio(subpasta + pastaFiltrado)


#Etapa 3
with open(subpasta + pastaOriginal + "\\teste_de_conceitos_data.csv", mode='w') as csv_file:
    fieldnames = ['time', 'value']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for time in range(0,len(x),1):
        writer.writerow({'time': x[time], 'value': y[time]})


#Etapa 4
#4.1
plt.figure()
plt.plot(x,y,'ro')
plt.xlabel('Tempo (s)')
plt.ylabel('Sinal de entrada (int)')
plt.savefig(subpasta + pastaOriginal + 'Função original')

#4.2
plt.figure()
plt.plot(x,y,color='black')
plt.xlabel('Tempo (s)')
plt.ylabel('Sinal de entrada (int)')
plt.savefig(subpasta + pastaOriginal + 'Função original Interpolada')

#4.3
def GerarGráficosDeEquacaoDeDiferencas(x,y,df,df2,xlim,paciente,nomeDoArquivo):
    
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

#derivando por equaçaõ de diferenças  
df = GeraEquacaoDeDiferencas(x,y)
df2 = GeraEquacaoDeDiferencas(x,df)
GerarGráficosDeEquacaoDeDiferencas(x,y,df,df2,N*T,paciente,subpasta + pastaOriginal + 'Equações de Diferenças')

#4.4
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

plt.figure()
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.savefig(subpasta + pastaOriginal + 'FFT')